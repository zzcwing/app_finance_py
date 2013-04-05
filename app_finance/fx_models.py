# -*- coding: utf-8 -*-
"""
Created on Fri Nov 02 13:01:21 2012

@author: zzcwing
"""
from __future__ import division
import sys
import os
import types

sys.path.append(os.path.join(os.path.dirname(__file__)))
from vm_models import *
a=[1,2,6,5,6]
class sfx(vm):
    # sv 残值, ac 年运营成本, cv 当前可变现价值, sy 可使用年份，ir 年利率
    def sfxiv(self,sv,ac,cv,ir,sy):
        try:
            self.sv=nc().nck(sv)
            self.ac=nc().nck(ac)
            self.cv=nc().nck(cv)
            self.ir=nc().nck(ir)
            self.sy=nc().nck(sy)
            if type(self.sv) is not types.ListType and type(self.cv) is not types.ListType and type(self.sy) is not types.ListType:
                if type(self.ac) is not types.ListType and type(self.ir) is not types.ListType:
                    vir=vm().snpv(1,self.ir,self.sy,1)
#                    print vir
                    afxc=(self.cv+self.ac*vir-vm().sfvf(self.sv,self.ir,self.sy,1))/vir
                    return afxc
                elif type(self.ac) is types.ListType and type(self.ir) is not types.ListType and len(self.ac)==self.sy:
                    vac=vm().snpv(self.ac,self.ir,self.sy,1)
#                    print vac
                    vir=vm().snpv(1,self.ir,self.sy,1)
                    afxc=(self.cv+vac-vm().sfvf(self.sv,self.ir,self.sy,1))/vir
                    return afxc
                elif type(self.ac) is not types.ListType and type(self.ir) is types.ListType and len(self.ir)==self.sy:
                    vsv=vm().sfvf(self.sv,self.ir[-1],self.sy,1)
                    vac=vm().snpv(self.ac,self.ir,self.sy,1)
                    vir=vm().snpv(1,self.ir,self.sy,1)
#                    print vac,vir,vsv
                    afxc=(self.cv+vac-vsv)/vir
                    return afxc
                elif type(self.ac) is types.ListType and type(self.ir) is types.ListType and len(self.ir)==self.sy:
                    vsv=vm().sfvf(self.sv,self.ir[-1],self.sy,1)
                    vac=vm().snpv(self.ac,self.ir,self.sy,1)
                    vir=vm().snpv(1,self.ir,self.sy,1)
#                    print vac,vir,vsv
                    afxc=(self.cv+vac-vsv)/vir
                    return afxc
                else:
                    print 'not correct type'
                    quit()
            else:
                print 'not correct type'
                quit()
        except:
            print 'not correct number type'
class mfx(sfx):
    def mfxiv(self,sv,ac,cv,ir,sy):
        try:
            self.sv=nc().nck(sv)
            self.ac=nc().nck(ac)
            self.cv=nc().nck(cv)
            self.ir=nc().nck(ir)
            self.sy=nc().nck(sy)
            if type(self.sv) is types.ListType and type(self.cv) is types.ListType and type(self.sy) is types.ListType and type(self.ac) is types.ListType and len(self.sv)==len(self.sy)==len(self.cv)==len(self.ac):
                mfivlist=[]
                for ict in range(len(self.sv)):
                    mfivlist.append(sfx().sfxiv(self.sv[ict],self.ac[ict],self.cv[ict],self.ir,self.sy[ict]))
                return mfivlist
            else:
                print 'list of number maybe wrong '
                quit()
        except:
            print 'not correct number type,sv,ac,sy,cv must be list type'
            quit()
if __name__=='__main__':
    fx=mfx()
    print fx.mfxiv([200,300],[700,400],[600,2400],0.15,[6,10])
    