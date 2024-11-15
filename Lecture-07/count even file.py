def even_counter():
    i=0
    with open(r"C:\Users\amiad\OneDrive\Desktop\programming\Python\Lecture-07\numbers.txt","r") as f:
        data=f.read()
        nums=data.split(",")
        for val in nums:
            if(int(val)%2==0):
                i+=1
    return i
counter=even_counter()
if counter==0:
    print("No even number in the file")
else:
    print("No. of even numbers =",counter)