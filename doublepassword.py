password1 = input()
password2 = input()
counter = 0
for i in range(4):
    if password1[i] != password2[i]:
        counter+= 1
print(str(pow(2,counter)))
#for one in range(0,9):
 #   for two in range(0,9):
  #      for three in range(0,9):
   #         for four in range(0,9):
    #            if one == int(password1[0]) or one== int(password2[0]):
     #               if two == int(password1[1]) or two == int(password2[1]):
      #                  if three == int(password1[2]) or three == int(password2[2]):
       #                     if four == int(password1[3]) or four == int(password2[3]):
        #                        counter += 1