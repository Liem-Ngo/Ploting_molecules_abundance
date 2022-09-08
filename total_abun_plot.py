from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
import matplotlib.colors as colors
from scipy.ndimage import gaussian_filter
import matplotlib.patches as mpatches
from matplotlib.colors import LogNorm
import os

output_csv='csv_output'

list_lum=[
    'zeta_22_1',
    'zeta_22_10',
    'zeta_22_50',
    'zeta_22_100'
]
plt.rcParams.update({'font.size': 18.0})

vmax_=1e-4
vmin_=1e-9
v_range_=vmax_/10.

sig=10
#list_mol=['S']#'H+','C+','H3+','HE+']#,'JSO2','JOCS','JSO','JH2S','JH2CS','JCS']
list_mol=["SO2",'Td']#,'OCS','SO','CS','H2S','H2CS']

for mol in list_mol:
    count_=0
    #for list_lum in list_list_lum:
    print (list_lum)
    count_+=1
    count=0
    fig, axs = plt.subplots(2,2, facecolor='w', edgecolor='k',figsize=(15,15))
    #fig.subplots_adjust(hspace = .0, wspace=0.35)
    cbar_ax = fig.add_axes([0.91, 0.1, 0.02, 0.78])

    axs = axs.ravel()
    for lum in list_lum:
        #for mol in list_mol:
        #mol='SO2'
        fig = plt.figure()
        li=lum.split('_')
        csv_file=os.path.join(output_csv,'{}_{}.csv'.format(mol,lum))
        z_data = pd.read_csv(csv_file,header=None)
        z = z_data.values
        data_=10**z
        data=data_#-data_17)
        #data = gaussian_filter(data, sigma=sig)
        #csv_file_td=os.path.join(output_csv,'{}_{}.csv'.format('Td',lum))
        #z_data_td = pd.read_csv(csv_file_td,header=None)
        #z_td = z_data_td.values
        #data_td=10**z_td
        #td=data_td#-data_17)
        if mol=='Td':
            cset =axs[count].imshow(data,norm=colors.LogNorm(vmin=1e1, vmax=1e3), origin='lower', cmap='coolwarm',extent=[0,1000,0,1000],interpolation='none',alpha=0.8)
        else:
            cset =axs[count].imshow(data,norm=colors.LogNorm(vmin=vmin_, vmax=vmax_), origin='lower', cmap='rainbow',extent=[0,1000,0,1000],interpolation='none',alpha=0.8)

        #plt.colorbar(cset, ax = axs[count])
        x_ticktext= ['$10^0$', '$10^1$', '$10^2$', '$10^3$', '$10^4$', '$10^5$', '$10^6$']
        x_tickvals= np.linspace(0,1000,7)
        y_ticktext= ['0.1','4.0','8.0','12.0','16.0','20.0', '24.0', '28.0','32.0', '36.0', '40.0']
        y_tickvals= np.linspace(0,1000,11)
        axs[count].set_xticks(x_tickvals)
        axs[count].set_xticklabels(x_ticktext)
        axs[count].set_yticks(y_tickvals)
        axs[count].set_yticklabels(y_ticktext)
        if count ==2:
            axs[count].set_ylabel('Distance*1e3 (AU)')
            axs[count].set_xlabel('Time (years)')
        str=r'$\zeta_{{CR}}= {}\times 1.3.10^{{-17}}$'.format(li[-1])
        #str=r'$\rm{{Inner\ density}} = {}\ \rm{{ cm}}^{{-3}}$'.format(li[4])
        #str=r'Plummer function ($\eta$) = {}'.format(li[-1])
        #str=r'Plummer function $\eta$= {}'.format(li[-1])
        axs[count].set_title(str)#+r' $\frac{{rate_{{for}}}}{{rate_{{des}}}}$')
    #plt.close(fig)
        count+=1
        plt.close()
    #if count_==1:
        #str=r'$ \frac{{d_{{{}}} - d_{{1e7}}   }}{{d_{{1e7}}}}$'.format(li[-3])
    #if count_==2:
        #str=r'$ \frac{{\eta_{{{}}} - \eta_{{1.0}}   }}{{\eta_{{1.0}}}}$'.format(li[-1])
    #if count_==3:
        #str=r'$ \frac{{L_{{{}}} - L_{{1e+05}}   }}{{L_{{1e+05}}}}$'.format(li[0])
    #if count_==4:
        #str=r'$ \frac{{\zeta_{{{}}} - \zeta_{{1e-17}}   }}{{\zeta_{{1e-17}}}}$'.format(li[-1])
    cbar=fig.colorbar(cset, cax=cbar_ax)
    if mol !="Td":
        cbar.ax.set_ylabel(r'Relative abundances ($n_{{{}}}/n_H$)'.format(mol), rotation=90)
    elif mol == "Td":
        str=r'Temperature (K)'
        cbar.ax.set_ylabel(r'Temperature (K)', rotation=90)

    #cbar.ax.set_ylabel(r'Relative abundances ($n_{{{}}}/n_H$)'.format(mol), rotation=90)
    #str='$\\frac{(zeta = )} / {}$'
    #plt.suptitle(str)
    plt.savefig('{}.png'.format(mol),dpi=300)
    #plt.show()
