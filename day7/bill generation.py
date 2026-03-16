''''
products=['rice','wheat floor','sugar','milk','eggs 12(pcs)','cooking oil','tea powder','salt','bread','soap']
prices=[60,30,20,40,50,80,90,99,45,67]

print("-------welcome to grocery store------")
print("here are the available products:\n")
print('index'.ljust(6,' '),'products'.ljust(15,' ')'price'.ljust(6,' '))
for i in range(10):
    print(str(i+1).ljust(6,' '),product[i].ljust(6,' '),str(prices[i]).ljust(6,' '))
'''
'''
def wish(name):
    print(f'hello{name},welcome to "pyhton 100 days program"')
wish("sudheer")
wish("ram")
wish("rahul")
'''
'''
def display(username,email,password):
    print("username:",username)
    print("email:", email)
    print("password:", password)

display(username = 'sudheer',email = "sudheer@gmail.com", password= "s@123")
display(username = 'sudheer@gmail.com',email = "sudheer", password= "s@123")
display(username = 's@123',email = "sudheer", password= "s@123")
'''
'''
def display(username,email,password,phoneno='+91'):
    print("username:",username)
    print("email:", email)
    print("password:", password)
    print("phoneno:",phoneno)

display(username = 'sudheer',email = "sudheer@gmail.com", password= "s@123")
display(username = 'sudheer@gmail.com',email = "sudheer", password= "s@123")
display(username = 's@123',email = "sudheer", password= "s@123")


def display(*names):
    print(names)
display("sudheer","adhitya","suresh ")
display("sudheer","adhitya")
display("sudheer",)
'''



products=['rice','wheat floor','sugar','milk','eggs 12(pcs)','cooking oil','tea powder','salt','bread','soap']
prices=[60,30,20,40,50,80,90,99,45,67]

print("-------welcome to grocery store------")
print("here are the available products:\n")
print('index'.ljust(6,' '),'products'.ljust(15,' ')'price'.ljust(6,' '))
for i in range(10):
    print(str(i+1).ljust(6,' '),product[i].ljust(6,' '),str(prices[i]).ljust(6,' '))

items = list(map(int,input("enter the indexes: ").split()))

print("selected items: ")
total_amount = 0
for item in items:
    print(products[item-1],prices[item-1])
    total_amount==prices[item-1]
