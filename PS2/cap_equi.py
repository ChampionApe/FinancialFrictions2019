import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

def plot_cap(R,N_R,n_0,_lambda,alpha,Inf,n_02,_lambda_2,alpha_2):
    def capital_demand_upper(R,lambda_x,n_0x):
        first = 0*np.ones(N_R)
        first_u = first[np.where(1>R)]
        second = n_0x/(1-lambda_x*R)
        second_u = second[np.where(np.logical_and(R>=1,lambda_x*R<1))]
        third = Inf*np.ones(N_R)
        third_u = third[np.where(lambda_x*R>=1)]
        return np.concatenate((first_u,second_u,third_u))
    cd_upper = capital_demand_upper(R,_lambda,n_0)
    cd_upper2 = capital_demand_upper(R,_lambda_2,n_02)
    cd_equi = (alpha/R)**(1/(1-alpha))
    cd_equi2 = (alpha_2/R)**(1/(1-alpha))
    
    fig = plt.figure(frameon=False, figsize=(8,8), dpi=120)
    ax = fig.add_subplot(1,1,1)
    ax.plot(R, cd_upper, color='blue')
    ax.plot(R, cd_upper2, linestyle='--', color='red')
    #ax.plot(R, cd_lower, color='red', alpha=0.5)
    ax.plot(R, cd_equi, color='blue')
    ax.plot(R, cd_equi2, linestyle='--', color='red')
    #ax.fill_between(R, cd_upper, cd_lower, alpha=0.5)
    ax.set_xlim([0, 2])
    ax.set_ylim([0, 10])
    # Labels:
    ax.set_xlabel('$R(w_1)$')
    ax.set_ylabel('Capital')
    fig.tight_layout()
    return fig



