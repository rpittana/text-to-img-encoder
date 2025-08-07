print("Enter text you'd like to encode")
input = input()
b = ''.join(format(ord(char), '08b') for char in input)
print(b)
chunks = [b[i:i + 3] for i in range(0, len(b), 3)]
print(chunks)