import sys
import os

sys.dont_write_bytecode=True
os.chdir(os.path.dirname(__file__))

def author():   
    lib = str(os.path.dirname(__file__) + 'library')
    sys.path.insert(1, lib)
    from gutenberg import collate







