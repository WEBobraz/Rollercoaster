print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
  print('You can ride the rollercoaster!')
  age = int(input('How old are you? '))
  if age < 12:
    print('Your ticket coast $5')
  elif age <= 18:
    print('Your ticket coast $12')
  else:
    print('Your ticket coast $18')
else:
  print('Sorry, you have to grow taller before you can ride.')
