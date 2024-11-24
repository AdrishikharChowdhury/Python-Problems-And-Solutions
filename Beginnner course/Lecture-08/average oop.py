class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for i in marks:
            sum+=i
        return sum/len(marks)
j=0
info={}
count=int(input("Enter the no. of information of students you want to enter: "))
while j<count:
    name=input("Enter the student name: ")
    marks=[]
    n=int(input("Enter the no. of subjects: "))
    for i in range(0,n):
        marks.append(float(input("Enter the marks: ")))
    s1=Student(name,marks)
    avg=s1.average()
    print("The average marks of ",s1.name," is ",avg)
    info.update({s1.name:avg})
    j+=1
print(info)