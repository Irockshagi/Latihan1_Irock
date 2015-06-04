############################################################################
#function vpu,vpl,vsu,vsl,poro = hash(k1,mu1,k2,mu2)
#HASHV - Hashin-Shtrikman upper and lower bound curves for velocities
#	 as a function of fraction of material 2.
#VP1, VS1, RO1: P and S velocity and density of material 1.
#VP2, VS2, RO2: P and S velocity and density of material 2.
#VPU, VPL, VSU, VSL: Upper and lower bounds on P and S velocities.
#POR: Porosity vector (volume fraction of material 2).
#Assumes material 1 has higher velocity than material 2. If not, then
#upper and lower bounds should be interchanged in the output.
#With no output arguments HASH plots the bounds as a function of porosity
#or fraction of phase 2 material. 
#
# Written by Roy Baroes for Himpunan Ahli Geofisika Indonesia - Irocks
#Jakarta , May 2015
# Modify from T. Mukerji
##############################################################################

import numpy as np
import matplotlib.pyplot as plt
plt.close()

#k1=30.6;
#mu1=35;
#k2=10;
#mu2=15;
#ro1=2.65;
#ro2=1;
def hash(k1,mu1,k2,mu2):
    poro=np.arange(0,1,0.01)
    ro=(1-poro)*ro1+poro*ro2;

    ku=k2+(1-poro)*(k1-k2)*(k2+4*mu1/3)/(k2+4*(mu1/3.)+poro*(k1-k2));
    kl=k2+(1-poro)*(k1-k2)*(k2+4*mu2/3)/(k2+4*(mu2/3.)+poro*(k1-k2));

    fgu=mu1*(9*k1+8*mu1)/(6*(k1+2*mu1));
    fgl=mu2*(9*k2+8*mu2)/(6*(k2+2.*mu2));
    gu=mu2+(mu1-mu2)*(1-poro)*(mu2+fgu)/(mu2+fgu+poro*(mu1-mu2));
    gl=mu2+(mu1-mu2)*(1-poro)*(mu2+fgl)/(mu2+fgl+poro*(mu1-mu2));


    vpu=np.sqrt((ku+(4*gu/3))/ro);
    vpl=np.sqrt((kl+(4*gl/3))/ro);
    vsu=np.sqrt(gu/ro);
    vsl=np.sqrt(gl/ro);

    return vpu,vpl,vsu,vsl,poro


plt.show()