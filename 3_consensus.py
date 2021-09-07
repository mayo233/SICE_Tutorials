from scipy.integrate  import odeint
import numpy as np
import matplotlib.pyplot as plt

def MAS(x,t,N):
    
    dxdt = [0] * len(N)
    u = [0] * len(N)
    
    # Definition of agent i
    for i in range(len(N)):
        
        # Computation of the control input of agent i 
        dif = []  
    
        for j in N[i]: 
            dif.append(x[j] - x[i])    
      
        u[i] = sum(dif)   
        
        # Dynamics of agent i 
        dxdt[i] = u[i]             
    
    return dxdt

N = [[2], [3,5], [4], [1,2], [6], [2]]
x0 = [-1, 2, 6, 3, -3, 1]
t = np.arange(0, 5, 0.001)

N.insert(0,[])
x0.insert(0,0) 
x = odeint(MAS, x0, t, args=(N,))

plt.plot(t,np.delete(x, 0, 1))
plt.xlabel('t')
plt.ylabel('xi')
plt.grid()
plt.show()

plt.savefig("consensus.eps", dpi=200, bbox_inches="tight", pad_inches=0.1)