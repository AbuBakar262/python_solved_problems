import time

start_time = time.perf_counter()


class Calculate:

    # this function calculates the sum of 2 numbers...
    def sum(self, a, b):
        result = a + b
        return result

    # this function calculates the multiplication of 2 numbers...
    def product(self, c, d):
        result = c * d
        return result

    # this function calculates the difference between 2 numbers...
    def difference(self, num1, num2):
        return num1 - num2


obj = Calculate()

# Calculation of Sum....
result_sum = obj.sum(2, 3)
print("Sum of Number 1 and Number 2 is", result_sum)
print()
print("Sleeping for 1 seconds")
print()
time.sleep(1)

# Calculation of Product / Multiplication.....
result_mul = obj.product(5, 3)
print("Product of Num+_1 and Num_2 is", result_mul)
print()
print("Sleeping for 3 seconds")
print()
time.sleep(3)
# Calculation of Difference.....
result_diff = obj.difference(7, 3)
print("Difference of Num+_1 and Num_2 is", result_diff)
print()
print("Sleeping for 5 seconds")
print()
time.sleep(5)

finish_time = time.perf_counter()
print("Finished in ", round(finish_time-start_time, 2), "second(s)")
