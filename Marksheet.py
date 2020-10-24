print("Welcome to the Marksheet")

print("Enter maths Marks: ", end=" ")
m = int(input())

print("Enter Java Marks: " ,end=" ")
j = int(input())

print("Enter C# Marks: ", end=" ")
c = int(input())

print("Enter Ps Marks: ", end=" ")
p = int(input())

print("Enter DS Marks: ", end=" ")
d = int(input())

if m > 100:
    print("Please Enter a marks Less than Hundred")
elif m>=80:
    print("A Grade in Math")
elif m>=60:
    print("B Grade Math")
elif m>=50:
    print("C Grade Math")
elif m>=40:
    print("D Grade Math")
else:
    print("You Are Fail in Math...")

if j>100:
    print("Pleae Enter a Marks less than Hundred")
elif j >= 80:
    print("A Grade in Java")
elif j >= 60:
    print("B Grade in Java")
elif j >= 50:
    print("C Grade in Java")
elif j >= 40:
    print("D Grade in Java")
else:
    print("You Are Fail in Java...")

if c>100:
    print("Pleae Enter a Marks less than Hundred")
elif c>= 80:
    print("A Grade in C++")
elif c>= 60:
    print("B Grade in C++")
elif c>= 50:
    print("C Grade in C++")
elif c>= 40:
    print("D Grade in C++")
else:
    print("You Are Fail in C++...")

if p>100:
    print("Pleae Enter a Marks less than Hundred")
elif p>= 80:
    print("A Grade in Pak Study")
elif p>= 60:
    print("B Grade in Pak Study")
elif p>= 50:
    print("C Grade in Pak Study")
elif p>= 40:
    print("D Grade in Pak Study")
else:
    print("You Are Fail in Pak Study...")

if d>100:
    print("Pleae Enter a Marks less than Hundred")
elif d>= 80:
    print("A Grade in Structure")
elif d>= 60:
    print("B Grade in Structure")
elif d>= 50:
    print("C Grade in Structure")
elif d>= 40:
    print("D Grade in Structure")
else:
    print("You Are Fail in Data Structure...")

tm = m+j+c+p+d
print("Marks Obtained", tm, "Out of 500")

per = tm/500*100
print(per, "%")