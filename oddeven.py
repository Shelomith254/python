def evn_odd(num):
	if num%2==0:
		return even
	else:
			
			return odd
def main():
	nums=int(input("please enter the number"))
	output=evn_odd(nums)
	print(f"the result in {nums} is {output}")