def yes_no(word):
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                return line_no
            else:
                line_no+=1
    return -1
word=(input("Enter the word to find: "))
boll=yes_no(word)
if(boll!=-1):
    print(word,"has been found the file on line no.",boll)
else:
    print("Not Found")