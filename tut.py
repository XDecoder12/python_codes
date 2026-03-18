import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

# from matplotlib.animation import FuncAnimation
# from IPython.display import HTML

def lorenz(t, state, sigma=10, beta=8/3, rho=28):
    x, y, z = state
    dxdt = sigma * (y-x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

t_span = (0, 40)
t_eval = np.linspace(*t_span, 5000)
initial_state = [1.0, 1.0, 1.0]

sol = solve_ivp(lorenz, t_span, initial_state, t_eval=t_eval, method='RK45')
x, y, z = sol.y

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z, lw=0.7, color='purple')
ax.set_title('Lorenz Atractor - Static 3d View')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# def integrate_lorenz(initial_state, t_span, t_eval):
#     sol = solve_ivp(lorenz, t_span, initial_state, t_eval=t_eval, method='RK45')
#     return sol.y

# trajectories = [integrate_lorenz(init, t_span, t_eval) for init in initial_state]