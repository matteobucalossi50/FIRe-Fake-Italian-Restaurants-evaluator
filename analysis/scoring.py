import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import subprocess

# other options
'''
ImageViewer(img).show()
image = Image.open('/Users/Matteo/Desktop/NLP/project/FIRe-Fake-Italian-Restaurants-evaluator/images/olive_garden.jpg')
image.show()
p = subprocess.Popen(["display", '/Users/Matteo/Desktop/NLP/project/FIRe-Fake-Italian-Restaurants-evaluator/images/olive_garden.jpg'])
raw_input("Give a name for image:")
p.kill()
'''

# label scores
def scoring(result):
    if result <= 5:
        scores = 5
        img = mpimg.imread('images/nonna-open.jpg')
    elif result >= 6 and result <= 10:
        scores = 4
        img = mpimg.imread('images/second_generation.jpg')
    elif result >= 11 and result <= 15:
        scores = 3
        img = mpimg.imread('images/rosie-s-italian-grille.jpg')
    elif result >= 16 and result <= 20:
        scores = 2
        img = mpimg.imread('images/olive_garden.jpg')
    else:
        scores = 1
        img = mpimg.imread('images/pizza_deep.jpg')

    return scores, img


