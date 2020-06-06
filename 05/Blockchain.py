import hashlib
import time
class Block:
      def __init__(self, timestamp, data, previous_hash):
            self.timestamp = timestamp
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.calc_hash()

      def calc_hash(self):
            sha = hashlib.sha256()
            tempstr = self.data + str(self.timestamp) + str(self.previous_hash)
            sha.update(tempstr.encode('utf-8'))
            return sha.hexdigest()

class BlockChain:
      def __init__(self):
            self.head = None
            self.tail = None
            self.hashmap = {}
      
      def get_tail(self):
            return self.tail
      
      def push(self,node):
            if self.head == None:
                  self.head = node
                  self.tail = node
                  self.hashmap[node.hash] = node
            else:
                  self.tail = node
                  self.hashmap[node.hash] = node
      
      def __str__(self):
            node = self.tail
            outstr = ""
            if node != None:
                  outstr = outstr + (str(node.data) + " <- ")            
                  while node.previous_hash != None:
                        node = self.hashmap[node.previous_hash]
                        outstr = outstr + (str(node.data) + " <- ")            
            return outstr

def const_data(data,prevhash):
      block = Block(time.gmtime(),data,prevhash)
      return block


if __name__ == "__main__":
     d1 = const_data("A",None) 
     print(d1.hash)
     d2 = const_data("B",d1.hash) 
     print(d2.hash)
     bchain = BlockChain()
     bchain.push(d1)
     bchain.push(d2)
     print(bchain)

