import random
mr=[random.randrange(-30,30) for i in range (30)]
print (mr)

for i in range(0,28):
	for j in range(i,29):
		for k in range(j,30):
			if (mr[i]+mr[j]+mr[k]==0):
				print (mr[i],mr[j],mr[k])
