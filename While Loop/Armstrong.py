# 1) Ask the user to enter a number and store it in `num`.

# 2) Set `sum` to 0.
#    (This will store the total of the cubes of each digit.)

# 3) Copy `num` into `temp`.
#    (We will change `temp` while checking digits, but we must keep `num` unchanged.)

# 4) Repeat while `temp` is greater than 0:
#    a) Find the last digit of `temp` and store it in `digit`.
#    b) Add (digit × digit × digit) to `sum`.
#    c) Remove the last digit from `temp` so you can move to the next digit.

# 5) After the loop, compare `num` and `sum`:
#    - If they are the same, print: `num` is an Armstrong number.
#    - Otherwise, print: `num` is not an Armstrong number.

num = int(input("Enter a  3- digit number: "))
sum = 0

temp = num



while temp > 0:
    digit = temp % 10 # gets the last digit
    sum = sum + (digit**3)
    temp = temp // 10 # removes the last digit
    
if sum == num:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
    

