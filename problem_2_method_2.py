# Author Arunprasath Shankar
# Pure Math Method - Fastest
import time
from math import sqrt
def fibo(n):
	root5 = sqrt(5)
	phi = 0.5 + root5/2
	return int(0.5 + phi**n/root5)
list1 = []
start = time.clock
for i in range(34):
	#print 'n = %d ==> %d' % (i,fibo(i))
	if (fibo(i)) < 4000001 and (fibo(i))%2 == 0: 
		list1.append(fibo(i))
sum = 0
for l in list1:
	sum = sum + l
end = time.clock()
print 'Sum = %d' % sum 
print 'Elapsed Time = %f' % end

