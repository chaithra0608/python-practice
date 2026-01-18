import random
def fortune():
  num=random.randint(0,7)
  if num==0:
    print('Dont pursue happiness – create it.')
  elif num==1:
    print('All things are difficult before they are easy.')
  elif num==2:
    print('The early bird gets the worm, but the second mouse gets the cheese.')
  elif num==3:
    print('Someone in your life needs a letter from you.')
  elif num==4:
    print('Dont just think. Act!')
  elif num==5:
    print('Your heart will skip a beat.')
  elif num==6:
    print('The fortune you search for is in another cookie.')
  else:
    print('Help! I am being held prisoner in a Chinese bakery!')
fortune()
fortune()
fortune()
