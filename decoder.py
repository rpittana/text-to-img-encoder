from PIL import Image

# Input
print("Enter name of the image file to decode")
input_file = input()
img = Image.open(input_file)
img = img.resize((img.width // 86, img.height // 86), Image.NEAREST)  # Resize to original size
# Extract binary data from the image
data = ''
pixels = list(img.getdata())
for i in range(len(pixels)):
    for j in range(3):
        data += str(int(pixels[i][j] / 255))
chunks = [data[i:i+8] for i in range(0, len(data), 8)]  # Split into chunks of 8 bits
for i in range(len(chunks) - 1, -1, -1):
    if len(chunks[i]) < 8 or chunks[i] == '00000000':
        del chunks[i] # Remove incomplete or padded chunks
#print(chunks)

# Convert binary chunks back to text
decoded_text = ''.join([chr(int(chunk, 2)) for chunk in chunks])  # Convert binary to text
print(decoded_text)