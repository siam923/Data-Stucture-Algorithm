import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None


    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return 'hash:{}, data:{}, Date_created:{}'.\
                    format(self.calc_hash(),
                        self.data, self.timestamp)

class BlockChain:
    def __init__(self):
        self.head = None
        self.current_block = None
        self.size = 0

    def add_block(self, block):
        if self.head is None:
            self.head = block
        else:
            block.previous_hash = self.current_block.hash
            self.current_block.next = block
        self.current_block = block
        self.size += 1

    def print_block(self):
        if self.head == None:
            print("Block Chain is empty")
        current = self.head
        while current != None:
            print(current)
            current = current.next


block1 = Block('1 June','block1_data')
block2 = Block('2 June','block2_data')
block3 = Block('3 June','block3_data')

block_chain = BlockChain()
block_chain.add_block(block1)
block_chain.add_block(block2)
block_chain.add_block(block3)

block_chain.print_block()

empty_block = BlockChain()
empty_block.print_block()
