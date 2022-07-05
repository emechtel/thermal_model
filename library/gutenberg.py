# -*- coding: utf-8 -*-
'''
this is a generator for matrix distances
it will return a set of num .csv files with dimensions num x num
each box represents the solution to a distance value problem
each box represents the distance to the upper left corner of box (1,1,1)
they are to be treated as matrices
NOT like coordinates in xyz space
'''
#NOTE this script is not commented, rather the commetned text represents old commands kept for posterity

def prose():
    import os
    import numpy as np
    os.chdir(os.path.dirname(__file__))
    old = np.loadtxt("catalog.csv")
    xold, yold, zold, slicesold = int(old[0]), int(old[1]), int(old[2]), int(old[3])
    return xold, yold, zold, slicesold

def collate():
    import os
    import numpy as np
    #from scipy import io 
    ex,why,zee,es = prose()
    row = str(os.path.dirname(__file__) + '\\nonfiction')
    try:
        os.chdir(row)
        for f in os.listdir(row):
            os.remove(os.path.join(row, f))
        print("Repository cleared")
    except:
        lib = os.path.dirname(__file__)
        os.chdir(lib)
        os.makedirs(row)
        os.chdir(row)
        print("Repository cleared")
    finally:
        dewey = np.zeros((ex,why))
        for z in range(zee):
            for x in range (ex):
                for y in range (why):
                    dewey[x][y] = np.float32(((x+0.5)**2+(y+0.5)**2+(z+0.5)**2)**(0.5))
            print(str(z/zee*100)+'%')
            # io.savemat('distancesz%s.mat' % str(z+1),{"unfiltereddistances": q})
            np.savetxt('shelf_no%s.csv' % str(z+1), dewey, delimiter=',')
            del dewey
            dewey = np.zeros((ex,why))
        print('100%')
        #q.astype(np.uint32).tofile('test.bin') #for more compact data sets, set uint[integer] to best value
        #io.savemat('distances.mat',{"unfiltereddistances": q})
        print('Done')


collate()
