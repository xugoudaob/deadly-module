#deadly1.3.3 by xgdb
import sys
import time
import platform
class DeadlyError(Exception):
    def __init__(self, message ="You met an DeadlyError,which means maybe you are Deadly!"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"

def deadly(t1='Deadly! '):
    t=''
    if type(t1) != str:
        raise DeadlyError("Maybe the programmer could not know which type on the function")
        return
    while t!=t1:
        print('deadly')
        t=input('>>> ')
def deadly_exit():
    deadly()
    sys.exit()
def gua_n(l1,l2,num):
    print("注：每一卦形代表一定的事物。乾代表天，坤代表地，巽（xùn）代表风，震代表雷，坎代表水，离代表火，艮（gèn）代表山，兑代表泽。")
    yaox={'111':"天",'000':'地','001':'雷','100':'山','101':'火','010':'水','011':'泽','110':'风'}
    x=yaox[l1]+yaox[l2]
    print(x,num)

def plus(l1,l2,num):
    i=''
    while i!='y' and i!="Y":
        i=input("Get return?(y/n)")
        if i=='n' or i=='N':
            break
    else:
        gua_n(l1,l2,num)

def gua():
    #基于python的一种算卦方法（张口泽版）(Suggested by Mr.口)
    from random import randint
    num=randint(1,6)
    print('口告诉你你的数字牌为',num)
    yao={0:'--  --',1:'------'}
    print('现在，口问你有用多少张牌\n当输入"0"时，他会用12张牌，输入"1"时也为12张，"2"时给18张，以此类推。')
    ca=int(input('请输入:'))
    def card_mk(ca):
        if ca<0:
            print('口认为你是个sb，并给你12张牌')
            card=12
        elif ca == 0:
            card=12
        else:
            card=ca*6+6
        return card
    card=card_mk(ca)
    print('现在，你使用了'+str(card)+'张牌')
    seed=input('请输入一些字符以洗牌(增加混乱度/熵值)')
    #随机+随机(multiple random)
    def nun(seed,card):
        sed=''
        for i in seed:
            if 48<=ord(i)<=57:
                sed+=i
            else:
                sed+=str(ord(i))
        while len(sed)<card:
            sed+=str(randint(0,9))
        a=[]
        for j in range(card):
            a.append(sed[randint(0,len(sed)-1)])
        return a
    tim=time.time()
    #转10+等可能性检查(for more fairness)
    def prch(a):
        b=[];b_0=0
        for i in a:
            b.append(int(i)%2)
        for j in b:
            if j==0:
                b_0+=1
        nd=0
        if b_0<len(b)/2:
            nd_0=len(b)/2-b_0
            while nd!=nd_0:
                e=randint(0,len(b)-1)
                if b[e]==1:
                    b[e]-=1
                    nd+=1
        if b_0>len(b)/2:
            nd_1=b_0-len(b)/2
            while nd!=nd_1:
                e=randint(0,len(b)-1)
                if b[e]==0:
                    b[e]+=1
                    nd+=1
        return b
    ls=nun(seed,card);lst=prch(ls)
    tim=time.time()-tim
    print("现在，口已经根据你给的字符用了"+str(tim)+"s打乱了牌，并得到了一个牌堆。\n请你为他提供6个不重复的牌号以完成算卦")
    i=0;lis=[]
    while i<6:
        mber=int(input("第"+str(i+1)+"张(已抽取的:"+str(lis)+")"))
        if 0<=mber<=card:
            if mber in lis:
                print("重复")
                i-=1
            else:
                lis.append(mber)
         
        else:
            print("你在干什么，一共",card,"张牌，且顺序为0到",card-1,"，你怎么得到",mber,"的？")
            i-=1
        i+=1
    gx1='';l1=''
    gx2='';l2=''
    cx=lis[::-1]
    cx1=cx[:3]
    cx2=cx[3:]
    for m in cx1:
        gx1+=yao[lst[m]]+'\n';l1+=str(lst[m])
    for n in cx2:
        gx2+=yao[lst[n]]+'\n';l2+=str(lst[n])
    print(gx1+'\n\n'+gx2)
    plus(l1,l2,num)

def jinz():
    from deadly import jz
    x=input("请输入进制数(2～36),没有不输")
    if x!=None:
        x=int(x)
    if not(1<=x<=36 or x==None):
        raise DeadlyError()
        return
    elif x==1:
        raise DeadlyError(message="请你回答一下:0的一进制是啥")
        return
    x=int(x)
    print("进制如何转换？")
    k=int(input('"0"代表x至10进制，"1"代表10至x进制，"2"代表找进制:'))
    if k==0:
        y=input(f"输入一个{x}进制数:").upper()
    elif k==1:
        y=int(input("输入转换成十进制的数:"))
    elif k==2:
        y=input("转换的数:").upper()
        i=int(input("预计结果，在此输入0代表结果为十进制，1表示为不同进制:"))
        if i==0:
            x=int(input("十进制数:"))
        elif i==1:
            xi=input("数的结果:").upper()
            yi=int(input("该数的进制(如果与之前填写的进制一致则可不填):"))
            if yi==None:
                yi=x
            x=jz(1,xi,yi)
    while k!=2 and not x in range(1,37):
        x=int(input("是不是忘了些啥？"))
    m=jz(k,x,y)
    print(m)

def jz(k,x,y):
    dicy={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35}
    di="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if type(y)==str:
        y.upper()
    if k==0:
        l=0;need=di[:x]
        for i in y:
            if i not in need:
                deadly_exit()
            num=dicy[i]
            l=l*x+num
        return l
    elif k==1:
        l=y
        sfan=""
        while l!=0:
            k1=l%x;l=l//x
            sfan+=need[k1]
        s=sfan[::-1];return s
    elif k==2:
        left,right=2,36
        mid=(left+right)//2
        while left<=right:
            v=jz(1,x,mid)
            if v==y:
                p=mid;return p
            elif v<x:
                left=mid+1
            else:
                right=mid-1
        p=-1
        return p

def rpn(user_input=''):#逆波兰表达式

    user_input += input("请输入逆波兰表达式：")
    
    # 替换逗号为空格，然后按空格分割
    tokens = user_input.replace(',', ' ').split()
    
    # 去除空字符串
    tokens = [token for token in tokens if token.strip()]

    caln(tokens)



def caln(list_1):
    from decimal import Decimal, getcontext
    getcontext().prec = 16
    st=[];top=-1
    if not type(list_1)==list:
        return
    op=['+','-','*','/','//','%','^']
    if list_1[0] in op or list[1] in op:
        return
    for i in list_1:
        if i in op:
            b=st.pop()
            a=st.pop()
            if i == '^':#需要给个解决这玩意的好办法，打这样的代码太累了
                c=a**b
            elif i='/':
                c=a/b
            elif i='//':
                c=a//b
            elif i='%':
                c=a%b
            elif i='*':
                c=a*b
            elif i='+':
                c=a+b
            elif i='-':
                c=a-b
            
            st.append(c)
            del c
        else:
            st.append(Decimal(i))
    if len(st)==1:
        print(st[0])
    elif len(st)==0:
        return
    else:
        print('结果是',st,'好像缺点东西，再加点?')
        add=''
        for i in st:
            add+=str(i)+' '
        rpn(add)
    


if __name__=='__main__':
    print('你是真的deadly(You\'re a truly Deadly)你知道吗?\n')
    deadly()
