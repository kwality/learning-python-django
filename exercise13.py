

how_many_times = int(input("How many Fibonacci number to generate? >>>> "))
count = 0
holder = [1,2,3,4,5,6]

<<<<<<< HEAD
# def fibonacci_number_please(num):
# 	if num == 1:
# 		print("thi")
# 		return [1, 1]
# 	return holder.append(holder[len(holder)] + holder[len(holder) - 1])

# while True:
# 	if count <= how_many_times:
# 		count += 1
# 		print(fibonacci_number_please(int(how_many_times)));
# 	else:
# 		break
# 		print("finished")

def do_fibonacci():
	print(holder[len(holder)])
	print(holder[len(holder) - 2])
	return holder.append(holder[len(holder) -1] + holder[len(holder) - 2])

def fibonacci(times):
	for num in range(1, int(times)):
		print(do_fibonacci())
		

fibonacci(how_many_times)
=======
new_number = holder[len(holder) - 2]
last_number = holder.pop()

new = last_number + new_number
print(last_number)
print(new_number)

print(new)



print(holder)


# def fibonacci_number_please(holder):
# 	if len(holder) == 1:
# 		return [1, 1]
# 	if len(holer) >= 1:
# 		print(holder)
# 		fibonacci_number_please(holder.append(holder.pop() + holder[len(holder) - 2]))
# 	else:
# 		return holder
#
# while True:
# 	if count <= how_many_times:
# 		count += 1
# 		print(fibonacci_number_please(holder));
# 	else:
# 		print("finished")
# 		break
>>>>>>> d564eea3822c11ea554d297e6308f7aa603e869d
