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

    def push(self,element):
        self.container[self.current] = element
        #Construct Tree in parallel using LL
        if self.current > 0: # For the element from index 1
            eletemploc = self.current + 1
            parentIndex = math.trunc(eletemploc/self.maxchild) - 1
            parentNode = self.container[parentIndex]
            element.parent = parentNode
            element.parentIndex = parentIndex
            if self.current%2 ==0:
                parentNode.right = element
                parentNode.rightIndex = self.current
            else:
                parentNode.left = element
                parentNode.leftIndex = self.current
        pointer = self.current
        while self.container[pointer].parentIndex!=None and (self.container[pointer].value < self.container[pointer].parent.value):
            pointer = self.compareandswap(pointer)

        self.current += 1
    def pop(self):
        print("Pop")

    def compareandswap(self, elementindex):
        cachechild = self.container[elementindex]
        cacheparent = self.container[cachechild.parentIndex]
        parentIndex = cachechild.parentIndex

        newChildBecomesParent = Node(cachechild.key,cachechild.value)
        newChildBecomesParent.parentIndex = cacheparent.parentIndex
        newChildBecomesParent.parent = cacheparent.parent
        newChildBecomesParent.left = cacheparent.left
        newChildBecomesParent.leftIndex = cacheparent.leftIndex
        newChildBecomesParent.right = cacheparent.right
        newChildBecomesParent.rightIndex = cacheparent.rightIndex

        newParentBecomesChild = Node(cacheparent.key,cacheparent.value)
        newParentBecomesChild.parentIndex = cachechild.parentIndex
        newParentBecomesChild.parent = cachechild.parent
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
    length = 15
    #input = [3,55,20,1,5,88,20,21,45,1001,393,5,35,77,3,8,3,99,44,78,32,92,723,67]
    input = [ele for ele in reversed(range(0,length))]
    minheap = MinHeap(len(input))
    for i in input:
        node = Node("Key"+str(i),i)
        minheap.push(node)
    minheap.print()