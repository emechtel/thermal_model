import sys
import os

sys.dont_write_bytecode=True # stops the __pycache__ folder from spawning
os.chdir(os.path.dirname(__file__)) # make current directory the working directory

def author():   # since this is the field deployable version, this will assemble the distance matrices remotely
    lib = str(os.path.dirname(__file__) + '\library') # define library folder path
    os.chdir(lib) # move to directory for compatibility with older python versions
    sys.path.append(lib) # add path to PATH
    from gutenberg import collate # import and deploy distance repository and file creation function
    sys.path.remove(lib) # remove path from PATH to prevent unwanted searching for future scripts
    os.chdir(os.path.dirname(__file__)) # return to current file directory to run rest of script
    

author()


