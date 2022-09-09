import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import os
import pandas as pd
from scipy import interpolate


list_mole=['Td','nH','SO2','OCS','H2S','H2CS','CS']

#add_="__22_z_"
#add_="_"
add_="__22_z_"

list_ratio_mole=[]
list_lum=[
    'zeta_22_1',
    'zeta_22_10',
    'zeta_22_50',
    'zeta_22_100'
    ]



output_folder='output_inanna'
output_csv='csv_output'
if not os.path.exists(output_csv):
	os.mkdir(output_csv)
abun_folder='abundance'
if not os.path.exists(abun_folder):
	os.mkdir(abun_folder)

x=np.linspace(500,40000,1000)
li=list_lum[0].split('_')
if li[0]=='zeta'or li[0]=='LMC':
    add_="_"
#abun='{}__22_z_zone_1_time_evol_rel_abun_all_spcs.txt'.format(list_lum[0])
abun='{}{}zone_1_time_evol_rel_abun_all_spcs.txt'.format(list_lum[0],add_)

#zeta_22_1_zone_1_time_evol_rel_abun_all_spcs.txt
file_abun=os.path.join(output_folder,abun)
name_mole=np.genfromtxt(file_abun,skip_footer=81, dtype='str')
#print (name_mole)
time_inter=np.logspace(0,6,1000)
index=np.where(name_mole == 'Time_in')
print(index[0][0])
for lum in list_lum:
    li=lum.split('_')
    if li[0]=='zeta'or li[0]=='LMC':
        add_="_"
    for mole in list_mole:
        split_mole=mole.split('_')
        #print(mole,split_mole,len(split_mole))

        if len(split_mole)==1:
            abun_name='{}_{}.txt'.format(mole,lum)
            abun_file=os.path.join(abun_folder,abun_name)
            gg=open(abun_file,'w')
            print('bla')
            for i in range(1,23):
                index_=np.where(name_mole == mole)
                index_mole=index_[0][0]
                abun='{}{}zone_{}_time_evol_rel_abun_all_spcs.txt'.format(lum,add_,i)
                #abun='{}__22_z_zone_{}_time_evol_rel_abun_all_spcs.txt'.format(lum,i)

                file_abun=os.path.join(output_folder,abun)
                e=np.genfromtxt(file_abun,skip_header=2, dtype='float')
                ee=e[:,index_mole]
                time_out=e[:,1]/31556930
                print('{:e}'.format(ee[-1]))
                ff = interpolate.interp1d(time_out, ee)
                mole_evol=ff(time_inter)
                #print(mole_evol.shape)

                for j in range(len(mole_evol)):
                    gg.write('{} '.format(mole_evol[j]))
                gg.write('\n')
            gg.close()

        elif len(split_mole)==2:
            abun_name='{}_{}.txt'.format(mole,lum)
            abun_file=os.path.join(abun_folder,abun_name)
            gg=open(abun_file,'w')
            #gg=open('{}/{}_{}.txt'.format(abun_folder,mole,lum),'w')
            for i in range(1,23):
                ind=mole.split('_')
                index_1=np.where(name_mole == ind[0])
                index_2=np.where(name_mole == ind[1])

                index_mole_1=index_1[0][0]
                index_mole_2=index_2[0][0]

                abun='{}{}zone_{}_time_evol_rel_abun_all_spcs.txt'.format(lum,add_,i)
                #abun='{}__22_z_zone_{}_time_evol_rel_abun_all_spcs.txt'.format(lum,i)

                file_abun=os.path.join(output_folder,abun)
                e=np.genfromtxt(file_abun,skip_header=2, dtype='float')
                ee=e[:,index_mole_1]/e[:,index_mole_2]
                time_out=e[:,1]/31556930
                #print(time_out)
                ff = interpolate.interp1d(time_out, ee)
                mole_evol=ff(time_inter)
                #print(mole_evol.shape)

                for j in range(len(mole_evol)):
                    gg.write('{} '.format(mole_evol[j]))
                gg.write('\n')
            gg.close()

        abundance_input=os.path.join(abun_file)
        ab=np.loadtxt(abundance_input)
        blabla=[]
        #print(len(ab[0,:]))
        for ii in range(len(ab[0,:])):
            #user_input_base='{}__22_z_user_input_saptarsy.txt'.format(lum)
            user_input_base='{}{}user_input_saptarsy.txt'.format(lum,add_)
            user_input=os.path.join(output_folder,user_input_base)
            radi=np.genfromtxt(user_input,usecols = (6),skip_header=130,skip_footer=61 )
            zone=ab[:,ii]#ab[:,ii]
            f = interpolate.interp1d(radi, zone)
            zone=f(x)
            #print(ii,zone)
            blabla.append(zone)
            radi=x
        arr = np.array(blabla)
        csv_name=os.path.join(output_csv,'{}_{}.csv'.format(mole,lum))
        #print()
        pd.DataFrame(np.log10(arr.T)).to_csv("{}".format(csv_name), header=None, index=None)
