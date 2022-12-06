with open(r'login.txt') as f:
    lines = f.readlines()

testscriptmethod = 'null'
for line in lines:
    if line.__contains__("end"):
        break
    else:
        print(line)
    if line.__contains__("@"):
        testscriptmethod = line
    # if line.__contains__("open"):
    #     testscriptmethod = line
    # if line.__contains__("Enter"):
    #     testscriptmethod = line
    # if line.__contains__("click"):
    #     testscriptmethod = line
    


f.close()
print(testscriptmethod)
with open(r"login.py",'w', newline='') as file1:
    file1.write(testscriptmethod)
