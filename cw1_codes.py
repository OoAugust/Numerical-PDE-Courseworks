from cw1_functions import initial_f, function_Q
import numpy as np

x_length = 4 * np.pi
t_length = 1
N = 1000
M = 1000

def hyperdiff_explicit(x_length, t_length, N, M):
    
    h = x_length/N
    k = t_length/M
    output_array = np.zeros(shape = (M + 1, N + 1))
    output_array[0, :] = initial_f(np.linspace(0, x_length, N + 1))
    period_length = int(np.floor( N / (x_length/(2 * np.pi))))


    for i in range(1, M + 1):

        

        output_array[i, 2 : N - 1] = (k/(h ** 4)) * (output_array[i - 1, 4 : N + 1] + output_array[i - 1, 0 : N - 3] - 
                                                4 * (output_array[i - 1, 3 : N] + output_array[i - 1, 1 : N - 2]) +
                                                6 * output_array[i - 1, 2 : N - 1]) + output_array[i - 1, 2 : N - 1]


        output_array[i , 0 : 2] = output_array[i, period_length : period_length + 2]
        output_array[i, N - 1 : N + 1] = output_array[i, N - 1 - period_length : N + 1 - period_length]

    
    return output_array
        
        



              


    
    return output_array




