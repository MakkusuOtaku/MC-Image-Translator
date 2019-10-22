from PIL import Image

blockMap = [
    [(0, 0, 0), "black_concrete"],
    [(255, 255, 255), "white_concrete"],
    [(255, 0, 0), "red_concrete"],
    [(0, 255, 0), "lime_concrete"],
    [(0, 255, 255), "yellow_concrete"],
    [(0, 0, 255), "blue_concrete"],
    [(255, 0, 255), "magenta_concrete"],
]

image = Image.open(input("File Name:    "))
width, height = image.size
sizeLimit = 32 #!!<=256!!#

if width > sizeLimit or height > sizeLimit:
    image.resize((sizeLimit, sizeLimit))

commands = []

def distance(pointA, pointB):
    out = 0
    for i in range(len(pointA)):
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
    commands.append("setblock ~"+str(x)+" ~5 ~"+str(y)+" "+getBlock(colour))

for x in range(width):
    for y in range(height):
        addPixel(x, y, image.getpixel((x, y)))

file = open("lastimage.mcfunction", 'w')
file.write('\n'.join(commands))
file.close()

input("Fin.")
