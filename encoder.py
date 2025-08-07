from PIL import Image
import math
print("Enter text you'd like to encode")
input = input()
b = ''.join(format(ord(char), '08b') for char in input)
print(b)
chunks = [b[i:i + 3] for i in range(0, len(b), 3)]
if(len(chunks[len(chunks)-1]) < 3): 
    chunks[len(chunks)-1] += '0' * (3 - len(chunks[len(chunks)-1]))
size = math.ceil(len(chunks) ** 0.5)
if size != len(chunks) ** 0.5:
    for i in range(size ** 2 - len(chunks)):
        chunks.append('000')
img = Image.new('RGB', (size, size), color=(0, 0, 0))
for i in range(size):
    for j in range(size):
        index = i * size + j
        img.putpixel((j, i), ((int(chunks[index][0])*255), (int(chunks[index][1])*255), (int(chunks[index][2])*255)))
img.save('output.png')
print("Image saved as output.png")