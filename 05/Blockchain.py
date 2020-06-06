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
            sha.update(self.data.encode('utf-8'))
            return sha.hexdigest()

class BlockChain:
      def __init__(self):
            self.head = None

      def push(node):
            if self.head = None:
                  self.head = node


def const_data(data,prevhash):
      block = Block(time.gmtime(),data,prevhash)
      return block


if __name__ == "__main__":
     d1 = const_data("A",None) 
     bchain = BlockChain()

