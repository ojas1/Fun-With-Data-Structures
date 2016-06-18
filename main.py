from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.uix.label import Label
from kivy.uix.button import Button
from random import random
from kivy.lang import Builder 
from kivy.uix.scrollview import ScrollView
from kivy.uix.togglebutton import ToggleButton
from functools import partial 
from random import random
from kivy.clock import Clock
import insert_data

# to get the reference to ds widget 
action_widget = Widget()
current_ds = ''
#True when basics section is displayed
basics_present = False
# True after ds is created 
ds_present = False
ds = []
# head of the link list
head_of_list = None
# tail of the queue
q_tail = -1
# front of the queue
q_front = 0
# top of the stack
stack_top = -1
# size of the stack
stack_size = 0
# True when ds is created but not displayed
ds_in_background = False

def clearmsg(dt): action_widget.error_messages.clear_widgets()

class ArrayElementWidget(BoxLayout):
    pass

class ArrayCreationWidget(BoxLayout):

    def create_array(self, size):
        try: s = int (size)
        except: return 
        global ds_present, ds, ds_in_background
        ds = []
        # Array is created and will be displayed
        ds_present = True
        ds_in_background = False
        #clear everything before displaying the new array
        action_widget.disp_sec.clear_widgets()
        # display the new array
        for i in range(int(size)):
            e = ArrayElementWidget()
            ds.append(e)
            action_widget.disp_sec.add_widget(e)
            e.address.text = str(100+i*4)
            e.index.text = str(i)
            e.val.text = 'Garbage'


class ArrayInsertionWidget(BoxLayout):

    def insert_data(self, data, pos):
        if (len(ds)): 
            if len(ds) > int(pos): ds[int(pos)].val.text = data


class ArrayDeletionWidget(BoxLayout):

    def delete_data(self, btn):
        try:
            pos = int(self.pos_or_data_val.text) 
            if pos < len(ds):
                i = pos
                while(i<len(ds)-1):
                    ds[i].val.text = ds[i+1].val.text
                    i +=1
            ds[len(ds)].val.text = 'value same but not in the array'
        except: return 


class ArrayReplacementWidget(BoxLayout):
    def replace_data(self, opt, btn):
        try:
            if opt == 'addr':
                pos = int(self.pos_or_data_to_replace.text)
                if pos < len(ds): ds[pos].val.text = self.replacement.text
            else:
                data = int(self.pos_or_data_to_replace.text)
                ds = [self.replacement.text for d in ds if int(d.val.text) == data]
        except: print "error"


class LLHeadWidget(BoxLayout): pass

class LLElementWidget(BoxLayout): pass

class LLCreationWidget(BoxLayout):

    def create_ll(self):
        global ds, head_of_list
        ds = []
        # Array is created and will be displayed
        ds_present = True
        ds_in_background = False
        #clear everything before displaying the new array
        action_widget.disp_sec.clear_widgets()
        ll_head = LLHeadWidget()
        head_of_list = ll_head
        action_widget.disp_sec.add_widget(ll_head)
        ll_head.head_address.text = str(int(10000*random()))
        ll_head.pointsto.text = 'null'        


