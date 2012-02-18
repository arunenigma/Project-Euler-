# Author -- Arunprasath Shankar
# Solved using recursion
# Run time is longer than the Matrix and Pure Math methods..
# Will post the Matrix and Pure Math Methods Shortly
import time
def fibo(n):
	if n < 2:
		return n
	return fibo(n-2) + fibo(n-1)
sum = 0
list1 = map(fibo,range(2,36)) # choose range based on your intuition
print list1
list2 = []
start = time.clock()
for l in list1:
	if l < 4000001 and l%2 == 0:
		list2.append(l)
		print list2
	else:
		pass

for l in list2:
	sum = sum + l
end = time.clock()
print 'sum = %d' % sum
print 'Elapsed Time = ',end - start,'seconds'
