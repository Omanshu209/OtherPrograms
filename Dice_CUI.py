#importing required modules
import random

#title
print("\033[1;32m*********************\n  Dice Simulator!\n**********************\n")

#taking input
type=int(input("Select The Type Of Dice You Want To Roll----\n\n1)Normal Dice(Equal Chances For Getting Each Number)\n2)Dice-Type A(High Chances Of Getting Numbers >3)\n3)Dice-Type C(High Chances Of Getting Numbers<=3)\n\nEnter Only A Number(1/2/3)::  "))
print('********************\n')

#dice
if type==1:
	while True:
		numberA=random.randint(1,6)
		print('Number:: '+str(numberA))
		retry=input('Do You Want To Roll The Dice Again?(Y/N):: ')
		if retry=='N':
			print('\n********************\n')
			break
		elif retry=='Y':
			print('\n********************\n')
			continue
		else:
			print('INVALID INPUT')
			print('\n********************\n')
			break
			
elif type==2:
		while True:
			chances=(1,2,3,4,4,4,4,5,5,5,6,6)
			randomA=random.randint(0,11)
			numberB=chances[randomA]
			print('Number:: '+ str(numberB))
			retry=input('Do You Want To Roll The Dice Again?(Y/N):: ')
			if retry=='N':
			    print('\n********************\n')
			    break
			elif retry=='Y':
			     print('\n********************\n')
			     continue
			else:
			    print('INVALID INPUT')
			    print('\n********************\n')
			    break
			
elif type==3:
		while True:
			chancesB=(1,1,1,1,2,2,2,3,3,4,5,6)
			randomB=random.randint(0,11)
			numberC=chancesB[randomB]
			print('Number:: '+str(numberC))
			retry=input('Do You Want To Roll The Dice Again?(Y/N):: ')
			if retry=='N':
				print('\n********************\n')
				break
			elif retry=='Y':
				print('\n********************\n')
				continue
			else:
				print('INVALID INPUT')
				print('\n********************\n')
				break
				
else:
	print('INVALID INPUT')
	
#printing developer's name(my name)
print('\n********************\n#MADE BY OMANSHU#\n********************\n')

#thank you
