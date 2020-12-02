import sympy as sym         
from prettytable import PrettyTable
import math
from tabulate import tabulate

#stating x and y as variables in equation
x,y = sym.symbols('x y')


class NewtonMethodForSystem:
    def __init__(self,initial_approx,functions,tolerance,steps=40):
        self.a=initial_approx
        self.steps=steps
        self.tolerance=tolerance
        self.table=PrettyTable(['x','y','f','g','a','b','c','d','ad-bc','-fd+gb','-ga+fc','h','k'])

    def __repr__(self):
        return "NewtonRaphsonForSystem(initial_approx:{},tolerance:{})".format(self.a,self.tolerance)

    def calc(self):
        #taking initial approximations and storing in i and j
        i,j=self.a[0],self.a[1]
        for q in range(40):
            f_ins=   f.subs([(x, i), (y, j)])           #sympy subs function to calculate functional values
            g_ins=   g.subs([(x, i), (y, j)])
            a_ins=   a.subs([(x, i), (y, j)])
            b_ins=   b.subs([(x, i), (y, j)])
            c_ins=   c.subs([(x, i), (y, j)])
            d_ins=   d.subs([(x, i), (y, j)])
            D=a_ins*d_ins-b_ins*c_ins
            D_1=-f_ins*d_ins+g_ins*b_ins
            D_2=-g_ins*a_ins+f_ins*c_ins
            h=D_1/D
            k=D_2/D 

            self.table.add_row([f"{value:.5f}"for value in [round(i,4),round(j,4),
                                round(f.subs([(x, i), (y, j)]),4),
                                round(g.subs([(x, i), (y, j)]),4),
                                round(a.subs([(x, i), (y, j)]),4),
                                round(b.subs([(x, i), (y, j)]),4),
                                round(c.subs([(x, i), (y, j)]),4),
                                round(d.subs([(x, i), (y, j)]),4),
                                round(D,4),round(D_1,4),
                                round(D_2,4),round(h,4),round(k,4)]])
            i=i+h
            j=j+k
            if (round(abs(f.subs([(x, i), (y, j)])),5)<self.tolerance) and (round(abs(g.subs([(x, i), (y, j)])),5)<self.tolerance):
                break

        return self.table

text = """
Newton Rhapson Method For System of Non-linear Equations.\nEnter the two non linear equations below.\nFor instance f(x,y) = x^2+3*x+2*y+7
"""

table = [[text]]
output = tabulate(table, tablefmt='grid')

print(output)

def convert_to(input):
    # Defining dictionary
    symbol={
        '^':'**'
    }
    output=""
    for i in input:
        # If the value of character i.e. "i" is defined as the keyword in the symbol dictonary then it is replaced and appended in output string else the character itself is appended
        output+=symbol.get(i,i) 

    return output #return the converted string

#taking system of non linear equations as input
f = sym.sympify(convert_to(input('Enter f(x,y): ')))
g = sym.sympify(convert_to(input('Enter g(x,y): ')))
N_places = int(input('Enter Correct To Decimal Places : '))
initial_approx_1 = float(input('Enter initial approximations:\nx = '))
initial_approx_2 = float(input('y = '))

tolerance= 0.5*pow(10, -N_places)

a = sym.diff(f,x)           #sympy function for calculating derivative of function
b = sym.diff(f,y)
c = sym.diff(g,x)
d = sym.diff(g,y)


ques =NewtonMethodForSystem([initial_approx_1,initial_approx_2],[f,g,a,b,c,d],tolerance)
print(repr(NewtonMethodForSystem([initial_approx_1,initial_approx_2],[f,g,a,b,c,d],tolerance)))
print(ques.calc())
