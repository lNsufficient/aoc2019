import sys

fn = sys.argv[1]
print "Input arg: " + str(fn)
with open(fn, 'r') as f:
    indata = f.read()
print indata

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

class intcode(object):
    def init(self, memory, address=0):
        self.memory = memory
        self.address = address

    def run():
        pass
 

 

