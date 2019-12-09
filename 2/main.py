import sys

fn = sys.argv[1]
print "Input arg: " + str(fn)
with open(fn, 'r') as f:
    indata = f.read()
print indata

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
 

    def rep(self, i, val):
        self.memory[i] = val

    def add(self):
        i1 = self.memory[self.memory[self.address+1]]
        i2 = self.memory[self.memory[self.address+2]]
        self.rep(self.memory[self.address+3], i1+i2) 
        self.address += 4

    def mul(self):
        args = self.memory[self.address+1:self.address+4]
        self.address += 4
        self.rep(args[2], self.memory[args[0]]*self.memory[args[1]])
 

def rep(l, i, val):
    l[i] = val

def add(l, i):
    rep(l, l[i+3], l[l[i+1]] + l[l[i+2]])

def mul(l, i):
    rep(l, l[i+3], l[l[i+1]]*l[l[i+2]])

in_list = indata.split(',')
in_list = [int(e) for e in in_list]
print "indata: "
print in_list

if fn == "input":
    rep(in_list, 1, 12)
    rep(in_list, 2, 2)
    print "after_replacing: "
print in_list
memory = list(in_list)
i = 0
while(i < len(in_list)):
    command = in_list[i]
    if command == 99:
        print "break:" + str(i)
        break
    if command == 1:
        add(in_list, i)
        i+=4
    elif command == 2:
        mul(in_list, i)
        i+=4
    else:
        print command

print "outdata: "
print in_list

print "trying with intcode class"
intc = Intcode(list(memory))
intc.run()
print intc

def run_sweep_i_j():
    for i in range(100):
        for j in range(100):
            ic = Intcode(list(memory))
            ic.rep(1, i)
            ic.rep(2, j)
            ic.run()
            print i, j, ic.memory[0]
            if ic.memory[0] == 19690720: 
                print "solution is " + str(i*100+j)
                return
run_sweep_i_j()
print "done testing all combinations of i and j"
