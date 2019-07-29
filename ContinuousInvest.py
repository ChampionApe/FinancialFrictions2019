# Note: Core code for running the simple continuous investment model, in Jean Tirole: The theory of corporate finance, chapter 3.

import time
import numba
import numpy as np
from scipy import optimize 
from scipy import interpolate 
from types import SimpleNamespace

import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
prop_cycle = plt.rcParams["axes.prop_cycle"]
colors = prop_cycle.by_key()["color"]

import ipywidgets as widgets 

class ContinousInvest:

    # __init__ is reserved for the commando initializing an instance of the class.
    def __init__(self, **kwargs):
        # a) Baseline setup:
        
        # Return to investment function, when succesfull:
        self.technology = "DecreasingReturns"
        self.a = 1
        self.b = 0.5

        # Probabilities of succes:
        self.p_high = 0.75
        self.p_low = 0.5

        # Entrepreneur variables:
        self.A = 1
        self.B = 2

        # figures:
        self.x1label = "$\\ell$"
        self.x2label = "$A$"
        self.N = 100

        # b) Update:
        for key, val in kwargs.items():
            setattr(self,key,val)

        self.calculations()

    def calculations(self):
        if self.technology == "DecreasingReturns":
            
