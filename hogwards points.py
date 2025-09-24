g=0
r=0
h=0
s=0
print('''Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk''')
a=int(input('Do you like Dawn or Dusk?:'))
if a==1:
  g+=1
  r+=1
  print('gryffindor=',g, 'and ravenclaw=',r)
elif a==2:
  h+=1
  s+=1
  print('hufflepuff=',h,' and slytherin=',s)
else:
  print('wrong input')

print('''Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold''')
b=int(input('When I’m dead, I want people to remember me as:'))
if b==1:
  h+=2
  print('hufflepuff=',h)
elif b==2:
  s+=2
  print('slytherin=',s)
elif b==3:
  r+=2
  print('ravenclaw',r)
elif b==4:
  g+=2
  print('gryffindor=',g)
else:
  print('wrong output')

print('''Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum''')
c=int(input('Which kind of instrument most pleases your ear?:'))
if c==1:
  s+=4
  print('slythrin=',s)
elif c==2:
  h+=4
  print('hufflepuff=',h)
elif c==3:
  r+=4
  print('ravenclaw=',r)
elif c==4:
  g+=4
  print('gryffindor=',g)
else:
  print('wrong output')
print("Scores are:")
print("Gryffindor =", g)
print("Hufflepuff =", h)
print("Ravenclaw  =", r)
print("Slytherin  =", s)
