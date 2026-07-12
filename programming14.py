text = input("Enter a string: ")
count = 0

for ch in text:
    if ch.isupper():
        count += 1

print("Uppercase Letters =", count)

# Output:
# Enter a string: PyTHon
# Uppercase Letters = 3
