#Huffman Coding
import sys
sys.path.append(".")
from MinHeap import MinHeap
from MinHeap import Node

class HuffCode:
    def reset(self):
        self.freqmap = dict()
        self.treedict = dict()
        self.codemap = dict()

    def __init__(self):
        self.reset()

    #O(n) = n^2 + 4n
    def huffman_encoding(self,data):
        if len(data) == 0:
            raise Exception("No Data to encode") 
        print("---Start huffman coding------")
        # Construct Frequency map -> O(n)=n
        for char in data:
            self.freqmap[char] = self.freqmap.get(char, 0) + 1

        # Construct priority queue for frequency map -> O(n)=n
        minheap = MinHeap(len(self.freqmap))
        for ele in self.freqmap:
            minheap.push(Node(str(ele),str(self.freqmap.get(ele))))

        # Encode tree process -> O(n) = n^2 + 2n
        size = minheap.size()
        #Fix for boundary conditions.
        if size == 1:
            ele1 = minheap.pop()
            self.treedict[ele1.key] = ele1          
        while size>1: # n^2
            ele1 = minheap.pop() #n
            ele2 = minheap.pop() #n
            sumfreq = ele1.value + ele2.value
            concat = ele1.key + ele2.key
            minheap.push(Node(concat,sumfreq))
            self.updatetreedict(ele1,ele2)
            size = minheap.size()
        treedictcore = self.treedict[list(self.treedict)[0]]
        
        # form coding map O(n) = n
        for key in self.freqmap: #n
            cha = key
            hcode = ''
            if len(self.freqmap) == 1:
                hcode = '0'
            hcode = (self.findcode(treedictcore,cha,hcode)[0])
            self.codemap[key] = hcode
        

        # Code the input string
        hestring = ''
        for ch in data:
            hestring = hestring + self.codemap[ch]
        
        rettree = self.treedict[list(self.treedict)[0]]
        return hestring,rettree

    def findcode(self,tree,cha,hcode):
        if cha in tree.key:
            if len(tree.key) == 1:
                return hcode,tree
            else:
                if cha in tree.left.key:
                    return self.findcode(tree.left,cha,hcode+'0')
                if cha in tree.right.key:
                    return self.findcode(tree.right,cha,hcode+'1')
        return hcode,tree

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
    
    #O(n) = nlogn
    def huffman_decoding(self,data,tree):
        print("---Start huffman de-coding------")
        if len(data) == 0:
            raise Exception("No Data to encode") 
        byte = data
        retstring = ''
        #For fixing boundary condition issues
        singlenodeflag = False
        if tree.left == None and tree.right == None:
            singlenodeflag = True
        while len(byte)>0:
            cnt = 0
            bound,tempretstring = self.traverse(byte,tree,cnt)
            if singlenodeflag:
                bound +=1
            byte = byte[bound:len(byte)]
            retstring += tempretstring
        return retstring
    
    def traverse(self,byte,tree,cnt):
        
        if len(tree.key) == 1:
            return cnt,tree.key
        else:
            bit = byte[0]
            byte = byte[1:len(byte)]
            cnt += 1
            if bit =='0':
                return self.traverse(byte,tree.left,cnt)
            else:
                return self.traverse(byte,tree.right,cnt)  

    

#a_great_sentence = "The bird is the word"
#Test case 2
print("Test case 1")
a_great_sentence = "T"
print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))
huffcode = HuffCode()
encoded_data, tree = huffcode.huffman_encoding(a_great_sentence)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = huffcode.huffman_decoding(encoded_data, tree)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

#Test case 2
print("Test case 2")
a_great_sentence = "Testing Huffman's coding"
print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))
huffcode = HuffCode()
encoded_data, tree = huffcode.huffman_encoding(a_great_sentence)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = huffcode.huffman_decoding(encoded_data, tree)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

#Test case 3
print("Test case 3")
a_great_sentence = "AAAAAAA"
print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))
huffcode = HuffCode()
encoded_data, tree = huffcode.huffman_encoding(a_great_sentence)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = huffcode.huffman_decoding(encoded_data, tree)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))


#Test case 4
print("Test case 4")
a_great_sentence = ""
print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))
huffcode = HuffCode()
encoded_data, tree = huffcode.huffman_encoding(a_great_sentence)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = huffcode.huffman_decoding(encoded_data, tree)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))