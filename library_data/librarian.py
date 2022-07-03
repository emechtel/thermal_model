# -*- coding: utf-8 -*-
'''
this is a generator for matrix distances
it will return a set of num .csv files with dimensions num x num
each box represents the solution to a distance value problem
each box represents the distance to the upper left corner of box (1,1,1)
they are to be treated as matrices
NOT like coordinates in xyz space
'''
# NOTE this script is not commented, rather the commetned text represents old commands kept for posterity

import os
import numpy as np
#from scipy import io 

lib = str(os.path.dirname(__file__) + '\library')
os.chdir(lib)
for f in os.listdir(lib):
    os.remove(os.path.join(lib, f))
print("Library cleared")

num = 5

q = np.zeros((num,num))
for z in range(num):
    for x in range (num):
        for y in range (num):
            q[x][y] = (x+1)**2+(y+1)**2+(z+1)**2
    print(str(z/num*100)+'%')
    # io.savemat('distancesz%s.mat' % str(z+1),{"unfiltereddistances": q})
    np.savetxt('distancesz%s.csv' % str(z+1), q, delimiter=',',)
    del q
    q = np.zeros((num,num))
    
print('100%')
#q.astype(np.uint32).tofile('test.bin') #for more compact data sets, set uint[integer] to best value
#io.savemat('distances.mat',{"unfiltereddistances": q})
print('Done')