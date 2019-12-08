import numpy as np
import sys 

fn = "input"
with open(fn, 'r') as f:
    indata = f.read()

print indata
imsize = (6, 25) # (rows, cols)
nbr_layers = len(indata)/(imsize[0]*imsize[1])
im = np.empty((nbr_layers,)+imsize)
print nbr_layers

for layer in range(nbr_layers):
    for j in range(imsize[0]):
        for i in range(imsize[1]):
            im[layer, j, i] = int(indata[i+j*25+layer*imsize[1]*imsize[0]])

print im

nbr_zeros = np.sum(im == 0, axis = (1,2))

print nbr_zeros
row = np.argmin(nbr_zeros)

print row
imlayer = im[row]
ones = np.sum(imlayer == 1)
twos = np.sum(imlayer == 2)
print ones, twos
print ones*twos
print "Answer to first task is: " + str(ones*twos)
print "CORRECT" 

first_non2 = lambda(x): int(x[np.argmax(x<2)])
dec = np.apply_along_axis(first_non2, 0, im)
print dec
print "Answer to second task is: LJECH"
print "CORRECT"
