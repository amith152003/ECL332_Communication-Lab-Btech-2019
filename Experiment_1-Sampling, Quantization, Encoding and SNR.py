import numpy as np
import matplotlib.pyplot as plt

amplitude = 1
fm = 100
t = np.arange(0, 0.05, 0.0005)

#1
x = np.sin(2*np.pi*fm*t)

#2
x_offset = x + 1

#3
fs = 10*fm
Ts = 1/fs
n = np.random.randint(2, size = len(t))
nTs = n*Ts
T = np.arange(0, 0.05, Ts)
x_s = np.sin(2*np.pi*fm*T)

#4
n = 3
L = 2**n
x_max = round(max(x))
x_min = round(min(x))
delta = (x_max - x_min)/2
Q_level = np.linspace(x_min, x_max, L+1)

x_q = np.linspace(0, 2*x_max, L, endpoint = False)
t_1 = t[0:len(x_q)]

#5
x_q_1 =[]

for i in x_s:
  for j in Q_level:
    if i>=j:
      x_q_1.append(j)
      break

e_q = x_q_1 - x_s
n=[5,6,7,8,9]
gamma = []

for i in range(len(n)):
  gamma.append(1.8+6*n[i])

plt.figure()
plt.subplot(2,2,1)
plt.plot(t, x)
plt.grid()

plt.subplot(2,2,2)
plt.plot(t, x_offset)
plt.grid()

plt.subplot(2,2,3)
plt.stem(T,x_s)
plt.grid()

plt.subplot(2,2,4)
plt.step(t_1,x_q)
plt.grid()

plt.figure()
plt.plot(n, gamma)

plt.show()

