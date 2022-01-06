with open("artifacts01.txt","r") as f:
    text=f.read()

with open("artifacts02.txt","a") as f:
    f.write(text +" appended ")
print("In stage2 appened file")
