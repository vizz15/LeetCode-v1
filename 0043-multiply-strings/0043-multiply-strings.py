class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result1=0
        result2=0
        sign1=1
        sign2=1
        start=0

        if num1 and num2 == "":
            return -1
        
        if num1[0]=='-':
            sign11=-1
            start=1
        elif num1[0]=='+':
            sign1=+1
            start=1


        if num2[0]=='-':
            sign2=-1
            start=1
        elif num2[0]=='+':
            sign2=+1
            start=1
        
        for i in range(start,len(num1)):
            char1=num1[i]
            digit=ord(char1)-ord('0')#converts to ascii value
            result1=(result1*10)+digit
        for i in range(start,len(num2)):
            char2=num2[i]
            digit=ord(char2)-ord('0')#converts to ascii value
            result2=(result2*10)+digit
        
        return str(result1*result2*sign1*sign2)




        