#MADE BY OMANSHU

#importing required modules
import random

#introduction
a=input("Enter Your Name:: ")
print("Hello, "+a+"\nIm Omanshu, the developer of this game..........\nWelcome to Digital Fight! This is a turn-based fighting game where you choose a character and fight with the computer.\nThere are 3 characters to choose from each with different health , attack and damage. The damage ranges with each attack and they all have varying accuracy rates.\nEnjoy!")

#title
print("\033[1;32m=======================================")
print("          Digital Fight!")
print("=======================================")

#selection of character
print("")
print("Choose your fighter!")
print("")
print("Fat Man                      Hacker                    Little Boy             Prototype")
print("")
print("Hp-400                       Hp-300                    Hp-200                 Hp-150")
print("A (10-30     50%)            A (15-30   90%)           B (20-25 100%)         A(1-50 75%)")
print("C (65-100   20%)             B (25-75  33%)            C (45-60 60%)          B(1-100 40%)")
print("")

#taking input and adjusting the level of difficulty
print("********************")
character=input("Character:: ")
print('[NOTE: If Level Of DIfficulty Is Not Selected Then The Default Value Of Computer\'s Hp(100) Will Be Taken] ')
hardness=input("Select The Level Of Difficulty(1/2/3/4/5/6/7/8/9):: ")
if hardness=='1':
	computer_hp=100
elif hardness=='2':
	computer_hp=150
elif hardness=='3':
	computer_hp=200
elif hardness=='4':
	computer_hp=250
elif hardness=='5':
	computer_hp=300
elif hardness=='6':
	computer_hp=350
elif hardness=='7':
	computer_hp=400
elif hardness=='8':
	computer_hp=450
elif hardness=='9':
	computer_hp=500
else:
	computer_hp=100
if character!='Fat Man' and character!='Hacker' and character!='Little Boy' and character!='Prototype':
	print('INVALID INPUT(Character)')
print('********************\n\n\n')

#main gameplay
fatman_hp=400
hacker_hp=300
littleboy_hp=200
prototype_hp=150
fatmanA_acc=("hit","miss")
fatmanC_acc=("miss","hit","miss","miss","miss","miss")
hackerA_acc=("hit","hit","hit","hit","hit","hit","hit","hit","hit","miss")
hackerB_acc=("hit","miss","miss")
lboyB_acc=("hit","hit")
lboyC_acc=("hit","hit","hit",'miss','miss')
ptA_acc=("hit","miss","hit","hit")
ptB_acc=("miss","hit","miss","hit","miss")

if character=="Fat Man":
	while True:
	    FMA=random.randint(0,1)
	    FMAM=fatmanA_acc[FMA]
	    CDA=random.randint(10,30)
	    FMC=random.randint(0,4)
	    FMCM=fatmanC_acc[FMC]
	    CDC=random.randint(65,100)
	    CA=random.randint(5,50)
	    idk=random.randint(0,9)
	    computer_acc=("hit","hit","hit","hit","hit","hit","hit","hit","hit","miss")
	    iddk=computer_acc[idk]
	    print("A (10-30     50%)\nC (65-100   20%)\n********************")
	    print("YOUR HP: "+str(fatman_hp)+'!')
	    print("COMPUTER'S HP: "+str(computer_hp)+"!\n********************")
	    print("")
	    attackfm=input("Choose Your Attack(A/C): ")
	    print("")
	    if attackfm=='A' and FMAM=='hit':
		    print('\n\n\nHIT!')
		    computer_hp-=CDA
	    if attackfm=='C' and FMCM=='hit':
	    	print('\n\n\nHIT!')
	    	computer_hp-=CDC
	    if attackfm=='A' and FMAM=='miss':
	    	print('\n\n\nMISS!')
	    if attackfm=='C' and FMCM=='miss':
		    print('\n\n\nMISS!')
	    if iddk=='hit':
	    	print('Computer: HIT!')
	    	fatman_hp-=CA
	    if iddk=='miss':
    		print('Computer: MISS!')
	    if computer_hp<=0:
		    break
	    if fatman_hp<=0:
		    break

