height=int(input('What is your height? (in cm)'))
credits=int(input('How many credits do you have?'))
print(height)
print(credits)
if height>=137 and credits>=10:
  print('Enjoy the ride!')
elif height<137 and credits>=10:
  print('You are not tall enough to ride.')
elif height>=137 and credits<10:
  print('You dont have enough credits.')
else:
  print('You dont meet the requirements')
