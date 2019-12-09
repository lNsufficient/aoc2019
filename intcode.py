class Intcode(object):
    def __init__(self, memory, address=0):
        self.memory = memory
        self.address = address
        self.not_halted = True

    def __str__(self):
        s = "Memory: " + str(self.memory) +"\nAddress:" + str(self.address)
        return s
 
    def run(self):
        while(True):
            command = self.memory[self.address]
            if command == 99:
                print "HALT!"
                break
            if command == 1:
                self.add()
            elif command == 2:
                self.mul()
            else:
                print "Unknown program call:"
                print command
                break;
 

    def get_params(self, nbr_params):
        self.address += nbr_params
        return self.memory[self.address - nbr_params: self.adress]

    def rep(self, i, val):
        self.memory[i] = val

    def add(self):
        i1 = self.memory[self.memory[self.address+1]]
        i2 = self.memory[self.memory[self.address+2]]
        self.rep(self.memory[self.address+3], i1+i2) 
        self.address += 4

    def mul(self):
        args = self.get_params(3)
        self.address += 4
        self.rep(args[2], self.memory[args[0]]*self.memory[args[1]])
 
