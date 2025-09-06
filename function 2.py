def calculate_sum_and_average(numbers):
       if not numbers:
       	return invalid
total_sum=sum(numbers)
average=total_sum/len(numbers)
return total_sum,average
numbers=(5,10,15,20,25)
total_sum,average=calculate_sum_and_average(numbers)
print('sum',total_sum,'average',average)