class LLInsertionWidget(BoxLayout):

    def insert_data_front(self, data_in_ll):
        global ds, head_of_list
        if head_of_list:
            action_widget.disp_sec.clear_widgets()
            # create a new LL node
            new_le = LLElementWidget()
            #assign a random address
            new_le.node_address.text = str(int(10000*random()))
            #assign a value
            new_le.val.text = data_in_ll.text
            # next of the new node points to next of head
            new_le.nextptr.text = head_of_list.pointsto.text
            # head points to new node
            head_of_list.pointsto.text = new_le.node_address.text
            # add the new node to the global ds list
            ds = [new_le] + ds
            action_widget.disp_sec.add_widget(head_of_list)
            for d in range(ds):
                action_widget.disp_sec.add_widget(d)


    def insert_data_end(self, data_in_ll):
        global ds, head_of_list
        if len(ds) == 0:
            self.insert_data_front(data_in_ll)
            return 
        if head_of_list:
            action_widget.disp_sec.clear_widgets()
            action_widget.disp_sec.add_widget(head_of_list)
            # create a new LL node
            new_le = LLElementWidget()
            #assign a random address
            new_le.node_address.text = str(int(10000*random()))
            #assign a value
            new_le.val.text = data_in_ll.text
            # next of the new node points to null
            new_le.nextptr.text = 'null'
            # last node points to new node
            ds[len(ds)-1].nextptr.text = new_le.node_address.text
            # add the new node to the global ds list
            ds.append(new_le)
            for d in range(ds): action_widget.disp_sec.add_widget(d)


    def insert_data_at(self, data_in_ll, pos):
        global ds, head_of_list
        try:
            pos = int(pos.text)-1
            data = int(data_in_ll.text)
        except:
            print 'invalid data or pos'
            return 
        if pos > len(ds) or pos < 0: return 
        if pos == 0:
            self.insert_data_front(data_in_ll)
            return 
        action_widget.disp_sec.clear_widgets()
        try:
            action_widget.disp_sec.add_widget(head_of_list)        
            # create a new LL node
            new_le = LLElementWidget()
            #assign a random address
            new_le.node_address.text = str(int(10000*random()))
            #assign a value
            new_le.val.text = data_in_ll.text
            # next of the new node points to next of previous
            new_le.nextptr.text = ds[pos-1].nextptr.text
            ds[pos-1].nextptr.text = new_le.node_address.text
            # add the new node to the global ds list
            last = ds[pos:]
            ds = ds[:pos]+[new_le]
            ds = ds + last
            for i in ds: action_widget.disp_sec.add_widget(i)
        except: return

class LLDeletionWidget(BoxLayout):
    def delete_data(self, pos):
        global ds, head_of_list
        try: pos = int(pos)-1
        except: return
        if pos <0 or pos > len(ds)-1: return 
        if len(ds) > 0:
            action_widget.disp_sec.remove_widget(ds[pos])
            if pos == 0: head_of_list.pointsto.text = ds[pos].nextptr.text
            else: ds[pos-1].nextptr.text = ds[pos].nextptr.text
            del ds[pos]

class LLReplacementWidget(BoxLayout):
    def replace_node(self, pos):
        global ds, head_of_list
        
        try:pos = int(pos)-1
        except:return 
        
        if pos < 0 or pos > len(ds) - 1:return 

        if len(ds) > 0:
            new_node = LLElementWidget()
            new_node.node_address.text = str(int(random()*1000))
            new_node.nextptr.text = ds[pos].nextptr.text
            if pos == 0: head_of_list.pointsto.text = ds[pos].node_address.text
            else: ds[pos-1].nextptr.text = new_node.node_address.text
            ds[pos] = new_node
            action_widget.disp_sec.clear_widgets()
            action_widget.disp_sec.add_widget(head_of_list)
            for i in range(len(ds)):
                action_widget.disp_sec.add_widget(ds[i])

class QueueElementWidget(BoxLayout):
    pass

class QueueCreationWidget(BoxLayout):
    def create_queue(self, size):
        action_widget.disp_sec.clear_widgets()
        global ds
        ds = []

        for i in range(int(size)):
            nqe = QueueElementWidget()
            nqe.address.text = str(1000+i*4)
            ds.append(nqe)
            action_widget.disp_sec.add_widget(ds[i])
    
class QueueInsertionWidget(BoxLayout):

    def insert_data(self, data):
        global ds, q_tail, q_front
        sign = 1 
        if q_tail<0: sign = -1
        q_tail +=1
        q_tail = (len(ds)+q_tail)%len(ds)
        if q_tail == q_front and sign>0:
            action_widget.error_messages.add_widget(Label(text='queue overflow', color= [0,0,0,1]))
            Clock.schedule_once(clearmsg, 2)
            return
        ds[q_tail].val.text = data

class QueueDeletionWidget(BoxLayout):
    def delete_data(self):
        global ds, q_tail, q_front
        if q_tail > 0:                
            ds[q_front].val.text = ''
            if q_front == q_tail: 
                q_front =0
                q_tail = -1
            else: q_front +=1 

class QueueReplacementWidget(BoxLayout): pass
    
class StackElementWidget(BoxLayout): pass

class StackCreationWidget(BoxLayout):
    def create_stack(self, size):
        global ds, stack_top, stack_size
        stack_size = int(size)
        if stack_size>0:
            action_widget.disp_sec.clear_widgets()
            for i in range(stack_size):
                sw = StackElementWidget()
                sw.address.text = str(1000 + i*4)
                ds.append(sw)
                action_widget.disp_sec.add_widget(sw)
                
