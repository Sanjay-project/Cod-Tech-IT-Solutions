from string import ascii_letters,digits,punctuation
import random
temp_password=[]
letters=int(input("how many leters do you want:"))
numbers=int(input("how many integers do you want:"))
symbols=int(input("how many symbols do you want:"))
for i in range(letters):
       temp_password+=random.choice(ascii_letters)
for i in range(numbers):
       temp_password+=random.choice(digits)
for i in range(symbols):
       temp_password+=random.choice(punctuation)       
random.shuffle(temp_password)       
final_password=''.join(temp_password)
print "Here is the Generated Password:",final_password