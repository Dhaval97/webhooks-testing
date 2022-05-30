"""
+
++
+++
"""

print("Using For Loop")
for i in range(1,4):
    print("+"*i)

print("===================================================")

print("Using While Loop")
j = 1
while(j<4):
    print("+"*j)
    j += 1

print("===================================================")

"""
*
**
***
+
++
+++
"""

print("Using For Loop")
for i in range(1,4):
    print("*"*i)
for i in range(1,4):
    print("+"*i)

print("===================================================")

print("Using While Loop")
m = 1
n = 1
while(m<4):
    print("*"*m)
    m += 1
while(n<4):
    print("+"*n)
    n += 1

print("===================================================")

"""
*
**
***
****
***
**
*
"""

print("Using For Loop")
for i in range(1,4):
    print("*"*i)
for i in range(-4,0):
    print("*"*abs(i))

print("===================================================")

print("Using While Loop")
p = 1
q = -4
while(p<4):
    print("*"*p)
    p += 1
while(q<0):
    print("*"*abs(q))
    q += 1

print("===================================================")
