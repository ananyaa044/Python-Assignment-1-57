#10. Write a program to swap two variables without using a temporary variable.
a = 5
b = 10
print("Before swapping:")
print("Value of a:", a)
print("Value of b:", b)

# Swapping without using a temporary variable
a = a + b
b = a - b
a = a - b

print("After swapping:")
print("Value of a:", a)
print("Value of b:", b)
