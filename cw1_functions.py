import numpy as np

def initial_f(x):

    output = np.sin(x) + np.cos(x)

    return output

def function_Q(x, t):

    output = np.cos(x)/(1 + np.exp(t))

    return output



    

