import numpy as np
from scipy import optimize
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

def interactive_capdemand(q_0,a,a_base,amin,amax,b_0,b_base,bmin,bmax,k_0,k_base,kmin,kmax,theta,theta_base,thetamin,thetamax,kbar,kplot_max):
    def plot_demand(theta,a,b_0,k_0):
        cd = np.empty(q_0.size)
        cd[q_0<theta] = np.inf
        cd[q_0<(b_0/k_0)] = 0
        cd[q_0>(theta+a)] = 0
        cd[(q_0>=max(theta, b_0/k_0)) & (q_0<=theta+a)] = (q_0[(q_0>=max(theta, b_0/k_0)) & (q_0<=theta+a)]*k_0-b_0)/(q_0[(q_0>=max(theta, b_0/k_0)) & (q_0<=theta+a)]-theta)
        cs = np.minimum(kbar*np.ones(q_0.size), kbar+q_0-1-theta)
        fig = plt.figure(frameon=False, figsize=(8,5), dpi=100)
        ax = fig.add_subplot(1,1,1)
        ax.plot(q_0,cd)
        ax.plot(q_0,cs)
        ax.set_xlim([q_0[0], q_0[-1]])
        ax.set_ylim([0, kplot_max])
        ax.set_xlabel('$q_0$')
        ax.set_ylabel('$k_1$')
        plt.legend(('Demand', 'Residual supply'), loc='lower left')
        fig.tight_layout()
    widgets.interact(plot_demand,
        theta = widgets.FloatSlider(
        description="$\\theta$",
        min = thetamin,
        max = thetamax,
        step = 0.05,
        value = theta_base
        ),
        a = widgets.FloatSlider(
        description="$a$",
        min = amin,
        max = amax,
        step = 0.05,
        value = a_base
        ),
        b_0 = widgets.FloatSlider(
        description="$b_0$",
        min =bmin,
        max =bmax,
        step = 0.05,
        value = b_base
        ),
        k_0 = widgets.FloatSlider(
        description="$k_0$",
        min = kmin,
        max = kmax,
        step = 0.05,
        value = k_base
        ))