# -*- coding: utf-8 -*-
"""
Created on Fri Apr 05 10:16:29 2013

@author: zzcwing
"""
from __future__ import division
import types
class income_tex:
    texrid={}
    qzd=0
    jd=0
    def __init__(self):
        #初始化纳税层级
        self.texrid={0:[0,0,0],1500:[0.03,0,1],4500:[0.1,105,2],9000:[0.2,555,3],35000:[0.25,1005,4]\
                ,55000:[0.30,2755,5],80000:[0.35,5505,6],80001:[0.45,13505,7]}
        #个税起征点
        self.qzd=3500
        #税收筹划的精度（迭代步长）
        self.jd=100
    def numbercheck(self,data): #判断是否数字类型
        try:        
            #self.data=data
#            print self.data
            if type(data) is types.IntType:
                return data
            elif type(data) is types.LongType:
                return data
            elif type(data) is types.FloatType:
                return data
            elif type(data) is types.ComplexType:
                return data
            else:
                print 'wrong type in float number---in position def numbercheck'
                quit()
        except:
            print 'wrong type contains----in position def numbercheck'
            quit()
    def at(self,tqzd): #根据应纳税所得额，确定使用哪一档税率
        res=[]
        if tqzd<=0:
            res=self.texrid[0]
        elif tqzd>0 and tqzd<=1500:
            res=self.texrid[1500]
        elif tqzd>1500 and tqzd<=4500:
            res=self.texrid[4500]
        elif tqzd>4500 and tqzd<=9000:
            res=self.texrid[9000]
        elif tqzd>9000 and tqzd<=35000:
            res=self.texrid[35000]
        elif tqzd>35000 and tqzd<=55000:
            res=self.texrid[55000]
        elif tqzd>55000 and tqzd<=80000:
            res=self.texrid[80000]
        elif tqzd>80000:
            res=self.texrid[80001]
        return res
        
    def mpt(self,mbit):
        atp=[]
        tex_mpt=0
        chbit=self.numbercheck(mbit)
        tqzd=chbit-self.qzd #应纳税所得额=应纳税收入-起征点（应纳税收入=总税前收入-可税前扣除项目（三险一金））
        atp=self.at(tqzd)
        tex_mpt=round(tqzd*atp[0]-atp[1],2)
        return tex_mpt
        
    def ypt(self,ybit,mbit):
        chybit=self.numbercheck(ybit)
        chmbit=self.numbercheck(mbit)
        if chmbit<self.qzd:
            tqzd=chybit-(self.qzd-chmbit)
        else:
            tqzd=chybit
        atp=self.at(round(tqzd/12,2))
        
        return round(tqzd*atp[0]-atp[1],2)
        
    #tic 年总税前收入,yf1 已发薪资的月薪，
    #ys 已发月数，yk 每月可税前扣除的部分(三险一金总额)，yf2 年终奖发放当月的月薪（已减可扣除部分）  
    #由于实际当年的年终奖发放是在次年的1月或者2月（农历过年前），年终奖发放月的月薪按照次年1月或者2月的月薪作为参考
    #同样对于当年做税收筹划时，也是在当年的1月或者2月，所以可能已经发放1-2个月工资，实际筹划月份为10-11个月     
    #说明一下应扣除数的问题，一般而言主要为三险一金，理论上三险一金是税前工资总额的比例数，但实务上每个地区的比率和征收方式各有千秋
    #一般而言是按照去年平均工资作为扣除基数，并非按照本年的应发工资，杭州地区为7月份统一调整本年的扣除基数    
    def bptr(self,tic,yf1,ys,yk,yf2): 
        ctic=self.numbercheck(tic)
        cyf1=self.numbercheck(yf1)
        cys=self.numbercheck(ys)
        cyk=self.numbercheck(yk)
        cyf2=self.numbercheck(yf2)
        mic=0
        if cys>=12 or cyf1>=tic or cyf2>=tic or cyk>cyf1 or cyk>cyf2:
            print "variable is not correct!---in position def bptr"
            return 0;
        wctic=ctic-cys*cyf1 #全年合计收入减去剩余部分
        redict={} #税收合计作为Key，相应的月薪、年终奖、可支配收入作为value
        lr=[]
#        mt=[] #存储所有税前月收入
#        yt=[] #存储所有税前年终奖
#        tt=[] #存储所有合计缴税
        gp=0 #存储所有可支配收入
        ts=0 #存数全年税收
        while True:
            if mic>=wctic:
                break
            else:
                yic=round(wctic-mic*(12-cys),2)
                tmic=mic-cyk
                ts=self.mpt(tmic)*(12-cys)+self.ypt(yic,cyf2)+self.mpt(cyf1-cyk)*cys
                #gp=tmic*(12-cys)+yic+(cyf1-cyk)*cys-ts
                gp=ctic-12*cyk-ts
                lr.append(ts)
                redict[ts]=[mic,yic,ts,gp]
                
                mic+=self.jd
        return redict[min(lr)]
        
if __name__=="__main__":
    it=income_tex()
    dig={}
    
    print u'扣除三险一金后月薪40500，应缴纳个税： ',it.mpt(40500)
    print u'年终奖40500，发放当月月薪30000，应缴纳年终奖个税',it.ypt(405000,30000)
    print '-------------------------------------------------------'
    print u'年薪450000，已发20000月薪，已发月数1个月，每月预计应扣三险一金3650，本年年终奖在次年发放月的月薪为20000'
    print u'以上情况下，本年最佳税收筹划组合'
    
    dtg=it.bptr(450000,20000,1,3650,20000)
    print u"税赋最低的月薪",dtg[0]
    print u"税赋最低的年终奖",dtg[1]
    print u"总体最低税赋为",dtg[2]
    print '-------------------------------------------------------'
        