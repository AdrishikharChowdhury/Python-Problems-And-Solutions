def replacer(data):
    new_data=data.replace("Java","Python")
    return new_data
with open("practice.txt","r") as f:
    data=f.read()
    new_data=replacer(data)
with open("practice.txt","w") as f:
    f.write(new_data)
with open("practice.txt","r") as f:
    print(f.read())
