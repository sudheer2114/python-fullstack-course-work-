data={
    student:{"name":sudheer,"status":True,"python":80,"java":77,"mysql":67},
    student:{"name":adhitya,"status":True,"python":80,"java":77,"mysql":67},
    student:{"name":ramesh,"status":False,"python":non,"java":non,"mysql":non},
    student:{"name":somya,"status":True,"python":99,"java":97,"mysql":95},
    student:{"name":sundar,"status":True,"python":60,"java":77,"mysql":67},
    }
name=input("enter the name:")
if student in data:
    if data[student]['name']:
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
    
