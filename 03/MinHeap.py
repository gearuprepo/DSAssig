import math
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.leftIndex = None
        self.right = None
        self.rightIndex = None
        self.parent = None
        self.parentIndex = None

class MinHeap:
    def __init__(self,initial_size):
        self.container = [None for _ in range(initial_size)]
        self.current = 0
        self.maxchild = 2 #2 For Binary representation
    # o(n) = 1
    def push(self,element):
        self.container[self.current] = element
        #Construct Tree in parallel using LL
        rtflag = False
        if self.current > 0: # For the element from index 1
            eletemploc = self.current + 1
            parentIndex = math.trunc(eletemploc/self.maxchild) - 1
            parentNode = self.container[parentIndex]
            element.parent = parentNode
            element.parentIndex = parentIndex

            if self.current%2 ==0:
                rtflag = True
                parentNode.right = element
                parentNode.rightIndex = self.current
            else:
                parentNode.left = element
                parentNode.leftIndex = self.current
        pointer = self.current
        while self.container[pointer].parentIndex!=None and (self.container[pointer].value < self.container[pointer].parent.value):
            pointer = self.compareandswap(pointer)
        self.current += 1

    #Needs optimization. Currently using this
    #o(n) = n
    def pop(self):
        retval = self.container[0]
        tempHeap = MinHeap(len(self.container))
        loopcontainer = self.container[1:len(self.container)]
        for ele in loopcontainer:
            if ele!=None:
                newnode = Node(ele.key,ele.value)
                tempHeap.push(newnode)
        self.container = tempHeap.container
        self.current -= 1
        return retval
    
    def size(self):
        return len(list(filter(None,self.container)))

    def compareandswap(self, elementindex):
        cachechild = self.container[elementindex]
        cacheparent = self.container[cachechild.parentIndex]
        parentIndex = cachechild.parentIndex

        newChildBecomesParent = Node(cachechild.key,cachechild.value)
        newParentBecomesChild = Node(cacheparent.key, cacheparent.value)

        newChildBecomesParent.parentIndex = cacheparent.parentIndex
        newChildBecomesParent.parent = cacheparent.parent
        lft = cacheparent.left
        rt = cacheparent.right
        if elementindex%2 ==0:
            rt = newParentBecomesChild
        else:
            lft = newParentBecomesChild
        newChildBecomesParent.left = lft
        newChildBecomesParent.leftIndex = cacheparent.leftIndex
        newChildBecomesParent.right = rt
        newChildBecomesParent.rightIndex = cacheparent.rightIndex


        newParentBecomesChild.parentIndex = cachechild.parentIndex
        newParentBecomesChild.parent = newChildBecomesParent
        if elementindex % 2 == 0:
            self.container[elementindex-1].parent = newChildBecomesParent
        newParentBecomesChild.left = cachechild.left
        newParentBecomesChild.leftIndex = cachechild.leftIndex
        newParentBecomesChild.right = cachechild.right
        newParentBecomesChild.rightIndex = cachechild.rightIndex

        self.container[elementindex] = newParentBecomesChild
        self.container[parentIndex] = newChildBecomesParent

        return parentIndex

    def print(self):
        cnt = 0
        for ele in self.container:
            if ele != None:
                par = self.printhelp(ele.parentIndex)
                lt = self.printhelp(ele.leftIndex)
                rt = self.printhelp(ele.rightIndex)
                print(str(cnt) +" : "+ele.key +" : "+str(ele.value)+", Parent : "+par+", Left : "+lt+", Right : "+rt)
                cnt +=1

    def printhelp(self,input):
        par = None
        if input!= None:
            par = str(input)
        return str(par)

if __name__ == "__main__":
    length = 4
    input = [55,20,5,3,88,20,21,45,1001,393,3,35,77,8,99,44,2,78,32,5,92,723,6,67]
    #input = [55, 88, 1001, 393, 77, 99,  78, 92, 723, 67]
    #input = [ele for ele in reversed(range(0,length))]
    #input = [55, 88, 21, 45]
    minheap = MinHeap(len(input))
    for i in input:
        node = Node("Key"+str(i),i)
        minheap.push(node)
    minheap.print()
    print("Going to POP")
    print(minheap.pop())
    minheap.print()