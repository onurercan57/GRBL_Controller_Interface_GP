# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

i=300
a=[]
us=[]
x=[]
y=[]
z=[]
while i<=1500:
    b=np.std(np.loadtxt("C:/Users/SCORPTR/Desktop/TEZ/yenilog/motor1kg/{}.txt".format(i)),axis=0)
    us.append(i)
    
    a.append(b.tolist())
    if i<1200:
        i+=50
    elif i<=1500:
        i+=100
for i,j,k in a:
    x.append(i)
    y.append(j)
    z.append(k)

print(a,"----------")
print(x)
print(y)
print(z)
print(us)


plt.figure(figsize=(20,6))

"""
plt.plot(us,x,color = "blue")
plt.plot(us,y,color = "red")
plt.plot(us,z,color = "green")
plt.title("Vibration of bed for different step periods")
plt.xlabel("Periods of steps(μs)")
plt.ylabel("Vibration amount(0-512)")
"""
#axis=np.arange(us)
barwitdh=10

usx=[]
usy=[]
usz=[]
plt.xticks(us)
for i in us:
    usx.append(i-barwitdh)
    usy.append(i)
    usz.append(i+barwitdh)



p1=plt.bar(usx,x, width=10, color="orange",linewidth=2,hatch="o")
p2=plt.bar(usy,y, width=10, color="red",linewidth=2)
p3=plt.bar(usz,z, width=10, color="blue",linewidth=2,hatch="/")


plt.title("Vibration of motor for different step periods(1kg)")
plt.xlabel("Periods of step(μs)")
plt.ylabel("Vibration amount")
plt.legend((p1[0],p2[0],p3[0]),("X axis","Y axis","Z axis"),prop={'size': 20})
plt.show()

