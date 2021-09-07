from scipy.integrate  import odeint
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import Polygon, Point

def MAS(x,t):
    
    x = np.array(x).reshape(-1, 2)
    dxdt = []
    
    # Definition of agent i
    for i in range(len(x)):
              
        # Control input of agent i
        cent, vor = voronoicentroid(np.array(x).reshape(-1, 2),workspace)
        u_i = -1 *(x[i] - cent[i])
        
        # Dynamics of agent i
        dxdt.append(u_i.tolist())
        
    return sum(dxdt,[]) 

def voronoicentroid(x,workspace):
    
    wb = workspace.bounds
    wl = workspace.length
    D = np.array([[wb[0] - wl * 10, wb[1] - wl * 10],
                  [wb[2] + wl * 10, wb[1] - wl * 10],
                  [wb[0] - wl * 10, wb[3] + wl * 10],
                  [wb[2] + wl * 10, wb[3] + wl * 10]])
    
    points = np.append(x, D, axis=0)
    
    vor = Voronoi(points)
    #vor = Voronoi(x)
    vcentroid = x

    for i in range(len(x)):
            poly = [vor.vertices[v] for v in vor.regions[vor.point_region[i]]]
            i_cell = workspace.intersection(Polygon(poly))
            vcentroid[i] = i_cell.centroid.coords[0]

    return  vcentroid, vor            

workspace = Polygon([[0, 0], [1, 0], [1, 1], [0, 1]])
x0 = np.array([[0.1, 0.1], [0.2, 0.1], [0.25, 0.3], [0.35, 0.2], [0.3, 0.3],
              [0.3, 0.5], [0.4, 0.15], [0.4, 0.3], [0.4, 0.4], [0.5, 0.4]])
t = np.arange(0, 50, 0.01)
x = odeint(MAS, np.array(sum(x0.tolist(),[])), t)

for i in range(len(x)):
    if i%100 == 0:
        cent, vor = voronoicentroid(np.array(x[i]).reshape(-1, 2),workspace)       
        voronoi_plot_2d(vor)
        plt.gca().set_aspect('equal')
        plt.gca().set_xlim([0, 1])
        plt.gca().set_ylim([0, 1])
        plt.show()









































