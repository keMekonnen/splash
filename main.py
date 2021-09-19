def read(inp:str, direc:bool = False):
    # function to read in a file as ones and zeros in a string or clean up a given string to have only ones and zeros
    if not direc:
        data = bin(int((open(inp, 'rb').read().hex())[2:], 16))[2:] # what a mess
        return data
    else:
        data = ''
        for i in inp:
            if i == '0' or i == '1':
                data += i
        return data

def deflate(inp: str, keysize: int= 256):
    # iterative function to squeeze the input to be less tahn the key size
    while len(inp)/4 > keysize:
        digest = ''
        i = 2
        while i < len(inp)+2:
            s = i-2
            sec = inp[s:i]
            if sec == '00':
                digest += '1'
            elif sec == '01':
                digest += '0'
            if sec == '11':
                digest += '1'
            else:
                digest += '0'
            i+=2
        inp = digest
    return inp

def inflate(inp:str, keysize:int=256):
    # iterative function to blow up the input into the right size
    i = 0
    while len(inp)/4 < keysize:
        inp += str(i%2)
        i+=1
    return inp

def splash(inp:str, keysize:int=256):
    # function to hash the input into the right size
    inpL = len(inp)/4
    if inpL > keysize:
        inp = deflate(inp, keysize) 
    inpL = len(inp)/4
    if inpL < keysize:
        inp = inflate(inp,keysize)
    return inp