This repository contains a JSON file (simulation_results.json) that stores the results of a discrete-time simulation model
describing the interactions between attacker and target populations.

The simulation is based on a system of difference equations that track the evolution of multiple compartments over time.
The discrete-time system model for analyzing the spread of malware in IoT networks. 
The model consists of two interconnected populations: the attacker population and the target population. 



## Attacker Dynamics
The dynamics of susceptible attackers (\(S_a\)) and malicious attackers (\(M_a\)) are given by:

$$
S_a^{n+1} - S_a^n = -\beta_a S_a^{n+1} M_a^{n+1} - \theta_a S_a^{n+1} + \nu_a M_a^{n+1}
$$

$$
M_a^{n+1} - M_a^n = \beta_a S_a^{n+1} M_a^{n+1} - (\theta_a + \nu_a) M_a^{n+1}
$$

## Target Population Dynamics
The target population dynamics are described by:

$$
S_t^{n+1} - S_t^n = \Pi - (\beta_a M_a^{n+1} + \beta_t M_t^{n+1}) S_t^{n+1}
$$

$$
M_t^{n+1} - M_t^n = (\beta_a M_t^{n+1} + \beta_t M_t^{n+1}) S_t^{n+1} - \sigma_t M_t^{n+1} - p M_t^{n+1}
$$

$$
R_t^{n+1} - R_t^n = \sigma_t M_t^{n+1} - \theta_t R_t^{n+1}
$$

$$
S_p^{n+1} - S_p^n = p M_t^{n+1}
$$
