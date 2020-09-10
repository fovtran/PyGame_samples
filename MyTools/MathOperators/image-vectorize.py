from scipy import misc
from skimage import color
from skimage import measure
import matplotlib.pyplot as plt
import imageio
from skimage.draw import ellipse
from skimage.measure import find_contours, approximate_polygon, subdivide_polygon

#fimg = misc.imread("girl1.jpg")
#fimg = misc.imread("girl2.png")
fimg = imageio.imread("girl2.png")
gimg = color.colorconv.rgb2grey(fimg)

contours = measure.find_contours(gimg, 0.5)


for n, contour in enumerate(contours):
    plt.plot(contour[:, 1], contour[:, 0], linewidth=2)

contour = contours[0]
new_s = contour.copy()
appr_s = approximate_polygon(new_s, tolerance=0.8)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(9, 4))
ax2.plot(contour[:, 0], contour[:, 1])
ax1.plot(appr_s[:, 0], appr_s[:, 1])
plt.show()
