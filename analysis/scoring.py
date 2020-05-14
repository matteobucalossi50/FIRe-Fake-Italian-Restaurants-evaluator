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
        score = 5
        img = mpimg.imread('images/nonna-open.jpg')
        image = r'images/nonna-open.jpg'
    elif result >= 6 and result <= 10:
        score = 4
        img = mpimg.imread('images/second_generation.jpg')
        image = r'images/second_generation.jpg'
    elif result >= 11 and result <= 15:
        score = 3
        img = mpimg.imread('images/rosie-s-italian-grille.jpg')
        image = r'images/rosie-s-italian-grille.jpg'
    elif result >= 16 and result <= 20:
        score = 2
        img = mpimg.imread('images/olive_garden.jpg')
        image = r'images/olive_garden.jpg'
    else:
        score = 1
        img = mpimg.imread('images/pizza_deep.jpg')
        image = r'images/pizza_deep.jpg'

    return score, img, image


