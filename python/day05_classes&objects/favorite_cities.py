class City:
  def __init__(self,name,country,population,landmarks):
    self.name=name
    self.country=country
    self.population=population
    self.landmarks=landmarks
bangalore=City('Bangalore','India',840000,['Vidhan Soudha','UB City'])
paris=City('Paris','France',40000,['Eiffel Tower','Restaurant'])
newyork=City('New York','USA',1000000,['Empire State Building','Central Park'])
london=City('London','UK',90000,['London Bridge','Bullet Building'])
class City_to_visit:
  def __init__(self,name,country,population,landmarks):
    self.name=name
    self.country=country
    self.population=population
    self.landmarks=landmarks
dubai=City_to_visit('Dubai','UAE',6000000,['Burj Khalifa','Palm Jumeira'])
siwa=City_to_visit('Siwa','Egypt',5000000,['Siwa Oasis','Library'])
print(vars(bangalore))
print(vars(paris))
print(vars(newyork))
print(vars(london))
print(vars(dubai))
print(vars(siwa))
