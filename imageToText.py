from PIL import Image, ImageOps
rgb_values = {(0, 0, 0):'#',(1, 0, 0):'@',
(0, 1, 0):'%',(0, 0, 1):'&', 
(1, 1, 0):'$',(1, 0, 1):'+',
(0, 1, 1):'4',(1, 1, 1):' '}
while True:
    try:
        directory=input("Enter image directory: ")
        img = Image.open(directory)
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
height = int(img.size[1]*percent)
img = img.resize((width, height), Image.Resampling.LANCZOS)
pix = img.load()
f = open(directory[::-1][directory[::-1].find('.'):directory[::-1].find('\\')][::-1] + "txt", "w")
for y in range(0, img.size[1]):
    for x in range(0, img.size[0]):
        f.write(rgb_values[tuple(round(value/255) for value in pix[x,y])])
    f.write("\n")
f.close()