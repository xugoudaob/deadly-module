#deadly1.3.4.4-beta by xgdb
#add more old-virsion-friendly codes



import sys
import time
#import platform      做一个废案留下的遗产...
__all__=['deadly','deadly_exit','gua_n','plus','gua','jinz','jz','rpn','caln','guess_num']
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
        #return None
    while t!=t1:
        print('deadly')
        t=input('>>> ')
def deadly_exit(t2='Deadly! '):
    deadly(t2)
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
    def card_mk(ca=12):
        if ca<0:
            print('口认为你是个sb，并给你12张牌')
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
    print("现在，口已经根据你给的字符用了{}}打乱了牌，并得到了一个牌堆。\n请你为他提供6个不重复的牌号以完成算卦".format(tim))
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
    if not (x is None):
        x=int(x)
    if not(1<=x<=36 or x is None):
        raise DeadlyError()
        #return None
    elif x==1:
        raise DeadlyError(message="请你回答一下:0的一进制是啥")
        #return None
    x=int(x)
    print("进制如何转换？")
    k=int(input("\"0\"代表{}至10进制，\"1\"代表10至{}进制，\"2\"代表找进制:".format(x,x)))
    if k==0:
        y=input("输入一个{}进制数:".format(x)).upper()
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
            if yi is None:
                yi=x
            x=jz(1,xi,yi)
    else:
        y=0
        deadly_exit()
    while k!=2 and not x in range(1,37):
        x=int(input("是不是忘了些啥？"))
    m=jz(k,x,y)
    print(m)

def jz(k,x,y):
    dicy={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35}
    di="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if type(y)==str:
        y.upper()
    if k==1 or k==0:
        need = di[:x] #a deadly bug
    elif k == 2:
        left, right = 2, 36
        mid = (left + right) // 2
        while left <= right:
            v = jz(1, x, mid)
            if v == y:
                p = mid
                return p
            elif v < x:
                left = mid + 1
            else:
                right = mid - 1
        p = -1
        return p
    else:
        raise DeadlyError("暂未开放")

    if k==0:
        l=0
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
        s=sfan[::-1]
        return s
    raise DeadlyError("Meet unknown error")

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
    if list_1[0] in op or list_1[1] in op:
        return
    for i in list_1:
        if i in op:
            b=st.pop()
            a=st.pop()
            if i == '^':#需要给个解决这玩意的好办法，打这样的代码太累了
                c=a**b
            elif i=='/':
                c=a/b
            elif i=='//':
                c=a//b
            elif i=='%':
                c=a%b
            elif i=='*':
                c=a*b
            elif i=='+':
                c=a+b
            elif i=='-':
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
    
def guess_num(r1 = 0,r2 = 100,fla=False):
    from random import randint
    yn=["y","n","Y","N"]
    if not fla:
        ex=input("是否以默认数字({}-{})进行游玩（y/n）".format(r1, r2))
        #I hate a programming language which has no do-while
        while not (ex in yn):
            ex=input("是否以默认数字({}-{})进行游玩（y/n）".format(r1, r2))
        if ex=="y" or ex=="Y":
            fla=True
        elif ex=="n" or ex=="N":
            try:
                r1=int(input("请输入一个有效的小正值"))
                r2=int(input("请输入一个有效的大正值"))
            except ValueError:
                print("err......")
                deadly()
    if r1+1 < r2-1:
        fla=True #免得有些人跳出循环不带True的
    elif 0<= r2-r1 <=2:
        print("恭喜你，你成功猜出了你要的数是",(r1+r2)/2)
        deadly()
    elif r2-r1 < 0:
        print("我好心，用python特性把它调过来供你游戏")
        r1,r2=r2,r1
        fla=True
    else:
        print("太招笑了(一般不会到这个条件)")
    c_num = randint(r1, r2)
    n_min=r1;n_max=r2
    if fla:#在范围为0-0出现的问题，还好被下面的while挡住了
        print("欢迎来到猜数游戏！这里已经有了一个{}到{}之间的整数。".format(r1, r2))
    while fla: #套用变量检验，免得有些人跳出检查环节fla不带True的
        try:
            if n_min+1 >= n_max-1:
                print("因为作者认为没必要猜了，所以恭喜你猜出正确数字{}！".format(int((n_max+n_min)/2)))
                break
            guess = int(input("请输入你猜的数字（({}-{})）：".format(n_min, n_max)))
            
            if guess == c_num:
                print("恭喜你猜对了！正确数字就是 {}！".format(c_num))
                break
            elif guess in list(range(n_min,n_max+1)):
                # 根据猜的数调整范围，并生成新的正确数
                if guess < c_num:
                    print("小！")
                    n_min = guess+1
                    n_max = n_max
                elif guess > c_num:
                    print("大！")
                    n_min = n_min
                    n_max = guess-1
                # 在新的范围内随机选一个数作为新的正确数
                c_num = randint(n_min, n_max)
                print("新的数已在 {} 到 {} 之间重新生成！".format(n_min, n_max))
            else:
                raise DeadlyError("out1")
        except ValueError:
            print("请输入一个有效的整数！")
        except:
            raise DeadlyError("out0")



if __name__=='__main__':
    print('你是真的deadly(You\'re a truly Deadly)你知道吗?\n')
    deadly()
