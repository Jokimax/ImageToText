from PIL import Image
rgb_values = {(0, 0, 0):'#',(1, 0, 0):'&',
(0, 1, 0):'%',(0, 0, 1):'@',(1, 1, 0):'"',(1, 0, 1):',',(0, 1, 1):'.',(1, 1, 1):' '}
while True:
    try:
        img = Image.open(input("Enter image directory: "))
        break
    except:
        print("Directory doesn't exist!")
img = img.convert('RGB')
while True:
    try:
        width=int(input("Input desired output width: "))
        percent = width/img.size[0]
        break
    except:
        print("Please enter a valid number!")
while True:
    try:
        directory=input("Output file name: ")
        break
    except:
        print("An error occured please try again!")
while True:
    try:
        f = open(input("Output file name: ") + ".txt", "w")
        break
    except:
        print("An error occured please try again!")
height = int(img.size[1]*percent/2)
img = img.resize((width, height), Image.Resampling.LANCZOS)
pix = img.load()
for y in range(0, img.size[1]):
    for x in range(0, img.size[0]):
        f.write(rgb_values[tuple(round(value/255) for value in pix[x,y])])
    f.write("\n")
f.close()