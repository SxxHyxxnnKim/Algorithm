word = input().lower()
wlist = list(set(word))
chk =[]

for i in wlist:
   count =word.count(i)
   chk.append(count)

if chk.count(max(chk)) >= 2:
   print('?')
else:
   print(wlist[(chk.index(max(chk)))].upper())
