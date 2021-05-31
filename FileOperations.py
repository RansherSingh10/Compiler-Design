n = 10
def add(num,marks):
    f = open("student.txt", "a")
    f.write(num + " " + marks +"\n")
    f.close()

def delete(num):
    f = open("student.txt", "r")
    txt = f.read()
    f.close()
    lines = txt.split('\n')
    lines = lines[0:len(lines)-1]
    n=-1
    for i in lines:
        n+=1
        i=i.split()
        if(i[0]==num):
            break
    del lines[n]
    txt=str("")
    for i in lines:
        txt+=i+"\n"
    f = open("student.txt", "w")
    f.write(txt)
    f.close()

def display():
    f = open("student.txt","r")
    txt = f.read()
    print(txt)

def update(num,marks):
    f = open("student.txt", "r")
    txt = f.read()
    f.close()
    lines = txt.split('\n')
    lines = lines[0:len(lines)-1]
    s = []
    for i in lines:
        j=i
        i=i.split()
        if(i[0]==num):
            s.append(num + " " +marks)
        else:
            s.append(j)
    txt=str("")
    for i in s:
        txt+=i+"\n"
    f = open("student.txt", "w")
    f.write(txt)
    f.close()

def calculate(num):
    f = open("student.txt","r")
    txt = f.read()
    f.close()
    lines = txt.split('\n')
    for i in lines:
        i=i.split()
        if(i[0]==num):
            avg = (int(i[1])+int(i[2])+int(i[3]))/3
            if(avg<50):
                print("FAIL")
            else:
                print("PASS")
            break

def exitFile():
    f = open("student.txt")
    f.close()

def operations():
    print("Choose one of the following operations: \n1. Add\n2. Delete\n3. Display\n4. Update\n5. Calculate\n6. Exit")
    t = int(input())

    if(t==1):
        num = input("Enter registration number: ")
        marks = input("Enter 3 subject marks: ")
        add(num, marks)
        operations()
           
    elif(t==2):
        num = input("Enter number to be deleted: ")
        delete(num)
        operations()

    elif(t==3):
        display()
        operations()

    elif(t==4):
        num = input("Enter registration number to be updated: ")
        marks = input("Enter 3 updated subject marks: ")
        update(num, marks)
        operations()

    elif(t==5):
        num = input("Enter number to calculate: ")
        calculate(num)

    elif(t==6):
        exitFile()

    else:
        print("Enter a Valid option!\n")
        operations()

operations()
