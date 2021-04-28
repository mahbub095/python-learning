# if(3<2):
#     print('ok')
# elif(1>2):
#     print('No')
# else:
#     print(1+1)
# print('hello')

print('Enter your command')
robot_move = input()

if robot_move == 'front':
    print('Moving Front')
elif robot_move =='back':
    print('Moving Back')
else:
    print('Stand Still')