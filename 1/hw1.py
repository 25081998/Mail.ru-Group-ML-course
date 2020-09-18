import cv2
from matplotlib import pyplot as plt
im = cv2.imread("big.jpg")

plt.imshow(im)

# print(im)
# print(im.shape)

### ПЕРВОЕ ЗАДАНИЕ ###
height = im.shape[0]
width = im.shape[1]
size = height * width
print("1 answer: size = {}".format(size))

### ВТОРОЕ ЗАДАНИЕ ###
mean1 = round(im[:, :, 0].mean())
mean2 = round(im[:, :, 1].mean())
mean3 = round(im[:, :, 2].mean())
print("2 answer: mean = {}".format(mean3))

### ТРЕТЬЕ ЗАДАНИЕ ###
std1 = round(im[:, :, 0].std())
std2 = round(im[:, :, 1].std())
std3 = round(im[:, :, 2].std())
print("3 answer: std = {}".format(std1))

### ЧЕТВЕРТОЕ ЗАДАНИЕ ###
revers = im[:, :, ::-1]
res = revers[0, 345, 0]
print("4 answer: res = {}".format(res))

