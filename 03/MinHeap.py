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
        print("Initi")
        self.container = [None for _ in range(initial_size)]
        self.current = 0
        self.maxchild = 2 #2 For Binary representation

    def push(self,element):
        print("Insert")
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
            print("Parent Details")
            print(str(parentIndex))
            #print(parentNode.key)
            print("-------------")
        self.current += 1
    def pop(self):
        print("Pop")

    def heapify(self):
        print("heapify")

    def print(self):
        print("print")
        cnt = 0
        for ele in self.container:
            if ele != None:
                print(str(cnt) +" : "+ele.key +" : "+str(ele.value))
                if ele.parentIndex != None:
                    print("Parent : "+str(ele.parentIndex))
                if ele.leftIndex != None:
                    print("Left : "+str(ele.leftIndex))
                if ele.rightIndex != None:
                    print("Right : "+str(ele.rightIndex))

if __name__ == "__main__":
    length = 16
    minheap = MinHeap(length)
    for i in range(0,length):
        print(str(i))
        node = Node("Key"+str(i),i)
        minheap.push(node)
    minheap.print()