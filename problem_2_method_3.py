# Matrix Method
import time
import numpy
fibo_matrix = numpy.matrix([[1,1],[1,0]])
def fibo(n):
	return (fibo_matrix ** (n-1)) [0,0]
list1 = []
start = time.clock()
for i in range(34):
	# print 'n = %d ==> %d' % (i,fibo(i))
	if (fibo(i)) < 4000001 and (fibo(i))%2 == 0:
		list1.append(fibo(i))
sum = 0
for l in list1:
	sum = sum + l
end = time.clock()
print 'Sum = %d' % sum
print 'Elapsed Time = ',end - start,'seconds'
