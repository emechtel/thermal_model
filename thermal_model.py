import sys
import os

sys.dont_write_bytecode=True # stops the __pycache__ folder from spawning
os.chdir(os.path.dirname(__file__)) # make current directory the working directory

def author():   # since this is the field deployable version, this will assemble the distance matrices remotely
    os.chdir(os.path.dirname(__file__) + '\library')
    lib = str(os.path.dirname(__file__) + '\library')
    sys.path.append(lib)
    from gutenberg import collate
    os.chdir(os.path.dirname(__file__))

author()


