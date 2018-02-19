def intCheck(mes):
  while True:
    try:
       Input = int(input(mes))       
    except ValueError:
       print("I said an integer between 0 and 1000000.")
       continue
    else:
       return Input 
       break


aker = (intCheck("Gimme an integer between 0 and 1000000:\n"))	
if (aker<=1000000 and aker>0):
	latin=""
	while (aker!=0):
		if (aker>=1000):
			v=1000
			latin+="M"
		elif (aker>=900):
			v=900
			latin+="CM"
		elif (aker>=500):
			v=500
			latin+="D"
		elif (aker>=400):
			v=400
			latin+="CD"
		elif (aker>=100):
			v=100
			latin+="C"
		elif (aker>=90):
			v=90
			latin+="XC"
		elif (aker>=50):
			v=50
			latin+="L"
		elif (aker>=40):
			v=40
			latin+="XL"
		elif (aker>=10):
			v=10
			latin+="X"
		elif (aker>=9):
			v=9
			latin+="IX"
		elif (aker>=5):
			v=5
			latin+="V"
		elif (aker>=4):
			v=4
			latin+="IV"
		else:
			v=1
			latin+="I"
		aker=aker-v
print (latin)




