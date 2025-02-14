#1 i scored 8.5

#2 continue skips current iteration of a loop and proceeds next, while break stops entirely.

#3 for "for" range is given. for while not

#4for i in range(2): 
    for j in range(2):  
        print(i, j)


#1
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
f_list = []
for items in list1:
    if items not in list2:
        f_list.append(items)
for item in list2:
    if item not in list1:
        f_list.append(item)

print(f_list)


#2
n = int(input())
for i in range(1, n):
    print(i*i)


#3
text = input("Enter the string:")
yangi = ""
harf = ["a", "e", "u", "i", "o"]
i = 0
count = 0
while i<(len(text) - 1):
    yangi += text[i]
    count+=1
    if count >= 3:
        if text[i] not in harf:
            yangi+="_"
            harf.append(text[i])
            count = 0
        
    i+=1
yangi+=text[-1]

print(yangi)

#4
import random
a = random.randint(1, 100)
n = int(input("Enter number: "))

attempts = 1
while attempts<=10:
    if n>a:
        n = int(input("Too high:  "))
        attempts+=1
        if attempts == 10:
            respond = input("You've lost. Want to play again? ")
            if respond in ['Y', 'YES', 'y', 'yes', 'ok']:
                attempts = 1
                a = random.randint(1, 100)
                n = int(input("Enter  number:"))
    elif n<a:
        n = int(input("Too low: "))
        attempts+=1
        if attempts == 10:
            respond = input("You've lost. Want to play again?  ")
            if respond in ['Y', 'YES', 'y', 'yes', 'ok']:
                attempts = 1
                a = random.randint(1, 100)
                n = int(input("Enter number:"))
    else:
        print("You guessed it right!")
        break

#5
password = input("Enter the password:  ")
if len(password)<8:
    print("Password is too short ")
if password.lower() == password:
    print("Password must contain an uppercase letter.")
if len(password)>8 and password.lower() != password:
    print("Password is strong. ")

#6
primes = list(range(2, 101))
print(primes)
for i in range(1, 101):
  for j in range(2, i-1):
       if i%j == 0:
          primes.remove(i)
          break

print(primes)
