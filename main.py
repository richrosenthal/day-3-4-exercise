# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0
if(size == 'S'):
  if(add_pepperoni == 'Y'):
    total += 2 
  if(extra_cheese == 'Y'):
    total += 1 
  total += 15
  print("Your pizza is $" + str(total))
elif(size == 'M'):
    if(add_pepperoni == 'Y'):
      total += 3 
    if(extra_cheese == 'Y'):
      total += 1 
    total += 20
    print("Your pizza is $" + str(total))
elif(size == 'L'):
  if(add_pepperoni == 'Y'):
    total += 3 
  if(extra_cheese == 'Y'):
    total += 1 
  total += 25 
  print("Your pizza is $" + str(total))




  




