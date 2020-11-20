from prettytable import PrettyTable
table = PrettyTable()

# RK-2 method python program

# function to be solved


def f(x, y):
    return (y**2-x**2)/(y**2+x**2)


# RK-2 method
def rk2(x0, y0, xn, n):

    # Calculating step size
    h = (xn-x0)/n

    # print('\n--------SOLUTION--------')
    # print('-------------------------')
    # print('x0\ty0\tyn')
    # print('-------------------------')
    table.title = '💥💥SOLUTIONS💥💥'
    table.field_names = ['x0', 'y0', 'yn']
    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h), (y0+k1)))
        k = (k1+k2)/2
        yn = y0 + k
        table.add_row([f'{value:.4f}' for value in [x0, y0, yn]])
        # print('%.4f\t%.4f\t%.4f' % (x0, y0, yn))
        # print('-------------------------')
        y0 = yn
        x0 = x0+h

    # print('\nAt x=%.4f, y=%.4f' % (xn, yn))
    print(table)
    print(f'x={xn:.4f}, y={yn:.4f}')


# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

# RK2 method call
rk2(x0, y0, xn, step)
