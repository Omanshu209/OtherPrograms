import re
print("**********************")
p_no = input("Enter A Phone Number To Validate:: ")
print("**********************")
format = r"^[1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$"
if re.match(format,p_no):
	print("Valid Phone Number")	
else:
	print("Invalid Phone Number")
print("**********************\nMade By Omanshu\n**********************")
