This repository contains a JSON file (simulation_results.json) that stores the results of a discrete-time simulation model
describing the interactions between attacker and target populations.

The simulation is based on a system of difference equations that track the evolution of multiple compartments over time.
The discrete-time system model for analyzing the spread of malware in IoT networks. 
The model consists of two interconnected populations: the attacker population and the target population. 

\begin{align}
 S_a^{n+1}-S_a^n&=-\beta_a S_a^{n+1} M_a^{n+1}-\theta_a S_a^{n+1}+\nu_a\,M^{n+1}_a \\
 M_a^{n+1}-M_a^n&=\beta_a S_a^{n+1} M_a^{n+1}-(\theta_a+\nu_a)\,M_a^{n+1}a 
\end{align}


and the targeted population is:

\begin{align}
S_t^{n+1}-S_t^n&=\Pi-\left(\beta_a M_a^{n+1}+\beta_t M_t^{n+1}\right) S_t^{n+1} \\
 M_t^{n+1}-M_t^n&=\left(\beta_a M_t^{n+1}+\beta_t M_t^{n+1}\right) S_t^{n+1}-\sigma_t M_t^{n+1}-p M_t^{n+1} \\
 R_t^{n+1}-R_t^n&=\sigma_t M_t^{n+1}-\theta_t R_t^{n+1} \\
 S_p^{n+1}-S_p^n&=p M_t^{n+1}
\end{align}
