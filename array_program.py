name_input = input("Enter your last name: ").upper()

size = len(name_input)
name = [None] * size

for index in range(size):
    name[index] = name_input[index]

i = 0
print("Output:", end=" ")
while i < size:
    print(name[i], end=" ")
    i += 1
print()
