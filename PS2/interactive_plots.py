import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

def interactive_cap(n_0base, lambda_base, alpha_base, Inf, N_R, R_grid, n_0_lower, n_0_upper, n_0_step, lambda_lower, lambda_upper, lambda_step):
    def capital_demand_upper(lambda_x,n_0x):
        first = 0*np.ones(N_R)
        first_u = first[np.where(1>R_grid)]
        second = n_0x/(1-lambda_x*R_grid)
        second_u = second[np.where(np.logical_and(R_grid>=1,lambda_x*R_grid<1))]
        third = Inf*np.ones(N_R)
        third_u = third[np.where(lambda_x*R_grid>=1)]
        return np.concatenate((first_u,second_u,third_u))   

    def interactive_capital_demand(lambda_,n_0):
        cap_demand_base = capital_demand_upper(lambda_base, n_0base)
        cap_demand_n = capital_demand_upper(lambda_, n_0)
        cap_equi = (alpha_base/R_grid)**(1/(1-alpha_base))
        fig = plt.figure(frameon=False, figsize=(8,5), dpi=100)
        ax = fig.add_subplot(1,1,1)
        ax.plot(R_grid, cap_equi, color='k', linewidth=1, linestyle='--')
        ax.plot(R_grid, cap_demand_n, linewidth=1.5, label='_nolegend_')
        ax.plot(R_grid, cap_demand_base, linewidth=1.5)
        ax.set_xlim([0, 2])
        ax.set_ylim([0, n_0_upper/(1-lambda_upper)])
        ax.set_xlabel('$R(w_1)$')
        ax.set_ylabel('Capital')
        plt.legend(('Equi. condition', 'Base ($n_0$=%.1f, $\\lambda=$%.1f, $\\alpha=$%.1f)' %(n_0base, lambda_base, alpha_base)), loc='lower left')
        fig.tight_layout()

    widgets.interact(interactive_capital_demand,
        lambda_ = widgets.FloatSlider(
        description="$\\lambda$",
        min = lambda_lower, 
        max = lambda_upper,
        step = lambda_step, 
        value = lambda_base
        ),
        n_0 = widgets.FloatSlider(
        description ="$n_0$",
        min = n_0_lower,
        max = n_0_upper,
        step = n_0_step,
        value = n_0base
        ))    