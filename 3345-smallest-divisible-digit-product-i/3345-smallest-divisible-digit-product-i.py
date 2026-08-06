class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        str1=str(n)
        l=[]
        if str1!='10' or '20' or '30' or '40' or '50' or '60' or '70' or '80' or '90' or '100':
            for i in range(len(str1)):
                l.append(ord(str1[i])-48)
            if len(l)>1:
                if l[0]*l[1]%t==0:
                    return n
                elif l[0]*l[1]%t!=0:
                    while l[0]*l[1]%t!=0:
                        if l[1]<9:
                            l[1]+=1
                        else:
                            l[0]+=1
                            l[1]=0
                        if l[0]*l[1]%t==0 or l[0]*l[1]==0:
                            return int("".join(map(str, l)))
            elif len(l)==1:
                if n%t==0:
                    return n
                elif n%t!=0:
                    while n%t!=0:
                        n+=1
                        if n==10 :
                            return n
                        elif n%t==0:
                            return n
        else:
            return n
        
        


        