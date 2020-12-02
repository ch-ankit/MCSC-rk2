# RK-2 method python program
from math import *
from prettytable import PrettyTable
from Equation import Expression
from math import sin,cos,exp,log
table = PrettyTable()

# RK-2 method
def rk2(x0, y0, xn, n,f, precision):

    # Calculating step size
    h = round((xn-x0)/n,precision)
    # print('\n--------SOLUTION--------')
    # print('-------------------------')
    # print('x0\ty0\tyn')
    # print('-------------------------')
    table.title = '💥💥  SOLUTIONS  💥💥'
    table.field_names = ['xn', 'yn', 'k1','k2','yn+1','interval-1','interval-2']
    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h), (y0+k1)))
        k = (k1+k2)/2
        yn = y0 + k
        table.add_row([f'{round(value,precision):.{precision}f}' for value in [x0, y0,k1,k2, yn,x0,x0+h]])
        # print('%.4f\t%.4f\t%.4f' % (x0, y0, yn))
        # print('-------------------------')
        y0 = yn
        x0 = x0+h

    # print('\nAt x=%.4f, y=%.4f' % (xn, yn))
    print('\n')
    print(table)
    print(' \n 💥💥   RESULT   💥💥 \n')
    print(f'At x = {round(xn,precision):.{precision}f}, y = {round(yn,precision):.{precision}f} \n')


def main():
    # Inputs
    exp=input('Enter the required expression: y`=f(x,y):')
    function=Expression(exp,['x','y'])
    precision = int(input('Enter the required number of decimal places: \t'))
    print('Enter the initial conditions:')
    x0 = float(input('x0 = '))
    y0 = float(input('y0 = '))

    print('Enter the calculation point: ')
    xn = float(input('xn = '))

    print('Enter the number of steps:')
    step = int(input('Number of steps = '))


    # RK2 method call
    rk2(x0, y0, xn, step, function, precision)

if __name__ == '__main__':
    main()


