class strReplace:
    def strReplace(self,str1,reStr):
        str1 = str1.replace(" ", reStr, 1)
        return str1


str1 = "hello world"
str1 =strReplace().strReplace(str1,"$")
print(str1)