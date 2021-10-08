house = [0 for i in range(100)]

def walk(number):
	seq = [i-1 for i in range(1,101) if i%number==0]
	for i in seq:
		if house[i]:
			house[i]=0
		else:
			house[i]=1


for i in range(1,101):
	walk(i)

sum = 0
for i in range(100):
	if house[i]:
		print(i+1)
		sum+=1

print("\n")
print(sum)

