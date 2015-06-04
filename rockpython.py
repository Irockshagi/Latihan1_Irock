# -*- coding: utf-8 -*-
#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from hash import *
from las import LASReader

logdata = LASReader('well_2.las', null_subs=np.nan)
#mengimport library dan membaca data sumur dari las file

#  Hashin -Strikman Bound
k1=36.6;
mu1=45;
k2=2.6;
mu2=0;
ro1=2.65;
ro2=1;
vpu,vpl,vsu,vsl,poro = hash(k1,mu1,k2,mu2)
#mengitung HS Bound curve



# baca curva dari logdata
z =logdata.data['DEPT']
GR = logdata.data['GR']
VP = logdata.data['Vp']
VS = logdata.data['Vs']
NPHI = logdata.data['NPHI']
RHOB = logdata.data['RHOB']

# menghitung nilai porositas dari formula yang diberikan
porositas = (2.65-RHOB)/(2.65-1.05)

#===========Zona Cemented sand========
CmSU=2254.0449
CmSL=2300.6792
CmSU1=np.where(z==CmSU)[0]
CmSU_1=int(CmSU1[0])
CmSU2=np.where(z==CmSL)[0]
CmSU2_1=int(CmSU2[0])

#===========Zona clean sand========
ClSU=2154.0703
ClSL=2164.1289
ClSU1=np.where(z==ClSU)[0]
ClSU_1=int(ClSU1[0])
ClSU2=np.where(z==ClSL)[0]
ClSU2_1=int(ClSU2[0])

#===========Zona shale========
ShlU=2078.0227 
ShlL=2105.1499
ShlU1=np.where(z==ShlU)[0]
ShlU_1=int(ShlU1[0])
ShlU2=np.where(z==ShlL)[0]
ShlU2_1=int(ShlU2[0])

#===========Zona Silty Sand1========
SltS1U=2168.0913
SltS1L=2184.0933
SltS1U1=np.where(z==SltS1U)[0]
SltS1U_1=int(SltS1U1[0])
SltS1U2=np.where(z==SltS1L)[0]
SltS1U2_1=int(SltS1U2[0])

#===========Zona Silty Sand2========
SltS2U=2186.0745
SltS2L=2200.0952
SltS2U1=np.where(z==SltS2U)[0]
SltS2U_1=int(SltS2U1[0])
SltS2U2=np.where(z==SltS2L)[0]
SltS2U2_1=int(SltS2U2[0])

#===========Zona Silty shale========
SiShlU=2143.2500  
SiShlL=2154.0703
SiShlU1=np.where(z==SiShlU)[0]
SiShlU_1=int(SiShlU1[0])
SiShlU2=np.where(z==SiShlL)[0]
SiShlU2_1=int(SiShlU2[0])


#hans Empirical sandstone line
VPhans=5.47-6.94*porositas-2.17*0.05

f1 = plt.figure(1,figsize = (12,8))
f1.suptitle('VP x Porositas dengan HS Bound', fontsize=25)
plt.xlabel('Porositas  '+ r'$[\%]$', fontsize = '12')
plt.ylabel('P-Wave '+ r'$[km/s]$', fontsize = '12')
plt.xlim(0,1)

CmS=plt.scatter(porositas[CmSU_1:CmSU2_1],VP[CmSU_1:CmSU2_1],c ='r',marker='x',hold='on')
ClS=plt.scatter(porositas[ClSU_1:ClSU2_1],VP[ClSU_1:ClSU2_1],c ='y',marker='o')
SH =plt.scatter(porositas[ShlU_1:ShlU2_1],VP[ShlU_1:ShlU2_1],c ='b',marker='+')
SltS1 =plt.scatter(porositas[SltS1U_1:SltS1U2_1],VP[SltS1U_1:SltS1U2_1],c ='g',marker='^')
SltS2 =plt.scatter(porositas[SltS2U_1:SltS2U2_1],VP[SltS2U_1:SltS2U2_1],c ='m',marker='D')
SltSh =plt.scatter(porositas[SiShlU_1:SiShlU2_1],VP[SiShlU_1:SiShlU2_1],c ='k',marker='s')

# plot Hashin -Strikman upper & low Bound
HSU=plt.plot(poro,vpl,color = 'g')
HSL=plt.plot(poro,vpu,color = 'b')
plt.text(0.44,4.6,'HS Upper bound',color = 'b')
plt.text(0.7,1.8,'HS Lower bound',color = 'g')

#Vp Han’s empirical sandstone line
hans=plt.plot(porositas,VPhans,color = 'y')
plt.text(0.1,4.7,'Hans empirical',color = 'y')

plt.grid()
plt.legend((CmS, ClS, SH, SltS1, SltS2, SltSh),
           ('Cemented sand', 'Clean Sand', 'Shale', 'Shilty Sand 1', 'Shilty Sand 2', 'Shilty shale',),
           scatterpoints=10,
           #loc='upper right',
           ncol=3,
           fontsize=12)

plt.show()