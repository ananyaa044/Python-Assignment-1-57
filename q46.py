#46. Write a program to accept five subject marks from the user and display their total.
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total_marks = sum(marks)
print("Total marks:", total_marks)
