n = input().split()
num = list(map(str,str(n[0])))
count = 0
even = []
odd = []
indexOdd = []
indexEven = []
for val in num:
    #Counting Special Character
    if not val.isdigit():
        count += 1
    else:
        if int(val)%2 == 0:
            even.append(val)
        else:
            odd.append(val)

print(even)
print(odd)
        
if count%2 != 0:
  res = [i + j for i, j in zip(odd, even)]
  print(''.join(res))

        


    
    
    
