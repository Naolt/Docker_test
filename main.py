def fizzbuzz(num):
	if not num % 3 and not num % 5:
		return "FizzBuzz"
	elif not num % 3:
		return "Fizz"
	elif not num % 5:
		return "Buzz"
	else:
		return str(num)
	

def main():
	num = int(input("Enter a number: "))	
	print(fizzbuzz(num))

if __name__ == "__main__":
	main()

