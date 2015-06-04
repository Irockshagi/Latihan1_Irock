import numpy as np


def hashb(k1,mu1,k2,mu2,ro1,ro2):

    por=np.arange(0,1,0.01)
    por[0]=0.0000001
    ro=(1-por)*ro1+por*ro2;
    por=np.arange(0,1,0.01)
    por[0]=0.0000001


    ku=k2+(1-por)*(k1-k2)*(k2+4*mu1/3)/(k2+4*(mu1/3.)+por*(k1-k2));
    kl=k2+(1-por)*(k1-k2)*(k2+4*mu2/3)/(k2+4*(mu2/3.)+por*(k1-k2));

    fgu=mu1*(9*k1+8*mu1)/(6*(k1+2*mu1));
    fgl=mu2*(9*k2+8*mu2)/(6*(k2+2.*mu2));
    gu=mu2+(mu1-mu2)*(1-por)*(mu2+fgu)/(mu2+fgu+por*(mu1-mu2));
    gl=mu2+(mu1-mu2)*(1-por)*(mu2+fgl)/(mu2+fgl+por*(mu1-mu2));


    vpu=np.sqrt((ku+(4*gu/3))/ro);
    vpl=np.sqrt((kl+(4*gl/3))/ro);
    vsu=np.sqrt(gu/ro);
    vsl=np.sqrt(gl/ro);

    return vpu,vpl,vsu,vsl,por

