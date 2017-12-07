import sys


def double(x):
    y = x * 2
    a = 1
    return y


for i in (0, 1):
    pass

for x in range(0, 3):
    print('Hello, World!' + str(x))


z = 0
if(0):
    print('Constant Unreachable Print statement!' + str(z))
    j = 70
    k = 0
    dk = double(k)
    for i in range(0, 70):
        k += 1
    k = 5


if(False):
    print('Second Constant Unreachable Print statement!' + str(z))


if(z):
    print('Unreachable Print statement!' + str(z))

print('3 doubled is: ' + str(double(3)))

sys.exit()
print('6 doubled is: ' + str(double(6)))
