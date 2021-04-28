# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))


# num = int(input("Enter a number "))
# if (num % 2) == 0:
#     print(format(num))
# else:
#     print(format(num))

# hacker rank

if __name__ == '__main__':
    n = int(input().strip())
if n%2==1 or n in range (5,21):
   print("Weird".format(n))
else:
   print("Not Weird".format(n))