# Write a program to demonstrate the use of valid and invalid Python identifiers.
name = "Ananya"
age = 20
student_name = "Python Student"

print(name)
print(age)
print(student_name)

print("Valid:", "student_name".isidentifier())
print("Invalid:", "123name".isidentifier())