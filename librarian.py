# this program refernces and edits the paramters for the thermal model

def query():
    import tkinter as kit
    import numpy as np
    import os

    # change to current folder directory
    os.chdir(os.path.dirname(__file__) + "\library")

    # get the old paramter values for prefilling the GUI text input
    old = np.loadtxt("catalog.csv")
    xold, yold, zold, slicesold = int(old[0]), int(old[1]), int(old[2]), int(old[3])

    # define the GUI window and assign title
    librarian = kit.Tk()
    librarian.title("Librarian")

    # save variables function
    def savedata():
        global params
        x = int(xq.get())
        y = int(yq.get())
        z = int(zq.get())
        slices = int(slicesq.get())
        params = list((x,y,z,slices))
        librarian.destroy()

    # make label for x-axis values, and give option for user input
    kit.Label(librarian, text="Enter x-axis chamber dimension (mm):").pack()
    xq = kit.Entry(librarian)
    xq.insert(0, xold) #insert old values for user to edit
    xq.pack() #implement label and text input, .pack() will not work with the .get() in the save function when used as method

    # make label for y-axis values, and give option for user input
    kit.Label(librarian, text="Enter x-axis chamber dimension (mm):").pack()
    yq = kit.Entry(librarian)
    yq.insert(0, yold)
    yq.pack()

    # make label for z-axis values, and give option for user input
    kit.Label(librarian, text="Enter z-axis chamber dimension (mm):").pack()
    zq = kit.Entry(librarian)
    zq.insert(0, zold)
    zq.pack()

    # make label for slice precision, and give option for user input
    kit.Label(librarian, text="Enter number of slices to use for computional precision:").pack()
    slicesq = kit.Entry(librarian)
    slicesq.insert(0, slicesold)
    slicesq.pack()


    # save button
    kit.Button(librarian, command=savedata, text="Save Changes").pack()

    #implement the GUI window
    librarian.mainloop()

    vessel = np.array(params)
    np.savetxt('catalog.csv', vessel, delimiter=',')


query()