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
from scipy import interpolate
from matplotlib import pyplot as plt

add_='_'

output_csv='csv_output'
output_folder='output_inanna'
list_lum=[
'zeta_22_1',
'zeta_22_10',
'zeta_22_50',
'zeta_22_100']

plt.rcParams.update({'font.size': 18.0})

vmax_=1e-8
vmin_=-vmax_
v_range_=vmax_/1e4

sig=10
#list_mol=['H+','HE+','C+','S','C','HCO+','H2+','H3+']
list_mol=['SO2']

x=np.linspace(500,40000,1000)
user_input_base='{}{}user_input_saptarsy.txt'.format(list_lum[0],add_)
user_input=os.path.join(output_folder,user_input_base)
radi=np.genfromtxt(user_input,usecols = (2,6),skip_header=130,skip_footer=61 )
#densi=ab[:,ii]#ab[:,ii]
f = interpolate.interp1d(radi[:,1], radi[:,0])
x=np.linspace(500,40000,1000)

print(radi[:,1])
dens_inter=f(x)
print(len(dens_inter))

def get_data_re(csv_file):
    z_data = pd.read_csv(csv_file,header=None)
    z = z_data.values
    data_=10**z
    time_inter=np.logspace(0,6,1000)
    data=data_#-data_17)
    for ii in range(2,1000):
        data[:,-ii]=(data[:,-ii]-data[:,-ii-1])/(time_inter[-ii]-time_inter[-ii-1])/31556930
    for ii in range(1000):
        data[ii,:]=data[ii,:]*dens_inter[ii]
    return data



for mol in list_mol:
    count_=0
    #for list_lum in list_list_lum:
    print (list_lum)
    count_+=1
    count=0
    fig, axs = plt.subplots(2,2, facecolor='w', edgecolor='k',figsize=(15,13))
    #fig.subplots_adjust(hspace = .0, wspace=0.35)
    cbar_ax = fig.add_axes([0.89, 0.1, 0.02, 0.78])


    axs = axs.ravel()
    for lum in list_lum:

        fig = plt.figure()
        li=lum.split('_')
        csv_file=os.path.join(output_csv,'{}_{}.csv'.format(mol,lum))

        data=get_data_re(csv_file)
        #data = gaussian_filter(data, sigma=sig)

        cset =axs[count].imshow(data,norm=colors.SymLogNorm(v_range_,vmin=vmin_, vmax=vmax_), origin='lower', cmap='coolwarm',extent=[0,1000,0,1000],interpolation='none',alpha=0.8)
        #axs[count].annotate('R$_{{1}}$', fontsize=15,color='k', xy=(100, 890),xycoords='data', xytext=(0, 0),textcoords='offset points')
        #axs[count].annotate('R$_{{3}}$', fontsize=15,color='k', xy=(900, 890),xycoords='data', xytext=(0, 0),textcoords='offset points')



        #if count==0 :
        #    axs[count].annotate('A$_{{12}}$', fontsize=15,color='k', xy=(900, 90),xycoords='data', xytext=(-58, 20),textcoords='offset points',arrowprops=dict(arrowstyle="->",linewidth = 2.,color = 'k'))
        #    axs[count].annotate('A$_{{11}}$', fontsize=15,color='k', xy=(980, 400),xycoords='data', xytext=(-58, 20),textcoords='offset points',arrowprops=dict(arrowstyle="->",linewidth = 2.,color = 'k'))

        #if count==1:
        #    axs[count].annotate('A$_{{21}}$', fontsize=15,color='k', xy=(980, 400),xycoords='data', xytext=(-58, 20),textcoords='offset points',arrowprops=dict(arrowstyle="->",linewidth = 2.,color = 'k'))
        #    axs[count].annotate('A$_{{22}}$', fontsize=15,color='k', xy=(920, 90),xycoords='data', xytext=(-58, 20),textcoords='offset points',arrowprops=dict(arrowstyle="->",linewidth = 2.,color = 'k'))
        #if count==2:
        #    axs[count].annotate('A$_{{31}}$', fontsize=15,color='k', xy=(980, 400),xycoords='data', xytext=(-58, 20),textcoords='offset points',arrowprops=dict(arrowstyle="->",linewidth = 2.,color = 'k'))
        #    axs[count].annotate('A$_{{32}}$', fontsize=15,color='k', xy=(850, 90),xycoords='data', xytext=(-58, 20),textcoords='offset points',arrowprops=dict(arrowstyle="->",linewidth = 2.,color = 'k'))
        #if count==3:
        #    axs[count].annotate('A$_{{41}}$', fontsize=15,color='k', xy=(980, 400),xycoords='data', xytext=(-58, 20),textcoords='offset points',arrowprops=dict(arrowstyle="->",linewidth = 2.,color = 'k'))
        #    axs[count].annotate('A$_{{42}}$', fontsize=15,color='k', xy=(780, 50),xycoords='data', xytext=(-58, 20),textcoords='offset points',arrowprops=dict(arrowstyle="->",linewidth = 2.,color = 'k'))

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
        str=r'$\zeta_{{CR}}= {}*1.3e-17$'.format(li[-1])
        #str=r'$\rm{{Inner\ density}} = {}\ \rm{{ cm}}^{{-3}}$'.format(li[4])
        #if li[0] !='1.0e+08' :
            #str=r'Total luminosity = 1e6*{} $L_\odot$'.format(li[0])
        #else :
            #str=r'Total luminosity = 1e6 $L_\odot$'

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
    #str=r'Total reaction rate of {}'.format(mol)

    #str='$\\frac{(zeta = )} / {}$'
    #plt.suptitle(str)
    cbar=fig.colorbar(cset, cax=cbar_ax)
    cbar.ax.set_ylabel(r'Reaction rate (cm$^{-3}$s$^{-1}$) or (s$^{-1}$)', rotation=90)
    plt.savefig('Total_rate_{}_zeta.pdf'.format(mol),dpi=300)
