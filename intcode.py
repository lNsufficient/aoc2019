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
            print self.memory
            instruction = self.memory[self.address]
            command = instruction%100
            param_modes = instruction/100
            if command == 99:
                print "HALT!"
                break
            elif command == 1:
                fun = self.add
            elif command == 2:
                fun = self.mul
            elif command == 3:
                fun = self.inp
            elif command == 4:
                fun = self.out
            else:
                print "Unknown program call:"
                print command
                break;
            fun(param_modes)
 
    def pos_or_val(self, a, is_val):
        print is_val
        if is_val:
            print "val"
            return a
        else:
            print "mem"
            return self.memory[a]

    def args(self, nbr_params, param_modes):
        self.address += nbr_params+1
        args = self.memory[self.address - nbr_params: self.address]
        param_modes = [int(e) for e in list(str(param_modes))[::-1]]
        param_modes = param_modes + [0]*(len(args)-len(param_modes))
        end_arg = args[-1]
        args = [self.pos_or_val(arg, is_val) for arg, is_val in zip(*(args, param_modes))] 
        args[-1] = end_arg
        print args
        return args

    def rep(self, i, val):
        print i
        self.memory[i] = val

    def add(self, param_modes):
        args = self.args(3, param_modes)
        self.rep(args[2], args[0] + args[1]) 

    def mul(self, param_modes):
        args = self.args(3, param_modes)
        self.rep(args[2], args[0]*args[1])

    def inp(self, param_modes):
        args = self.args(1, param_modes)
        v = raw_input('input number to opcode 3:')
        self.rep(args[0], v)
 
    def out(self, param_modes):
        args = self.args(1, param_modes)
        print(str(args[0]))

 
