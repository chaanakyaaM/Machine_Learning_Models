try:
    x=list(map(int,input('enter x(comma seperated):').split(',')))
except:
    print('There is an error in you x values')
    exit()

try:
    y=list(map(int,input('enter y(comma seperated):').split(',')))
except:
    print('There is an error in you y values')
    exit()

n=len(x)

sum_x=sum(x)
sum_y=sum(y)

x_square=sum([i**2 for i in x])
y_square=sum([i**2 for i in y])

sum_xy=sum([i*j for i,j in zip(x,y)])

a=((sum_y * x_square) - (sum_x * sum_xy)) / (n * x_square - (sum_x)**2)
b=((n * sum_xy) - (sum_x * sum_y)) / ((n * x_square) - (sum_x**2))

print(f'Regression: {a}+{b}x')

x=int(input('enter val:'))

ans=int(a+(b*x))
print(f'predicted: {ans}')


