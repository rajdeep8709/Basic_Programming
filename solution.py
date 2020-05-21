#The fact that uses here that a^a=0,hence all twice occurence 
#number is become zero. 
def solution(array):
	ans = 0
	for i in range(len(array)):
		ans = ans ^ array[i]
	return ans	
array = list(map(int,input().split()))
print(solution(array))
