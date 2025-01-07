class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        
           
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        # TODO: 
        temp = DLinkedListNode(item, self.__head, None)
        if self.__head != None: #there is a head
            self.__head.setPrevious(temp)
        else: #there is no head & tail
            self.__tail=temp
        self.__head = temp
        self.__size += 1

        
    def remove(self, item):
        # TODO:
        current = self.__head
        previous=None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
        if (current.getNext() != None):
            current.getNext().setPrevious(previous)
        else:
            self.tail=previous
        self.__size -= 1
        
    def append(self, item):
        # TODO:
        new_node = DLinkedListNode(item,None, None)
        current = self.__head # Start the traversal
        if self.__size == 0: # check if list is empty
            self.add(item)
        else:
            while (current.getNext()!=None):
                current= current.getNext() # traversing the list
            current.setNext(new_node)
            new_node.setPrevious(current)
            self.__size = self.__size +1
        
    def insert(self, pos, item):
        # TODO:
        new_node = DLinkedListNode(item,None,None)
        current = self.__head
        assert isinstance(pos, int), ("not an int")
        assert pos >= 0, ("not positive")
        
        while current != None and pos -1 >= 0:
        
            current= current.getNext()
            pos = pos - 1       
        if current.getNext() == None:
            current.setNext(new_node)
            new_node.setPrevious(current)
            self.__tail = new_node
        elif current.getPrevious() == None:
            current.setPrevious(new_node)
            new_node.setNext(current)
            self.__head = new_node
            print("eggy")
        elif current.getNext() == None and current.getPrevious == None:
            current.setPrevious(new_node)
            new_node.setNext(current)     
            self.__head = new_node
        else:
            current.getPrevious().setNext(new_node)
            current.setPrevious(new_node)
            new_node.setNext(current)
            new_node.setPrevious(current.getPrevious()) 

        
        self.__size = self.__size +1
        
    def pop1(self):
        # TODO:
        current = self.__head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.__head = None
        else:
            previous.setNext(None)
        self.__size = self.__size -1
        return current.getData()
    
    def pop(self, pos=None):
        # TODO:
        # Hint - incorporate pop1 when no pos argument is given
        current = self.__head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.__head = None
        else:
            previous.setNext(None)
        self.__size = self.__size - 1
        return current.getData()
        
    def searchLarger(self, item):
        # TODO:
        current = self.__head
        index = 0
        while current != None:
            if current.getData() > item:
                return index
            else:
                current = current.getNext()
                index = index + 1
        
        return(-1)
        
    def getSize(self):
        # TODO:    
        return self.__size
    
    def getItem(self, pos):
        # TODO:   
        if pos < 0:
            pos = self.__size + pos
        current = self.__head
        assert pos < self.__size, ("too big")
        while current != None and pos > 0:
        
            current= current.getNext()
            pos = pos - 1
            if current.getNext() == None:
                return(current.getData())            
            
        return(current.getData())        
        
    
        
    def __str__(self):
        # TODO:   
        current = self.__head
        string = ''
        while current != None:
            string = string + str(current.getData())+ ' '
            current = current.getNext()            
        return string[0:-1]


def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
    print(str(int_list))
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

                
if __name__ == '__main__':
    test()
