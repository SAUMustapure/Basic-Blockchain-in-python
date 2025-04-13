import hashlib

def hashGenerator(data): #so this function takes some data and generates a hash for the block 
    result=hashlib.sha256(data.encode())
    return result.hexdigest()
class Block:
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash

class Blockchain:
    def __init__(self):
        hashLast=hashGenerator('gen_last')
        hashStart=hashGenerator('gen_hash') #here we are randomly generating hashes for the first block     
        genesis=Block('gen_data',hashStart,hashLast) #first block in chain 
        self.chain=[genesis] #made a chain that is an array and pu genesis block in it 
    
    def add_block(self,data):
        prev_hash= self.chain[-1].hash #taking the hash of the last item added in the chain 
        hash= hashGenerator(data+prev_hash) #pass some unique data to the hashgenerator to get a unique hash for your current block 
        block=Block(data,hash,prev_hash) #initialise the block with all the necessary data 
        self.chain.append(block) #added to the chain

bc=Blockchain()
bc.add_block('1')
bc.add_block('2')
bc.add_block('3')

for block in bc.chain:
    print(block.__dict__)