def yes_no(data):
    return (bool(data.find("learning")))
with open("practice.txt","r") as f:
    data=f.read()
    boll=yes_no(data)
    if(boll):
        print("Learning has been found the file")
    else:
        print("Not Found")