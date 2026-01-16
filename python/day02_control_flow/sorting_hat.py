gryffindor=0
ravenclaw=0
hufflepuff=0
slytherin=0

print('q1)Do you like dawn or dusk?\n\t 1) Dawn\n\t2) Dusk')

q1=int(input('Enter your choice:'))

if q1==1:
  gryffindor+=1
elif q1==2:
  hufflepuff+=1
else:
  print('Wrong Input')

print('q2) When I’m dead, I want people to remember me as:\n\t1) The Good\n\t2) The Great\n\t3) The Wise\n\t4) The Bold')

q2=int(input("Enter your choice:"))

if q2==1:
  hufflepuff+=2
elif q2==2:
  slytherin+=2
elif q2==3:
  ravenclaw+=2
elif q2==4:
  gryffindor+=2
else:
  print('Wrong input')

print('Q3) Which kind of instrument most pleases your ear?\n\t1) The violin\n\t2) The trumpet\n\t3) The piano\n\t4) The drum')

q3=int(input('Enter your choice:'))

if q3==1:
  hufflepuff+=4
elif q3==2:
  slytherin+=4
elif q3==3:
  ravenclaw+=4
elif q3==4:
  gryffindor+=4
else:
  print('Wrong input')

print("Final scores:\n")
print("Gryffindor",gryffindor)
print("Ravenclaw",ravenclaw)
print("Hufflepuff",hufflepuff)
print("Slytherin",slytherin)
