def ComputeGrade(average):
    if average < 0 or average > 100:
        return 'Unrecognized marks/avg'
    elif 0 <= average <= 30:
        return 'D'
    elif 31 <= average <= 50:
        return 'C'
    elif 51 <= average <= 70:
        return 'B'
    elif 71 <= average <= 100:
        return 'A'


math = float(input("Enter Math marks: "))
physics = float(input("Enter Physics marks: "))
geo = float(input("Enter Geography marks: "))
chem = float(input("Enter Chemistry marks:"))

average = (math + physics + geo + chem) / 4

result = ComputeGrade(average)
print("Grade:", result)