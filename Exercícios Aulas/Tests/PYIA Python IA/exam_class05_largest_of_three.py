def biggest_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
<<<<<<< HEAD
    
    elif num2 > num1 and num2 > num3:
        return num2
    
=======
    elif num2 > num1 and num2 > num3:
        return num2
>>>>>>> 8a36c80a601eb8941e4f1f3b5534d0a744ff19ad
    else:
        return num3

print(biggest_number(1, 3, 5))