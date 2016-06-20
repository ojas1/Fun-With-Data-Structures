from kivy.storage.jsonstore import JsonStore

menu_store = JsonStore('menu.json')
ds_data = JsonStore('ds.json')

menu_store.put('Arrays', menu = ['basics', 'create', 'insert', 'delete'])
menu_store.put('Linked List', menu = ['basics', 'create', 'insert', 'delete', 'replace'])
menu_store.put('Queue', menu = ['basics', 'create', 'insert', 'delete'])
menu_store.put('Stack', menu = ['basics', 'create', 'insert', 'delete'])
menu_store.put('Heap', menu = ['basics', 'create', 'insert', 'delete', 'replace'])
menu_store.put('Tree', menu = ['basics', 'create', 'insert', 'delete', 'replace'])
menu_store.put('Graph', menu = ['basics', 'create', 'insert', 'delete', 'replace'])

ds_data.put('Arrays', 
            basics = 'Array is a kind of data structure that can store a fixed-size sequential collection\n'+
            'of elements of the same type\n'+
            'An array is used to store a collection of data,\n'+
            'but it is often more useful to think of an array as a collection of variables of the same type.\n'+
            '\nInstead of declaring individual variables, such as number0, number1, ..., and number99,\n'+
            '\nyou declare one array variable such as numbers and use numbers[0], numbers[1], and ..., numbers[99]'+
            '\nto represent individual variables. A specific element in an array is accessed by an index.'+
            '\nAll arrays consist of contiguous memory locations.\n'+
            '\nThe lowest address corresponds to the first element and the highest address to the last element.')

ds_data.put('Linked List', 
            basics = 'A linked list is a data structure in which the objects are arranged in a linear order.\n'+
            '\nUnlike an array, however, in which the linear order is determined by the array indices, \n'+
            'the order in a linked list is determined by a pointer in each object.\n'+
            '\nLinked Lists provide a simple, flexible representation for dynamic sets,\n'+
            ' supporting(though not necessarily efficiently) all the operations.')

ds_data.put('Queue', 
            basics = 'QUEUE is a DYNAMIC SET in which the element removed from the set is prespecified.\n'+
                        'In a Queue the element deleted is always the one that has been in the set for the longest time:\n'+
                        '     the queue implements a first-in first-out, or FIFO policy.\n'+
                        '\nINSERT OPERATION:\n'+
                        '           We call the insert operation on a queue ENQUEUE\n'+
                        '\nDELETE OPERATION:\n'+
                        '           and we call the delete operation DEQUEUE, it takes no argument.\n'+
                        '\nThe FIFO property of a queue causes it to operate like a line of customers waiting to pay a cashier.\n'
                        '\nThe queue has a head and a tail.\n'+
                        'When an element is enqueued it takes its place at the tail of the queue.\n'+
                        'The element dequeued is always the one at the head of the queue.\n'+
                        '\nWe can implement a queue of atmost n-1 elements using an array of Q[1...n]\n'+
                        '\nThe Queue has an attribute Q.head that indexes or points to its head.\n'+
                        'The attribute Q.tail indexes the next location at which a newly arriving element\n'+
                        'will be inserted into the queue.')

ds_data.put('Stack', 
            basics = 'STACK is a DYNAMIC SET in which the element removed from the set is prespecified.\n'+
                        '\nIn a stack the element deleted from the set is the one most recently inserted:'+
                        '\n   the stack implements a last-in, first-out, or LIFO policy.\n'+
                        '\nINSERT OPERATION:\n'+
                        '         The Insert operation on a stack is often called PUSH.\n'+
                        '\nDELETE OPERATION:\n'+
                        '         The Delete operation which does not take an element argument is often called POP.\n'+
                        '\nWe can implement a stack of at most n elements with an array S[1...n].\n'+
                        'The array has an attribute S.top that indexes the most recently inserted element.\n'+
                        '\nThe stack consists of elements S[1...S.top],\n'+
                        'where S[1] is the element at the bottom of the stack\n'+
                        'and S[S.top] is the element at the top\n'+
                        '\nWhen S.top = 0, the stack contains no element and is empty.'+
                        '\nIf we try to pop an empty stack, we say the stack underflows, which is normally an error.\n'+
                        '\nIf S.top exceeds n, the stack overflows.\n')

ds_data.put('Heap', 
            basics = 'The (binary) heap data structure is an array object that we can view as a\n'+
            'nearly complete binary tree.\n'+
            '\neach node of the tree corresponds to an element of the array.\n'+
            '\nThe tree is completely filled on all levels except possibly the lowest,\n'+
            'which is filled from the left up to a point.\n'+
            '\nAn array A that represents a heap is an object with two attributes:\n'+
            '     A.length, which (as usual) gives the number of elements in the array,\n'+
            '     and A.heap-size, which represents how many elements in the heap are stored within array A.\n'+
            '\nThat is, although A[1...A.length] may contain numbers, only the elements in A[1...A.heap-size],\n'+
            'where 0<=A.heap-size<=A.length, are valid elements of the heap.\n'+
            '\nThe root of the tree is A[1], and given the index i of a node, we can easily compute the indices\n'+
            'of its parent, left child and right child.\n'+
            '\nPARENT(i):\n'+
            '     return floor(i/2)\n'+
            '\nLEFT(i):\n'+
            '     return 2i\n'+
            '\nRIGHT(i):\n'+
            '     return 2i+1\n'+
            '\nThere are two kinds of binary heaps:\n'+
            '     max-heaps and min-heaps')

ds_data.put('Tree', 
            basics = 'arrays are sequential data structures')

ds_data.put('Graph', 
            basics = 'arrays are sequential data structures')
