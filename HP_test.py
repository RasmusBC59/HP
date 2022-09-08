# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:22:27 2022

@author: Triton4acq_2
"""

from HP8594 import SpectrumAnalyzer
import matplotlib.pyplot as plt
import numpy as np

HP = SpectrumAnalyzer()
# HP.freq_center
# result = HP.get_trace()
# result_binary = HP.get_trace_in_binary()
# freq = HP.get_sweeps(1)
HP.freq_start(0)
# HP.freq_stop

# import pyvisa
# rm = pyvisa.ResourceManager()
# visa_list = rm.list_resources()
# HP = rm.open_resource('GPIB0::6::INSTR', timeout=5)
# HP.write('CF?')
# HP.read_raw()


#%% Data extraction
result_binary = HP.get_trace_in_binary() 
result_decode = result_binary.decode()    
result = result_decode.split("\r\n")
del result[-1]
result_float = np.array(result,dtype=float)
x = range(0,401)  
plt.plot(x, result_float)

#%%
sf=HP.freq_start
stf=HP.freq_stop
bw=HP.bw_res
st=HP.sweep_time
npts=401

# data saving
with open('Rx_B_All_off.txt', 'w') as f:
    f.write(f'# Start frequency = {sf} Hz'+'\n'+f'# stop frequency = {stf} Hz'+'\n'+f'# Bandwidth = {bw} Hz'+'\n'+f'# Sweep time = {st} s'+'\n')
    for item in result:
        f.write(f'{item}'+'\n')
