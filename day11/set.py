
'''password = input("enter the password: ")
check=set()
if len (password)>=8:
    for i in password:
        if i.islower():
            check.add('l')
        if i.isupper():
             check.add('u')
        elif i.isdigit():
             check.add('n')
        else:
            check.add('s')

    if len(check)==4:
        print("strong password")

    else:
        print("weak password")
     else:
        print("weak password")
'''


data={
    student:{"name":sudheer,"status":True,"python":80,"java":77,"mysql":67},
    student:{"name":adhitya,"status":True,"python":80,"java":77,"mysql":67},
    student:{"name":ramesh,"status":False,"python":non,"java":non,"mysql":non},
    student:{"name":somya,"status":True,"python":99,"java":97,"mysql":95},
    student:{"name":sundar,"status":True,"python":60,"java":77,"mysql":67},
    }
name=input("enter the name:")
if name in data:
    if data[name]['status']:
        sum = data[name]['pyhton']+data[name]['java']+data[name]['mysql']
        avg = sum/3
        if avg>=90:
            print(f"you {name} got 1st in class")
        elif avg>=75:
            print(f"you{name} are 2nd in class")
        elif avg>=60:
            print(f"you{name} are 3nd in class")
        elif avg>=50:
            print(f"you{name} are 4nd in class")
        elif avg>=35:
            print(f"you{name} just passed")
        else:
            print(f"{name} you failed ")
        else:
            print("student nit founf:")
    
