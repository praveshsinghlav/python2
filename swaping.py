def swap_numbers(a, b):
    print("Before swapping: a =", a, "b =", b)

    # Swapping the numbers using a temporary variable
    temp = a
    a = b
    b = temp

    print("After swapping: a =", a, "b =", b)


# Test the swap_numbers function
num1 = 10
num2 = 20

swap_numbers(num1, num2)
