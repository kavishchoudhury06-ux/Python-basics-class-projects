# The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given number.

mean = 38

total_numbers = 40

correct_number = 56

incorrect_number = 36

sum = mean * total_numbers

print(sum)

# correct sum the these numbers

correct_sum = sum - (incorrect_number - correct_number)

print(correct_sum)

# correct mean

correct_mean = correct_sum / total_numbers

print("Correct Mean is:", correct_mean)