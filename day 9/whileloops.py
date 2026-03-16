''''
i = 20
while i <=30:
   if i == 25:
         pass
   print(i)
   i+=1
'''
'''
bullets = 6
while bullets > 0:
    print(f'{bullets} bullets are left, you can shoot!')
    bullets-=1
else:
        print('game over')
'''
'''
moves = 32
winning_point = 16
while moves > 0:
    if moves == winning_point:
        print("you win the game")
        break
    print(f'{moves} moves are left, you can play')
    moves-=1
else:
    print("game over")
'''
'''
students = {}
n = int(input("enter the no of students:"))
for i in range (n):
    name = input("enter the name:")
    students[name]=False
    print(students)
'''
students = {}
n = int(input("enter the no of students:"))
for i in range (n):
    name = input("enter the name:")
    students[name]=False
for name in students:
    status = int(input(f"(enter the {name} status(0-absent,1-present): "))
    students[name]=bool(status)
print(students)