class StackInsertionWidget(BoxLayout):

    def push(self, data):
        global ds, stack_top, stack_size
        if stack_top  == stack_size-1:
            action_widget.error_messages.clear_widgets()
            action_widget.error_messages.add_widget(Label(text='stack overflow', color= [0,0,0,1]))
            Clock.schedule_once(clearmsg, 2)
            return

        else:
            stack_top +=1
            ds[stack_top].val.text = data

class StackDeletionWidget(BoxLayout):
    def pop(self):
        global ds, stack_top
        if stack_top == -1:
            action_widget.error_messages.clear_widgets()
            action_widget.error_messages.add_widget(Label(text='stack underflow', color= [0,0,0,1]))
            Clock.schedule_once(clearmsg, 2)
            return
        else:
            ds[stack_top].val.text = ''
            stack_top -=1

class StackReplacementWidget(BoxLayout): pass
class HeapElementWidget(BoxLayout): pass
class HeapCreationWidget(BoxLayout):

    def create_heap(self, size):
        pass
 
    
class HeapInsertionWidget(BoxLayout): pass
class HeapDeletionWidget(BoxLayout): pass
class HeapReplacementWidget(BoxLayout): pass
class TreeElementWidget(BoxLayout): pass

class TreeCreationWidget(BoxLayout):

    def create_tree(self, size): pass
 

class TreeInsertionWidget(BoxLayout): pass
class TreeDeletionWidget(BoxLayout): pass
class TreeReplacementWidget(BoxLayout): pass
class GraphElementWidget(BoxLayout): pass

class GraphCreationWidget(BoxLayout):

    def create_graph(self, size): pass
 
    
class GraphInsertionWidget(BoxLayout): pass
class GraphDeletionWidget(BoxLayout): pass
class GraphReplacementWidget(BoxLayout): pass
# menu button in the ds widget menu section 
class MenuButton(Button):
    def perform_action(self, action):
        global basics_present, ds, current_ds, ds_in_background, ds_present
        # clear the input section everytime a menu button is pressed
        action_widget.oprtn_input.clear_widgets()
        # if the basics content is displayed clear it.
        if basics_present == True:
            action_widget.disp_sec.clear_widgets()
            basics_present = False
