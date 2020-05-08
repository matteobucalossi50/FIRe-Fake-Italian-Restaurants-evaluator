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
def scoring(result, doc):
    scores = {}
    if result <= 5:
        scores[doc] = 5
        img = mpimg.imread('nonna-open.jpg')
    elif result >= 6 and result <= 10:
        scores[doc] = 4
        img = mpimg.imread('Red-Sauce-Raos.jpg')
    elif result >= 11 and result <= 15:
        scores[doc] = 3
        img = mpimg.imread('rosie-s-italian-grille.jpg')
    elif result >= 16 and result <= 20:
        scores[doc] = 2
        img = mpimg.imread('olive_garden.jpg')
    else:
        scores[doc] = 1
        img = mpimg.imread('pizza_deep.jpg')

    plt.imshow(img)
    plt.show()
    ok = input("Got it now? (yes/no: ")
    if ok == 'yes':
        plt.close()

    return scores


scoring(result, "Test_menu")