if character=='Hacker':
	while True:
	    HKA=random.randint(0,9)
	    HKAM=hackerA_acc[HKA]
	    AAA=random.randint(15,30)
	    HKB=random.randint(0,2)
	    HKBM=hackerB_acc[HKB]
	    AAB=random.randint(25,75)
	    CA=random.randint(5,50)
	    idk=random.randint(0,9)
	    computer_acc=("hit","hit","hit","hit","hit","hit","hit","hit","hit","miss")
	    iddk=computer_acc[idk]
	    print("A (15-30   90%)\nB (25-75  33%)\n********************")
	    print("YOUR HP: "+str(hacker_hp)+'!')
	    print("COMPUTER'S HP: "+str(computer_hp)+"!\n********************")
	    print("")
	    attackhk=input("Choose Your Attack(A/B): ")
	    print("")
	    if attackhk=='A' and HKAM=='hit':
	    	print("\n\n\nHIT!")
	    	computer_hp-=AAA
	    if attackhk=='B' and HKBM=='hit':
	    	print('\n\n\nHIT!')
	    	computer_hp-=AAB
	    if attackhk=='A' and HKAM=='miss':
	    	print("\n\n\nMISS!")
	    if attackhk=='B' and HKBM=='miss':
	    	print("\n\n\nMISS!")
	    if iddk=='hit':
	    	print('Computer: HIT!')
	    	hacker_hp-=CA
	    if iddk=='miss':
    		print('Computer: MISS!')
	    if computer_hp<=0:
		    break
	    if hacker_hp<=0:
		    break
		    
if character=='Little Boy':
	while True:
	    LBB=random.randint(0,1)
	    LBBM=lboyB_acc[LBB]
	    BBB=random.randint(20,25)
	    LBC=random.randint(0,4)
	    LBCM=lboyC_acc[LBC]
	    BBC=random.randint(45,60)
	    CA=random.randint(5,50)
	    idk=random.randint(0,9)
	    computer_acc=("hit","hit","hit","hit","hit","hit","hit","hit","hit","miss")
	    iddk=computer_acc[idk]
	    print("B (20-25 100%)\nC (45-60 60%)\n********************")
	    print("YOUR HP: "+str(littleboy_hp)+'!')
	    print("COMPUTER'S HP: "+str(computer_hp)+"!\n********************")
	    print("")
	    attacklb=input("Choose Your Attack(B/C): ")
	    print("")
	    if attacklb=='B' and LBBM=='hit':
	    	print("\n\n\nHIT!")
	    	computer_hp-=BBB
	    if attacklb=='C' and LBCM=='hit':
	    	print("\n\n\nHIT!")
	    	computer_hp-=BBC
	    if attacklb=='B' and LBBM=='miss':
	    	print("\n\n\nMISS!")
	    if attacklb=='C' and LBCM=='miss':
	    	print("\n\n\nMISS!")
	    if iddk=='hit':
	    	print('Computer: HIT!')
	    	littleboy_hp-=CA
	    if iddk=='miss':
    		print('Computer: MISS!')
	    if computer_hp<=0:
		    break
	    if littleboy_hp<=0:
		    break
		    
if character=="Prototype":
	while True:
	    PTA=random.randint(0,3)
	    PTAM=ptA_acc[PTA]
	    CCA=random.randint(1,50)
	    PTB=random.randint(0,4)
	    PTBM=ptB_acc[PTB]
	    CCB=random.randint(1,100)
	    CA=random.randint(5,50)
	    idk=random.randint(0,9)
	    computer_acc=("hit","hit","hit","hit","hit","hit","hit","hit","hit","miss")
	    iddk=computer_acc[idk]
	    print("A(1-50 75%)\nB(1-100 40%)\n********************")
	    print("YOUR HP: "+str(prototype_hp)+'!')
	    print("COMPUTER'S HP: "+str(computer_hp)+"!\n********************")
	    print("")
	    attackpt=input("Choose Your Attack(A/B): ")
	    print("")
	    if attackpt=="A" and PTAM=='hit':
	    	print("\n\n\nHIT!")
	    	computer_hp-=CCA
	    if attackpt=="B" and PTBM=='hit':
	    	print("\n\n\nHIT!")
	    	computer_hp-=CCB
	    if attackpt=='A' and PTAM=="miss":
	    	print("\n\n\nMISS!")
	    if attackpt=='B' and PTBM=='miss':
	    	print('\n\n\nMISS!')
	    if iddk=="hit":
	    	print('Computer: HIT!')
	    	prototype_hp-=CA
	    if iddk=='miss':
	    	print('Computer: MISS!')
	    if computer_hp<=0:
	    	break
	    if prototype_hp<=0:
	    	break
	    	
if fatman_hp<=0:
	print('\n\nYOU LOSE !\n\n')
if hacker_hp<=0:
    print("\n\nYOU LOSE!\n\n")
if littleboy_hp<=0:
	print("\n\nYOU LOSE!\n\n")
if prototype_hp<=0:
	print("\n\nYOU LOSE!\n\n")
if computer_hp<=0:
	print('\n\nYOU WON !\n\n')
	
#printing the developer's name(my name)'
print("\n******************************\n     #Made By Omanshu#\n******************************")

#thank you
