#Huffman Coding
import sys
sys.path.append(".")
from MinHeap import MinHeap
from MinHeap import Node

class HuffCode:
    def __init__(self):
        self.freqmap = dict()
        self.treedict = dict()

    def huffman_encoding(self,data):
        print(data)
        # Construct Frequency map -> O(n)
        for char in data:
            self.freqmap[char] = self.freqmap.get(char, 0) + 1
        print(self.freqmap)

        # Construct priority queue for frequency map
        minheap = MinHeap(len(self.freqmap))
        for ele in self.freqmap:
            minheap.push(Node(str(ele),str(self.freqmap.get(ele))))
        minheap.print()

        # Encode tree process
        size = len(minheap.container)
        while size>0:
            size = len(minheap.container)
            ele1 = minheap.pop()
            ele2 = minheap.pop()
            sumfreq = ele1.value + ele2.value
            concat = ele1.key + ele2.key
            minheap.push(Node(concat,sumfreq))
            self.updatetreedict(ele1,ele2)
            size = len(minheap.container)

        # encode data
        pass

    def updatetreedict(self,e1,e2):
        n1 = self.treedict.get(e1.key)
        if n1 == None:
            n1 = Node(e1.key,e1.value)
        else:
            self.treedict.pop(e1.key)
        
        n2 = self.treedict.get(e2.key)
        if n2 == None:
            n2 = Node(e2.key,e2.value)
        else:
            self.treedict.pop(e2.key)
        
        sumfreq = n1.value + n2.value
        concat = n1.key + n2.key
        treenode = Node(concat,sumfreq)
        treenode.left = n1
        treenode.right = n2
        self.treedict[concat] = treenode
    

    def huffman_decoding(data,tree):
        print(data)
        pass


    def encode_tree_process():
        print("In Core process")
        # find 2 min elements from priority Queues
        # Remove 2 elements from priority queue
        # Merge elements and create a new node
        # reinsert new element to PQ


a_great_sentence = "The bird is the word"
print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))
hcode = HuffCode()
#encoded_data, tree = \
hcode.huffman_encoding(a_great_sentence)
#print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#print ("The content of the encoded data is: {}\n".format(encoded_data))

    #decoded_data = huffcode.huffman_decoding(encoded_data, tree)

    #print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #print ("The content of the encoded data is: {}\n".format(decoded_data))