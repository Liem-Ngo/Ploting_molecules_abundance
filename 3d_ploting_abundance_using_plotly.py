import plotly.graph_objects as go
import numpy as np
import pandas as pd
import os

lum='zeta_22_1'
#for lum in list_lum:
csv_file='SO2_{}.csv'.format(lum)
csv_temper='Td_{}.csv'.format(lum)

#html_name=lum+'_temperature.html'
html_name=csv_file+'_.html'

#csv_file='file_so2_ocs_{}.csv'.format(lum)
mycolors_a = pd.read_csv(csv_temper)
z_data = pd.read_csv(csv_file)
z = z_data.values

'''
csv_file_ref=os.path.join('{}_{}.csv'.format('SO2',lum))
z_data_ref = pd.read_csv(csv_file_ref,header=None)
z_ref = z_data_ref.values
data_ref=10**z_ref



csv_file=os.path.join('{}_{}.csv'.format('OCS',lum))
z_dat = pd.read_csv(csv_file,header=None)
z_ocs = z_dat.values
data_=10**z_ocs
data=data_ref/data_#data_/data_ref

'''

#z = data

sh_0, sh_1 = z.shape
x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
fig = go.Figure(data=[go.Surface(z=z_data.values)])
N = 50
arrr= np.linspace(0,100,4)
aaa=arrr.astype('str')
#fig.update_layout()
fig.update_layout(title='{}'.format(lum), autosize=True,scene = dict(
                    xaxis_title='Time (years)',
                    yaxis_title='Distance (1e3 AU)',
                    xaxis = dict(
                            ticktext= ['1', '1e1', '1e2', '1e3', '1e4', '1e5', '1e6'],
                            tickvals= np.linspace(0,1000,7)
                            ),
                    yaxis = dict(
                    ticktext= ['0.5','4.0','8.0','12.0','16.0','20.0', '24.0', '28.0','32.0', '36.0', '40.0'],
                    tickvals= np.linspace(0,1000,11)
                        ),
                    zaxis_title='log10[n_H/n_SO2]'),width=600, height=600
                    )




fig.write_html(html_name)

#fig.show()
