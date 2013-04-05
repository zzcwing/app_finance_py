# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 20:03:49 2012

@author: zzcwing
"""

#value of money models
from __future__ import division
import types
#import sys
class nc:
    def numbercheck(self,data):
        try:
            self.data=data
#            print self.data
            if type(self.data) is types.IntType:
                return self.data
            elif type(self.data) is types.LongType:
                return self.data
            elif type(self.data) is types.FloatType:
                return self.data
            elif type(self.data) is types.DoubleType:
                return self.data
            elif type(self.data) is types.ComplexType:
                return self.data
            else:
                print 'wrong type in single number'
                quit()
        except:
            print 'wrong number type contains'
            quit()
    def nck(self,inum):
        try:
            self.inum=inum
            if type(self.inum) is types.ListType:
                cnum=[]
                for it in self.inum:
#                    print it
                    if type(it) is types.ListType:
                        cnum.append(nc().nck(it))
                    else:
                        cnum.append(nc().numbercheck(it))
                return cnum
            else:
                cnum=nc().numbercheck(self.inum)
                return cnum
        except:
            print 'the type of input data is wrong'
            quit()
class vm:
    def spvs(self,prin,ir,n,isir): #单利
        try:
            self.prin=prin
            self.ir=ir
            self.n=n
            self.isir=isir
            if not self.isir:#isir=0 输出终值，#isir=1 输出利息
                if type(self.prin) is types.ListType:
                    f=[]
                    for it in self.prin:
                        f.append(it*(1+self.ir)*self.n)
                    
                else:
                    f=self.prin*(1+self.ir)*self.n
            else:
                if type(self.prin) is types.ListType:
                    f=[]
                    for it in self.prin:
                        f.append(it*self.ir*self.n)
                else:
                    f=self.prin*self.ir*self.n
            return f
        except TypeError:
            print 'must be number'
    def spvf(self,prin,ir,n,isir):#复利
        try:
            self.prin=prin
            self.ir=ir
            self.n=n
            self.isir=isir            
            if not self.isir:#isir=0 输出终值，#isir=1 输出利息
                if type(self.prin) is types.ListType:
                    f=[]
                    for it in self.prin:
                        f.append(it*(1+self.ir)**self.n)
                else:
                    f=self.prin*(1+self.ir)**self.n
            else:
                if type(self.prin) is types.ListType:
                    f=[]
                    for it in self.prin:
                        f.append(it*(1+self.ir)**self.n-it)
                else:
                    f=self.prin*(1+self.ir)**self.n-self.prin
            return f
        except TypeError:
            print 'must be number'
            
    def sfvf(self,prin,ir,n,isir):#单项金额的现值
        try:
            self.prin=prin
            self.ir=ir
            self.n=n
            self.isir=isir            
            if not self.isir:#isir=0 输出期初现值，#isir=1 输出期末现值
                if type(self.prin) is types.ListType:
                    f=[]
                    for it in self.prin:
                        f.append((it/(1+self.ir)**(self.n-1)))
                else:
                    f=self.prin/((1+self.ir)**(self.n-1))
            else:
                if type(self.prin) is types.ListType:
                    f=[]
                    for it in self.prin:
                        f.append(it/((1+self.ir)**self.n))
                else:
                    f=self.prin/((1+self.ir)**self.n)
            return f
        except TypeError:
            print 'must be number'
            

    def lpvf(self,prin,ir,n,isir=0):
        try:
            self.prin=prin
            self.ir=ir
            self.n=n
            self.isir=isir
            if not self.isir:#isir=1 普通年金终值 isir=0 预付年金终值（期初应付年金终值）
                if (type(self.ir) is types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n==len(self.ir)):
                    f=0
                    for ipp in range(len(self.prin)):
                        f=(self.prin[ipp]+f)*(1+self.ir[ipp])
                    l=f-sum(self.prin)
                elif (type(self.ir) is not types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n):
                    f=0
                    for ipp in range(len(self.prin)):
                        f=(self.prin[ipp]+f)*(1+self.ir)
                    l=f-sum(self.prin)
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is types.ListType) and (len(self.ir)==self.n):
                    f=0
                    for irr in range(len(self.ir)):
                        f=(self.prin+f)*(1+self.ir[irr])
                    l=f-self.prin*self.n
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is not types.ListType):
                    f=0
                    for inn in range(self.n):
                        f=(self.prin+f)*(1+self.ir)
                    l=f-self.prin*self.n
                else:
                    print 'var is not correct'
                    f=0
                    l=0
            else:
                if (type(self.ir) is types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n==len(self.ir)):
                    f=0
                    for ipp in range(len(self.prin)):
                        if ipp==0:
                            f=self.prin[ipp]
                        else:
                            f=self.prin[ipp]+f*(1+self.ir[ipp-1])
                    l=f-sum(self.prin)
                elif (type(self.ir) is not types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n):
                    f=0
                    for ipp in range(len(self.prin)):
                        f=self.prin[ipp]+f*(1+self.ir)
                    l=f-sum(self.prin)
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is types.ListType) and (len(self.ir)==self.n):
                    f=0
                    for irr in range(len(self.ir)):
                        if irr==0:
                            f=self.prin
                        else:
                            f=self.prin+f*(1+self.ir[irr-1])
                    l=f-self.prin*self.n
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is not types.ListType):
                    f=0
                    for inn in range(self.n):
                        f=self.prin+f*(1+self.ir)
                    l=f-self.prin*self.n
                else:
                    print 'var is not correct'
                    f=0
                    l=0
            return dict((['pvf',f],['interest',l]))
        except TypeError:
            print 'must be number'
    
    def lfvf(self,prin,ir,n,isir):
        try:
            self.prin=prin
            self.ir=ir
            self.n=n
            self.isir=isir
            if not self.isir: #isir=1 普通年金现值 isir=0 预付年金现值（期初应付年金现值）
                if (type(self.ir) is types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n==len(self.ir)):
                    f=0
                    for ipp in range(len(self.prin)):
                        if ipp==0:
                            f=self.prin[ipp]
                        else:
                            f=self.prin[ipp]+f/(1+self.ir[ipp-1])
                elif (type(self.ir) is not types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n):
                    f=0
                    for ipp in range(len(self.prin)):
                        f=self.prin[ipp]+f/(1+self.ir)
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is types.ListType) and (len(self.ir)==self.n):
                    f=0
                    for irr in range(len(self.ir)):
                        if irr==0:
                            f=self.prin
                        else:
                            f=self.prin+f/(1+self.ir[irr-1])
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is not types.ListType):
                    f=0
                    for inn in range(self.n):
                        f=self.prin+f/(1+self.ir)
                else:
                    print 'var is not correct'
                    f=0
            else:
                if (type(self.ir) is types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n==len(self.ir)):
                    f=0
                    for ipp in range(len(self.prin)):
                        f=(self.prin[ipp]+f)/(1+self.ir[ipp])
                elif (type(self.ir) is not types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n):
                    f=0
                    for ipp in range(len(self.prin)):
                        f=(self.prin[ipp]+f)/(1+self.ir)
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is types.ListType) and (len(self.ir)==self.n):
                    f=0
                    for irr in range(len(self.ir)):
                        f=(self.prin+f)/(1+self.ir[irr])
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is not types.ListType):
                    f=0
                    for inn in range(self.n):
                        f=(self.prin+f)/(1+self.ir)
                else:
                    print 'var is not correct'
                    f=0
            return f
        except TypeError:
            print 'must be number'
    def snpv(self,prin,ir,n,isir):
        try:
            self.prin=prin
            self.ir=ir
            self.n=n
            self.isir=isir
            if not self.isir: #isir=1 期末收回净现金流 isir=0 期初收回净现金流
                if (type(self.ir) is types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n==len(self.ir)):
                    f=[]
                    for ipp in range(len(self.prin)):
                        if ipp==0:
                            f.append(self.prin[ipp])
                        else:
                            f.append(self.prin[ipp]/(1+self.ir[ipp-1])**(ipp))
                elif (type(self.ir) is not types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n):
                    f=[]
                    for ipp in range(len(self.prin)):
                        f.append(self.prin[ipp]/(1+self.ir)**(ipp))
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is types.ListType) and (len(self.ir)==self.n):
                    f=[]
                    for irr in range(len(self.ir)):
                        if irr==0:
                            f.append(self.prin)
                        else:
                            f.append(self.prin/(1+self.ir[irr-1]**(irr)))
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is not types.ListType):
                    f=[]
                    for inn in range(self.n):
                        f.append(self.prin/(1+self.ir)**inn)
                else:
                    print 'var is not correct'
                    f=[0]
            else:
                if (type(self.ir) is types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n==len(self.ir)):
                    f=[]
                    for ipp in range(len(self.prin)):
                        f.append(self.prin[ipp]/(1+self.ir[ipp])**(ipp+1))
#                    print f
                elif (type(self.ir) is not types.ListType) and (type(self.prin) is types.ListType) and (len(self.prin)==self.n):
                    f=[]
                    for ipp in range(len(self.prin)):
                        f.append(self.prin[ipp]/(1+self.ir)**(ipp+1))
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is types.ListType) and (len(self.ir)==self.n):
                    f=[]
                    for irr in range(len(self.ir)):
                        f.append(self.prin/(1+self.ir[irr])**(irr+1))
                elif (type(self.prin) is not types.ListType) and (type(self.ir) is not types.ListType):
                    f=[]
                    for inn in range(self.n):
                        f.append(self.prin/(1+self.ir)**(inn+1))
                else:
                    print 'var is not correct'
                    f=[0]
            return sum(f)
        except TypeError:
            print 'must be number'
            
class iv(vm):
    def ivbond(self,bv,prin,ir,n,isir):
        
        self.bv=bv
        fbond=vm.snpv(self,prin,ir,n,isir=1)
        try:
            if type(self.bv) is not types.ListType:
                if type(self.ir) is types.ListType:
                    print self.ir
                    fvbond=fbond+self.bv/((self.ir[-1]+1)**self.n)
                else:
                    print self.ir
                    fvbond=fbond+self.bv/((self.ir+1)**self.n)
            else:
                if type(self.ir) is types.ListType:
                    print self.ir
                    fvbond=[]
                    for ifv in self.bv:
                        fvbond.append(fbond+ifv/((self.ir[-1]+1)**self.n))
                else:
                    print self.ir
                    fvbond=[]
                    for ifv in self.bv:
                        fvbond.append(fbond+ifv/((self.ir+1)**self.n))              
            return fvbond
        except TypeError:
            print 'wrong var type'
            
    def ivstock(self,hd,gp,bv,prin,ir,n,isir):
        try:
            self.hd=hd
            self.gp=gp
            self.bv=bv
            if self.hd==0:
                self.prin=prin
                self.ir=ir
                self.isir=isir
                
                if type(self.gp) is not types.ListType and type(self.prin) is not types.ListType and type(self.ir) is not types.ListType:
                    fvstock=self.prin*(1+self.gp)/(self.ir-self.gp)
                elif type(self.gp) is types.ListType and type(self.prin) is not types.ListType and type(self.ir) is not types.ListType:
                    fvstock=[]
                    for fvs in self.gp:
                        fvstock.append(self.prin*(1+fvs)/(self.ir-fvs))
                elif type(self.gp) is not types.ListType and type(self.prin) is types.ListType and type(self.ir) is not types.ListType:
                    fvstock=[]
                    for fvs in self.prin:
                        fvstock.append(fvs*(1+self.gp)/(self.ir-self.gp))
                elif type(self.gp) is not types.ListType and type(self.prin) is not types.ListType and type(self.ir) is types.ListType:
                    fvstock=[]
                    for fvs in self.ir:
                        fvstock.append(self.prin*(1+self.gp)/(fvs-self.gp))
                else:
                    print 'wrong var'
                    fvstock=0
            else:
                self.prin=prin
                self.n=n
                if type(self.gp) is types.ListType and type(self.prin) is types.ListType:
                    print 'wrong var'
                elif type(self.gp) is types.ListType and type(self.prin) is not types.ListType and (len(self.gp)==self.n): 
                    dprin=[]
                    for dpr in range(len(self.gp)):
                        dprin.append(self.prin*(1+self.gp[dpr])**(dpr+1))
                elif type(self.gp) is not types.ListType and type(self.prin) is not types.ListType:
                    dprin=[]
                    for dpr in range(self.n):
                        dprin.append(self.prin*(self.gp+1)**(dpr+1))
                    print dprin,self.bv,ir,self.n
                else:
                    print 'prin and dp should just one is list'
                fvstock=iv.ivbond(self,self.bv,dprin,ir,self.n,isir=1)
            return fvstock
        except TypeError:
            print 'wrong type'
        except ZeroDivisionError:
            print 'ir-gp should not equal to zero'
            
    def dnpv(self,cashin,cashout,ir,n,isir):
        try:
            self.cashin=cashin
            self.cashout=cashout
            self.n=n
            if type(self.cashin) is types.ListType and type(self.cashout) is types.ListType and (len(self.cashin)==self.n==len(self.cashout)):
                dnpvinout=[]            
                for ipv in range(len(self.cashin)):
                    dnpvinout.append(self.cashin[ipv]-self.cashout[ipv])
            elif type(self.cashin) is not types.ListType and type(self.cashout) is types.ListType and self.n==len(self.cashout):
                dnpvinout=[]
                for ipv in range(len(self.cashout)):
                    dnpvinout.append(self.cashin-self.cashout[ipv])
            elif type(self.cashin) is types.ListType and type(self.cashout) is not types.ListType and len(self.cashin)==self.n:
                dnpvinout=[]
                for ipv in range(len(self.cashin)):
                    dnpvinout.append(self.cashin[ipv]-self.cashout)
            elif type(self.cashin) is not types.ListType and type(self.cashout) is not types.ListType:
                dnpvinout=[]
                for ipv in range(self.n):
                    dnpvinout.append(self.cashin-self.cashout)
            else:
                print 'cashin cashout is not correct type or the length of list is not equal to n '
                dnpvinout=0
#            print dnpvinout
            npv=vm.snpv(self,dnpvinout,ir,self.n,isir=1)
            return dict((['npv',npv],['npv_record',dnpvinout]))
        except:
            print 'bad value'
    def pi(self,cashin,cashout,ir,n,isir):
        try:
            self.cashin=cashin
            self.cashout=cashout
            self.n=n
            if type(self.cashin) is types.ListType and type(self.cashout) is types.ListType and (len(self.cashin)!=self.n or len(self.cashin)!=len(self.cashout) or len(self.cashout)!=self.n):
                print 'cashin cashout is not correct type or the length of list is not equal to n '
                pi=0
            else:
#            print dnpvinout
                npvin=vm.snpv(self,self.cashin,ir,self.n,isir=1)
                npvout=vm.snpv(self,self.cashout,ir,self.n,isir=1)
                pi=npvin/npvout
            return pi
        except:
            print 'can not caculate pi'
            
    def irr(self,cashin,cashout,ir,n,isir):
        try:
            self.ir=ir
            self.cashin=cashin
            self.cashout=cashout
            self.n=n
            if type(self.cashin) is types.ListType and type(self.cashout) is types.ListType and (len(self.cashin)!=self.n or len(self.cashin)!=len(self.cashout) or len(self.cashout)!=self.n):
                print 'cashin cashout is not correct type or the length of list is not equal to n '
            else:
                irr=0
                ird=True
                while ird:
                    npvin=vm.snpv(self,self.cashin,irr,self.n,isir=1)
                    npvout=vm.snpv(self,self.cashout,irr,self.n,isir=1)
                    npvinout=npvin-npvout
                    if npvinout <0.001:
                        print 'irr is %f ' % irr
                        return irr
                        break
                    irr=irr+0.001
                    if irr>1:
                        ird=False
                        print 'can not find irr'
                        return 0
                        break            
        except:
            print 'can not caculate irr'
            
    def ivd(self,cashin,cashout,ir,n,isir):
        try:
#            self.cashin=cashin
#            self.cashout=cashout
#            self.n=n
            ivd_npv=iv.dnpv(self,cashin,cashout,ir,n,isir)['npv_record']
            vd=0
            for ivs in range(len(ivd_npv)):
                vd=vd+ivd_npv[ivs]
                if vd>=0:
                    ivd=ivs+(-sum(ivd_npv[:ivs])/ivd_npv[ivs])
                    print 'the investment period is %f' % ivd
                    return ivd
                    break
            print 'can not caculate inn'
            return 0
        except:
            print 'error inn'
if __name__=='__main__':
    a=[[1,2],[3,4],5,6]
#    ck=nc()
##    print a
#    print ck.nck(a)
##    s=vm()
##    print s.snpv(1000,[0.1,0.11,0.09,0.08,0.12],5,1)
#    p=iv()
##    print p.ivbond(10000,1000,0.2,5,1)
#    print p.ivd([1000,1200,1300,1400,1500],[2000,600,700,900,1000],[0.11,0.12,0.10,0.09,0.08],5,1)
#    p=vm()
#    print p.lfvf(1,0.15,6,1)