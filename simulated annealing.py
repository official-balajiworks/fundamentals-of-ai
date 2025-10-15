import math
import random
import matplotlib.pyplot as plt

# Objective function
def f(x):
    return x**2 + 10 * math.sin(x)

# Simulated Annealing function
def simulated_annealing(objective, x_start, T_max, T_min, cooling_rate):
    x_current = x_start
    f_current = objective(x_current)
    best_x, best_f = x_current, f_current
    temperatures, energies = [], []

    T = T_max
    while T > T_min:
        # Generate new candidate
        x_new = x_current + random.uniform(-1, 1)
        f_new = objective(x_new)
        delta_E = f_new - f_current

        # Accept better solutions or sometimes worse ones
        if delta_E < 0 or math.exp(-delta_E / T) > random.random():
            x_current, f_current = x_new, f_new
            if f_new < best_f:
                best_x, best_f = x_new, f_new

        # Record data
        temperatures.append(T)
        energies.append(f_current)

        # Cool down
        T *= cooling_rate

    return best_x, best_f, temperatures, energies


# Run the algorithm
best_x, best_f, temps, energies = simulated_annealing(f, x_start=5, T_max=1000, T_min=1e-3, cooling_rate=0.99)

print(f"Best solution: x = {best_x:.4f}, f(x) = {best_f:.4f}")

# Plot energy vs temperature
plt.plot(temps, energies)
plt.xlabel("Temperature")
plt.ylabel("Energy (Cost Function)")
plt.title("Simulated Annealing Progress")
plt.show()
