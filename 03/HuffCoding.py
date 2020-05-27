#Huffman Coding
import sys
sys.path.append(".")
from MinHeap import MinHeap
from MinHeap import Node
class HuffCode:
    def __init__(self):
        self.freqmap = dict()

    def huffman_encoding(this,data):
        print(data)
        # Construct Frequency map -> O(n)
        for char in data:
            this.freqmap[char] = this.freqmap.get(char, 0) + 1
        print(this.freqmap)

        # Construct priority queue for frequency map
        minheap = MinHeap(len(this.freqmap))
        for ele in this.freqmap:
            minheap.push(Node(str(ele),str(this.freqmap.get(ele))))
        minheap.print()

        # Encode tree process
        size = len(minheap.container)
        while size>0:
            minheap.pop()
            size = len(minheap.container)
            minheap.print()
        # encode data
        pass

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