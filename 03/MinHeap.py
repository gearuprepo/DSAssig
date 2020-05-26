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
        #Find out parent location
        if self.current > 0: # For the element from index 1
            eletemploc = self.current + 1
            parentIndex = math.trunc(eletemploc/self.maxchild) - 1
            parentNode = self.container[parentIndex]
            element.parent = parentNode
            element.parentIndex = parentIndex
            if self.current%2 ==0:
                # Store in right
                parentNode.right = element
                parentNode.rightIndex = self.current
            else:
                #store in left
                parentNode.left = element
                parentNode.leftIndex = self.current
        self.current += 1
    def pop(self):
        print("Pop")

    def heapify(self):
        print("heapify")

    def print(self):
        cnt = 0
        for ele in self.container:
            if ele != None:
                par = self.printhelp(ele.parentIndex)
                lt = self.printhelp(ele.leftIndex)
                rt = self.printhelp(ele.rightIndex)
                print(str(cnt) +" : "+ele.key +" : "+str(ele.value)+", Parent : "+par+", Left : "+lt+", Right : "+rt)

    def printhelp(self,input):
        par = None
        if input!= None:
            par = str(input)
        return str(par)

if __name__ == "__main__":
    length = 160
    minheap = MinHeap(length)
    for i in range(0,length):
        node = Node("Key"+str(i),i)
        minheap.push(node)
    minheap.print()