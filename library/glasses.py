import os
import numpy as np

os.system("pip install --upgrade pip")
os.system("pip install Pillow")
from PIL import Image as im

try:
    row = str(os.path.dirname(__file__) + '\\nonfiction')
    num = len([entry for entry in os.listdir(row) if os.path.isfile(os.path.join(row, entry))])

    val = input("There are currently %s slices available for viewing.\nEnter slice value starting at 1: " % str(num))

    shelf = np.loadtxt(str(row + "\\shelf_no%d.csv" % int(val)), delimiter=',')

    max = np.max(shelf)
    min = np.min(shelf)
    range = max-min
    step = 255/range

    image_data = np.uint8(step*(shelf-min))

    os.chdir(os.path.dirname(__file__))

    book = im.fromarray(image_data)
    book.save(str(os.path.dirname(__file__) + "\\book.jpeg"))
    booklet = im.open(str(os.path.dirname(__file__) + "\\book.jpeg"))
    booklet.show('Value Gradient')
    os.remove(str(os.path.dirname(__file__) + "\\book.jpeg"))
except Exception as err:
    print("\nSomething is wrong with you parameters, please try again.\nThe system reutrned the following error message:")
    print("")
    print(err)
    print("")
