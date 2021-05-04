# Python code to demonstrate the working of Greatest Common Divisor (GCD) #
# Contains three methods labeled as STL, Recursion, and Euclidean Algorithm #

# Method to compute GCD using STL #
# Importing "math" for mathematical operations #

import math

# Find the GCD of 21600 and 2970 #

print("By Using STL The GCD of 21600 and 2970 is: ", end="")
print(math.gcd(21600,2970))

# The output is 270 for GCD 21600 and 2970 #
# The Calculation also done manually and resulted the same value (output) #

# Proceed to the next problem #

# Find the GCD of 2679 and 851 #

import math
print("By Using STL The GCD of 2679 and 851 is: ", end="")
print(math.gcd(2679,851))

# The output is 1 for GCD 2679 and 851 #
# The Calculation also done manually and resulted the same value (output) #

# Proceed to next problem #

# Find the GCD of -456 and 688 #

import math
print("By Using STL The GCD of -456 and 688 is: ", end="")
print(math.gcd(-456,688))

# The output is 8 for GCD -456 and 688 #
# The Calculation also done manually and resulted the same value (output) #

# Method to compute GCD using Recursion #

# Find the GCD of 21600 and 2970 #

def hcf(a,b) :
    if(b==0) :
        return a
    else:
        return hcf(b, a % b)
a=21600
b=2970

print("By Using Recursion The GCD of 21600 and 2970 is: ", end="")
print(hcf(21600,2970))

# The output is 270 for GCD 21600 and 2970 #
# Both STL and Recursion method provided the same result #

# Method to compute the GCD using Euclidean Algorithm #

# Pseudo Code of The Algorithm #
#   1. Let (a) and (b) be the two number;
#   2. Start by inputing n, m;
#   3. (a) has the max value on given value n, m, show by: a == max{n,m};
#   4. (b) has the min value on given value n, m, show by: a == min(n,m);
#   5. Find (q) as the largest integer such that q(b) <= a;
#   6. (a) % (b) = r, Let a = b and b = r;
#   7. The set defined as: r = qb - a;
#   8. Continue Looping in Iteration until a % b <= 0;
#   9. The result value b = gcd(n.m) == b;
#   10. Finish

# Method to compute GCD of 2016 and 273 using pseudo code of the Euclidean Algorithm #
# As given a=2016, b=273 #

def gcd(a,b):
    # Everything divides 0 #
    if (a==0) :
        return b
    if (b==0) :
        return a
    
    # base case #
    if (a==b) :
        return a
    
    # a is greater #
    if (a>b) :
        return gcd(a-b, b)
    return gcd(a, b-a)

# Input value of (a) and (b) #
a=2016
b=273
if(gcd(a,b)) :
    print('By Using Euclidean Algorithm The GCD of', a, 'and', b, 'is:', gcd(a, b))
else :
    print('Pus Besar')

# The output is 21 for GCD 2016 and 273 #
# Tested methods: STL, Recursion, and Euclidean Alogorithm provided the same result #
# All function working properly #