def pon(p):
  if p==0:
    return("Zero")
  elif p<0:
    return("Negative")
  else:
    return("Positive")
p=int(input())
print(pon(p))
