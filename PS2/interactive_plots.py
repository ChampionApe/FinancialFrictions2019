import numpy as np
from scipy import optimize
import math
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

def equi_cap(N_n,N_lambda,alpha,n_grid,lambda_grid):
    k_equi = np.empty([N_n,N_lambda])
    for i in range(0,N_n):
        for j in range(0,N_lambda):
            if n_grid[i]<(1-lambda_grid[j])*alpha**(1/(1-alpha)):
                k_equi[i,j] = optimize.newton(lambda x: x-alpha*lambda_grid[j]*x**(alpha)-n_grid[i], 1, )
            else:
                k_equi[i,j] = alpha**(1/(1-alpha))
    return k_equi

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def equi_cap_figure(k_equi,n_grid,lambda_base,_lambda,lambda_grid):
    k_equi_base = k_equi[:,lambda_base]
    lambda_val = find_nearest(lambda_grid, _lambda)
    lambda_index = np.where(lambda_grid == lambda_val)
    fig = plt.figure(frameon=False, figsize=(8,5), dpi=100)
    ax = fig.add_subplot(1,1,1)
    ax.plot(n_grid,k_equi_base)
    ax.plot(n_grid,k_equi[:,lambda_index[0]])
    ax.set_xlim([n_grid[0], n_grid[-1]])
    ax.set_ylim([np.min(k_equi), np.max(k_equi)])
    ax.set_xlabel('$n_0$')
    ax.set_ylabel('$k$ in equilibrium')
    plt.legend(('Baseline', 'Adjusted $\\lambda$'))
    fig.tight_layout()

def interactive_equicap(N_n,N_lambda,alpha,n_grid,lambda_grid,lambda_base,lambda_lower, lambda_upper,lambda_step):
    k_equi = equi_cap(N_n,N_lambda,alpha,n_grid,lambda_grid)

    def plot_int(_lambda):
        equi_cap_figure(k_equi,n_grid,lambda_base,_lambda,lambda_grid)
    
    widgets.interact(plot_int,
        _lambda = widgets.FloatSlider(
        description="$\\lambda$",
        min = lambda_lower, 
        max = lambda_upper,
        step = lambda_step,
        value = lambda_grid[lambda_base]
        ))

def interactive_pc(R,I,Delta,kappa,sbar):
    def plot_int_pc(I,kappa):
        pc = (-R/2)*sbar**2+(R*(1+Delta)-kappa)*sbar+(1-Delta)*kappa-(R/2)*(1-Delta)**2-2*Delta*I
        fig = plt.figure(frameon=False, figsize=(8,5), dpi=100)
        ax = fig.add_subplot(1,1,1)
        ax.plot(sbar,pc, label='_nolegend_')
        ax.set_xlim([1-Delta, 1+Delta])
        ax.set_ylim([-2, 2])
        ax.axhline(y=0, color='k', label='_nolegend_')
        if ((R*(1+Delta)-kappa)**2+2*R*((1-Delta)*kappa-(R/2)*(1-Delta)**2-2*Delta*I))>=0:
            s_star = 1+Delta-kappa/R-(1/R)*math.sqrt((R*(1+Delta)-kappa)**2+2*R*((1-Delta)*kappa-(R/2)*(1-Delta)**2-2*Delta*I))
            ax.axvline(x=s_star,linestyle='--')
        ax.set_xlabel('s')
        ax.set_ylabel('(PC)')
        fig.tight_layout()

    widgets.interact(plot_int_pc,
        I = widgets.FloatSlider(
        description="I",
        min = 0,
        max = 2,
        step = 0.1,
        value = 1.5
        ),
        kappa = widgets.FloatSlider(
        description="$\\kappa$",
        min = 0,
        max = 1,
        step = 0.1,
        value = 0.1
        ))

    
    

