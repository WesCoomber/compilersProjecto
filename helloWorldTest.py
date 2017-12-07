import sys

'''
You should get this output when running our flake8 plugin on the helloWorldTest.py file:
notice that it correctly catches the second if (cero) dead code block, the first if(cero) code block is NOT DEAD
and it catches the single indirect if(z) dead code block

➜  codingtools git:(master) ✗ flake8 helloWorldTest.py
helloWorldTest.py:6:5: F841 local variable 'a' is assigned to but never used
helloWorldTest.py:18:1: A421 dead code after if(0) statement.
startOfDeadCode block for if() statement starting at line 18.
    <class '_ast.Print'>[<_ast.BinOp object at 0x101dedf50>]
    <class '_ast.Assign'><_ast.Num object at 0x101e07150>
    <class '_ast.Assign'><_ast.Num object at 0x101e07210>
    <class '_ast.Assign'><_ast.Call object at 0x101e072d0>
    <class '_ast.For'><_ast.Name object at 0x101e073d0>
    <class '_ast.Assign'><_ast.Num object at 0x101e07650>
endOfDeadCode block for if() statement starting at line 18.

helloWorldTest.py:28:1: A422 dead code after if(False) statement.
startOfDeadCode block for if() statement starting at line 28.
    <class '_ast.Print'>[<_ast.BinOp object at 0x101e07750>]
endOfDeadCode block for if() statement starting at line 28.

helloWorldTest.py:32:1: A423 dead code after if(z) statement, indirect if(0) detected.
startOfDeadCode block for if() statement starting at line 32.
    <class '_ast.Print'>[<_ast.BinOp object at 0x101e07950>]
endOfDeadCode block for if() statement starting at line 32.

helloWorldTest.py:41:1: A423 dead code after if(cero) statement, indirect if(0) detected.
startOfDeadCode block for if() statement starting at line 41.
    <class '_ast.Print'>[<_ast.BinOp object at 0x101e07ed0>]
endOfDeadCode block for if() statement starting at line 41.

helloWorldTest.py:46:1: A424 dead code after sys.exit() expression on line 46.
'''

def double(x):
    y = x * 2
    a = 1
    return y


# for i in (0, 1):
#    pass

for x in range(0, 3):
    print('Hello, World!' + str(x))

foo = 3
z = 0
if 0:
    print('Constant Unreachable Print statement!' + str(z))
    j = 70
    k = 0
    dk = double(k)
    for i in range(0, 70):
        k += 1
    k = 5


if False:
    print('Second Constant Unreachable Print statement!' + str(z))


if z:
    print('Unreachable Print statement! Single Indirect' + str(z))

cero = foo
if cero:
    print('YES REACHABLE Print statement! Double Indirect' + str(z))

cero = z

if cero:
    print('Unreachable Print statement! Double Indirect' + str(z))

print('3 doubled is: ' + str(double(3)))

sys.exit()
print('6 doubled is: ' + str(double(6)))
