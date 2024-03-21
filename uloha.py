from PIL import Image
from PIL import ImageColor


def drticka(row: str):
    groups = []
    row = row.strip()
    for i in range(0, len(row), 6):
        group = row[i : i + 6]
        groups.append(group)
    return groups


input_file = open("result.txt", "r", encoding="UTF-8")

first_line = input_file.readline().strip().split(" ")

height = int(first_line[1])
width = int(first_line[0])

img = Image.new("RGB", (width, height), color="white")

pixels = img.load()

y = 0

for row in input_file:
    x = 0
    temp = drticka(row)
    for i in range(len(temp)):
        hexa = "#" + temp[i]
        colour = ImageColor.getcolor(hexa, "RGB")
        pixels[x, y] = (colour[0], colour[1], colour[2])
        x+=1
    y += 1

img.show()