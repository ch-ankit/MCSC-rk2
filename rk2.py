# RK-2 method python program
import math
import sympy as sym
from prettytable import PrettyTable
from Equation import Expression
from math import sin,cos,exp,log
table = PrettyTable()

#To convert pi from the console into a floating number
def PiConverter(input):
    # Defining dictionary
    symbol={
        'pi': math.pi
    }
    output=""
    for i in input:
        # If the value of character i.e. "i" is defined as the keyword in the symbol dictonary then it is replaced and appended in output string else the character itself is appended
        output+=symbol.get(i,i) 

    return output #return the converted value

# RK-2 method
def rk2(x0, y0, xn, n,f, precision):

    # Calculating step size
    h = round((xn-x0)/n,precision)

    #Creating the table
    table.title = '💥💥  SOLUTIONS: RUNGE-KUTTA 2nd ORDER METHOD  💥💥'

    table.field_names = ['xn', 'yn', 'k1','k2','yn+1','interval-1','interval-2']

    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h), (y0+k1)))
        k = (k1+k2)/2
        yn = y0 + k
        table.add_row([f'{round(value,precision):.{precision}f}' for value in [x0, y0,k1,k2, yn,x0,x0+h]])
        y0 = yn
        x0 = x0+h

    print('\n')
    print(table)

    print(' \n 💥💥   RESULT   💥💥 \n')
    print(f'At x = {round(xn,precision):.{precision}f}, y = {round(yn,precision):.{precision}f} \n')


def main():
    # Inputs
    exp=input('\nEnter the required expression:\n y`=f(x,y): ')
    function=Expression(exp,['x','y'])

    print('\nEnter the initial conditions [ y(x0) = y0 ] :')


    print('Enter the initial conditions:')
    x0 = float(input('x0 = '))
    y0 = float(input('y0 = '))

    print('\nEnter the calculation point:')
    xn = sym.sympify(PiConverter(input('xn = ')))

    print('\nEnter the number of steps: ')
    step = int(input('Number of steps = '))


    print('\nEnter the required number of decimal places: ')
    precision = int(input('No. of decimal places: '))

    # RK2 method call
    rk2(x0, y0, xn, step, function, precision)

if __name__ == '__main__':
    main()


