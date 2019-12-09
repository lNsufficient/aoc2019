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
 

    def args(self, nbr_params):
        self.address += nbr_params+1
        return self.memory[self.address - nbr_params: self.address]

    def rep(self, i, val):
        self.memory[i] = val

    def add(self):
        args = self.args(3)
        self.rep(args[2], self.memory[args[0]]+self.memory[args[1]]) 

    def mul(self):
        args = self.args(3)
        self.rep(args[2], self.memory[args[0]]*self.memory[args[1]])
 
