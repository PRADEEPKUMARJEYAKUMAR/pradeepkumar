import string
p=input()
p.lower()
a=['a','e','i','o','u']
b="qwertyuioplkjhgfdsazxcvbnm"
if p in a:
  print("Vowel")
elif p in b:
  print("Consonant")
else:
  print("Invalid")
