for i in range(0, 3):
   arr = list(map(int, input().split()));
   countBae = 0
   for i in range(len(arr)):
      if arr[i] == 0 :
         countBae += 1
   
   if countBae == 1:
      print('A')
   elif countBae == 2:
      print('B')
   elif countBae == 3:
      print('C')
   elif countBae == 4:
      print('D')
   else:
      print('E')