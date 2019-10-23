import os
from PIL import Image

blockMap = [
    [(0, 0, 0), "black_concrete"],
    [(211, 211, 211), "light_gray_concrete"],
    [(128, 128, 128), "gray_concrete"],
    [(255, 255, 255), "white_concrete"],
    [(255, 105, 180), "pink_concrete"],
    [(255, 0, 0), "red_concrete"],
    [(255, 128, 0), "orange_concrete"],
    [(255, 255, 0), "yellow_concrete"],
    [(0, 255, 0), "lime_concrete"],
    [(58, 95, 11), "green_concrete"],
    [(0, 255, 255), "light_blue_concrete"],
    [(0, 0, 255), "blue_concrete"],
    [(102, 51, 153), "purple_concrete"],
    [(255, 0, 255), "magenta_concrete"],
    [(89, 60, 31), "brown_concrete"],
    [(0, 140, 132), "cyan_concrete"],
]

image = Image.open(input("File Name:    "))
width, height = image.size
sizeLimit = 64 # <=256

if width > sizeLimit or height > sizeLimit:
    image = image.resize((sizeLimit, sizeLimit))
    width, height = image.size

commands = []

print(image.getpixel((16, 16)))

def distance(pointA, pointB):
    out = 0
    for i in range(len(pointA)):
        if i < len(pointB):
            point = pointA[i]-pointB[i]
            out += max(-point, point)
    return(out)

def getBlock(colour):
    best = [(0, 0, 0), "air"]
    for block in blockMap:
        if distance(colour, block[0]) <= distance(colour, best[0]):
            best = block
    return(best[1])

def addPixel(x, y, colour):
    commands.append("setblock ~"+str(x)+" ~-1 ~"+str(y)+" "+getBlock(colour))

for x in range(width):
    for y in range(height):
        addPixel(x, y, image.getpixel((x, y)))

fileName = "image"
itemCount = 1
while os.path.exists(fileName+str(itemCount)+".mcfunction"):
    itemCount += 1
fileName += str(itemCount)

print("Saving to "+fileName+"...")
file = open(fileName+".mcfunction", 'w')
file.write('\n'.join(commands))
file.close()

input("Fin.")
