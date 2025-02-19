import numpy as np
import matplotlib.pyplot as plt

# Parameters
beta_a = 0.01  # Attack rate in attacker's space
theta_a = 0.1  # Natural failure rate of attackers
nu_a = 0.05  # Recovery rate of attackers
beta_t = 0.02  # Attack rate in target population
sigma_t = 0.1  # Recovery rate of compromised devices
theta_t = 0.05  # Failure rate of recovered devices
p = 0.1  # Protection rate
Pi = 10  # Recruitment rate for susceptible targets

# Initial conditions
S_a = 1000  # Initial susceptible attackers
M_a = 50  # Initial malicious attackers
S_t = 5000  # Initial susceptible targets
M_t = 10  # Initial compromised targets
R_t = 200  # Initial recovered targets
S_p = 100  # Initial protected targets

# Time parameters
T = 100  # Total time steps
dt = 1  # Time step size

# Arrays to store results
time = np.arange(0, T, dt)
S_a_history = np.zeros_like(time)
M_a_history = np.zeros_like(time)
S_t_history = np.zeros_like(time)
M_t_history = np.zeros_like(time)
R_t_history = np.zeros_like(time)
S_p_history = np.zeros_like(time)

# Initial values
S_a_history[0] = S_a
M_a_history[0] = M_a
S_t_history[0] = S_t
M_t_history[0] = M_t
R_t_history[0] = R_t
S_p_history[0] = S_p

# Iterative solution
for n in range(1, len(time)):
    # Solve for S_a and M_a
    S_a_next = (S_a_history[n - 1] + nu_a * M_a_history[n - 1] * dt) / (
                1 + (beta_a * M_a_history[n - 1] + theta_a) * dt)
    M_a_next = (M_a_history[n - 1] + beta_a * S_a_next * M_a_history[n - 1] * dt) / (1 + (theta_a + nu_a) * dt)

    # Solve for S_t, M_t, R_t, and S_p
    lambda_t = beta_a * M_a_next + beta_t * M_t_history[n - 1]
    S_t_next = (S_t_history[n - 1] + Pi * dt) / (1 + lambda_t * dt)
    M_t_next = (M_t_history[n - 1] + lambda_t * S_t_next * dt) / (1 + (sigma_t + p) * dt)
    R_t_next = (R_t_history[n - 1] + sigma_t * M_t_next * dt) / (1 + theta_t * dt)
    S_p_next = S_p_history[n - 1] + p * M_t_next * dt

    # Update values
    S_a_history[n] = S_a_next
    M_a_history[n] = M_a_next
    S_t_history[n] = S_t_next
    M_t_history[n] = M_t_next
    R_t_history[n] = R_t_next
    S_p_history[n] = S_p_next

# Plot results
plt.figure(figsize=(12, 8))

# Attacker's space
plt.subplot(2, 1, 1)
plt.plot(time, S_a_history, label='Susceptible Attackers ($S_a$)')
plt.plot(time, M_a_history, label='Malicious Attackers ($M_a$)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Attacker Population Dynamics')
plt.legend()
plt.grid()

# Target population
plt.subplot(2, 1, 2)
plt.plot(time, S_t_history, label='Susceptible Targets ($S_t$)')
plt.plot(time, M_t_history, label='Compromised Targets ($M_t$)')
plt.plot(time, R_t_history, label='Recovered Targets ($R_t$)')
plt.plot(time, S_p_history, label='Protected Targets ($S_p$)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Target Population Dynamics')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()