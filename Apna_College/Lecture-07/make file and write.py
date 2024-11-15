with open("practice.txt","w") as f:
    f.write("Hi everyone\n")
    f.write("We are learning File I/O\n")
    f.write("Using Java\n")
    f.write("I like programming in Java")
with open("practice.txt","r") as f:
    data=f.read()
    print(data)