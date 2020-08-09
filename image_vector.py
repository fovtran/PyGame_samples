newRGB = np.zeros((height,width,3))   #make empty array to update with RGB values
for i in range(height):
    for j in range(width):                     
        RGB = image[i,j,:]            #RGB vector at given pixel with size 3 since is [R,G,B]
        new = np.dot(W,RGB)           #W is 3x3 matrix of weights
        newRGB[i,j,:] = new           #put new RGB values into the empty matrix

image = mpimg.imread('test.png')   #reading image file into matplotlib.image
print(image.shape)                 #image has shape (height,width,3)
W = np.array([...])                #arbitrary 3x3 matrix of weights  
x = np.rollaxis(image,2,1)         #moving the RGB axis to 2nd position
print(x.shape)                     #x has shape (height,3,width)
Wx = np.dot(W,x)                   #matrix multiplication
print(Wx.shape)                    #Wx has shape (3,height,width)
y = np.rollaxis(Wx,0,3)            #moving RGB axis back to 3rd position to have image shape
print(y.shape)                     #y has shape (height,width,3) like original image

In [9]: np.tensordot(image, W, ([2], [1])).shape
Out[9]: (1000, 1000, 3)

In [13]: np.einsum('ijk,lk->ijl', image, W).shape
Out[13]: (1000, 1000, 3)


In [19]: x = np.rollaxis(image,2,1)

In [20]: Wx = np.dot(W,x)

In [21]: y = np.rollaxis(Wx,0,3)

In [22]: np.allclose(np.tensordot(image, W, ([2], [1])), y)
Out[22]: True

In [14]: np.allclose(np.tensordot(image, W, ([2], [1])), np.einsum('ijk,lk->ijl', image, W))
Out[14]: True

In [15]: %timeit np.einsum('ijk,lk->ijl', image, W)
10 loops, best of 3: 31.1 ms per loop

In [16]: %timeit np.tensordot(image, W, ([2], [1]))
100 loops, best of 3: 18.9 ms per loop