#        if current_ds == 'Arrays':
            # if basics menu is selected 
        if action == 'basics':
            #clear everything before displaying the content 
            action_widget.disp_sec.clear_widgets()
            # show the basics
            action_widget.disp_sec.add_widget(
                                            Label(
                                                text=insert_data.ds_data.get(action_widget.ds_widget.text)[action],
                                                color=[0,0,0,1]))
            # the basics section is on display and the ds is in background if present
            basics_present = True
            if ds_present: ds_in_background = True
        # if create menu is selected
        elif action == 'create':
            # clear the display
            action_widget.disp_sec.clear_widgets()
            # the ds has not been created yet and if previously it was created it has been deleted
            ds_present = False
            # there is no ds present in background
            ds_in_background = False
            # basics section is not on display
            basics_present = False
            if current_ds == 'Arrays':
                action_widget.oprtn_input.add_widget(ArrayCreationWidget())
            elif current_ds == 'Linked List':
                action_widget.oprtn_input.add_widget(LLCreationWidget())
            elif current_ds == 'Queue':
                action_widget.oprtn_input.add_widget(QueueCreationWidget())
            elif current_ds == 'Stack':
                action_widget.oprtn_input.add_widget(StackCreationWidget())
            elif current_ds == 'Heap':
                action_widget.oprtn_input.add_widget(HeapCreationWidget())
            elif current_ds == 'Tree':
                action_widget.oprtn_input.add_widget(TreeCreationWidget())
            elif current_ds == 'Graph':
                action_widget.oprtn_input.add_widget(GraphCreationWidget())

        else:
            # if ds is present and in the background
            if ds_present == True and ds_in_background == True:
                # display the ds
                for d in range (ds):
                    action_widget.disp_sec.add_widget(d)
                    # the ds is no longer in the background
                    ds_in_background = False
                    basics_present = False

            if action == 'insert':
                if current_ds == 'Arrays':
                    action_widget.oprtn_input.add_widget(ArrayInsertionWidget())
                elif current_ds == 'Linked List':
                    action_widget.oprtn_input.add_widget(LLInsertionWidget())
                elif current_ds == 'Queue':
                    action_widget.oprtn_input.add_widget(QueueInsertionWidget())
                elif current_ds == 'Stack':
                    action_widget.oprtn_input.add_widget(StackInsertionWidget())
                elif current_ds == 'Heap':
                    action_widget.oprtn_input.add_widget(HeapInsertionWidget())
                elif current_ds == 'Tree':
                    action_widget.oprtn_input.add_widget(TreeInsertionWidget())
                elif current_ds == 'Graph':
                    action_widget.oprtn_input.add_widget(GraphInsertionWidget())            

            elif action == 'delete':
                if current_ds == 'Arrays':
                    arr_del_w = ArrayDeletionWidget()
                    action_widget.oprtn_input.add_widget(arr_del_w)
                    selected_opt = [option for option in ToggleButton.get_widgets('oprtn_type') if option.state == 'down'][0]
                    arr_del_w.delete_button.bind(on_press = arr_del_w.delete_data)
                elif current_ds == 'Linked List':
                    action_widget.oprtn_input.add_widget(LLDeletionWidget())
                elif current_ds == 'Queue':
                    action_widget.oprtn_input.add_widget(QueueDeletionWidget())
                elif current_ds == 'Stack':
                    action_widget.oprtn_input.add_widget(StackDeletionWidget())
                elif current_ds == 'Heap':
                    action_widget.oprtn_input.add_widget(HeapDeletionWidget())
                elif current_ds == 'Tree':
                    action_widget.oprtn_input.add_widget(TreeDeletionWidget())
                elif current_ds == 'Graph':
                    action_widget.oprtn_input.add_widget(GraphDeletionWidget())
            
            elif action == 'replace':
                if current_ds == 'Arrays':
                    arr_repl_w = ArrayReplacementWidget()
                    action_widget.oprtn_input.add_widget(arr_repl_w)
                    arr_repl_w.repl_btn.bind(on_press = partial(arr_repl_w.replace_data,
                        [option for option in ToggleButton.get_widgets('oprtn_type_repl') if option.state == 'down'][0].text))
                elif current_ds == 'Linked List':
                    action_widget.oprtn_input.add_widget(LLReplacementWidget())
                elif current_ds == 'Queue':
                    action_widget.oprtn_input.add_widget(QueueReplacementWidget())
                elif current_ds == 'Stack':
                    action_widget.oprtn_input.add_widget(StackReplacementWidget())
                elif current_ds == 'Heap':
                    action_widget.oprtn_input.add_widget(HeapReplacementWidget())
                elif current_ds == 'Tree':
                    action_widget.oprtn_input.add_widget(TreeReplacementWidget())
                elif current_ds == 'Graph':
                    action_widget.oprtn_input.add_widget(GraphReplacementWidget())

# widgets to display data structure details.
class DataStrWidget(BoxLayout):

    def __init__(self, **kwargs): super(DataStrWidget, self).__init__(**kwargs)   


# home page list button
class DSButton(ListItemButton): pass
	
# Root class of the app
class VisualRoot(BoxLayout):  
          
     # return home
    def return_home(self):
        self.clear_widgets()
        self.add_widget(VisualRoot())
	

	# function to respond to ds option selected
    def go_to_the_ds(self, selected_ds):
        global current_ds, action_widget 
        current_ds = selected_ds 
        self.clear_widgets()
        w = DataStrWidget(size=Window.size)
        action_widget = w
        self.add_widget(w)
        w.ds_widget.text = selected_ds
        menu_box = BoxLayout(orientation='vertical')
        menu_widget = []
        for i in range(5):
            menu_widget.append(MenuButton(text=insert_data.menu_store.get(selected_ds)['menu'][i]))
            menu_box.add_widget(menu_widget[i])
        w.menu.add_widget(menu_box)


	# function to select the operation on array
class FunWithDSApp(App): pass
	
if __name__ == '__main__':
    Builder.load_file('array.kv')
    Builder.load_file('linklist.kv')
    Builder.load_file('queue.kv')
    Builder.load_file('stack.kv')
    Builder.load_file('heap.kv')
    Builder.load_file('tree.kv')
    Builder.load_file('graph.kv')
    FunWithDSApp().run() 
