import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# label scores
def scoring(result, doc):
    scores = {}
    if result <= 5:
        scores[doc] = 5
        img = mpimg.imread('nonna-open.jpg')
        plt.imshow(img)
        plt.show()
    elif result >= 6 and result <= 10:
        scores[doc] = 4
        img = mpimg.imread('Red-Sauce-Raos.jpg')
        plt.imshow(img)
        plt.show()
    elif result >= 11 and result <= 15:
        scores[doc] = 3
        img = mpimg.imread('rosie-s-italian-grille.jpg')
        plt.imshow(img)
        plt.show()
    elif result >= 16 and result <= 20:
        scores[doc] = 2
        img = mpimg.imread('olive_garden.jpg')
        plt.imshow(img)
        plt.show()
    else:
        scores[doc] = 1
        img = mpimg.imread('pizza_deep.jpg')
        plt.imshow(img)
        plt.show()

    return scores

scoring(result, "Test_menu")

