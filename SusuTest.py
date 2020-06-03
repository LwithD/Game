def isTriangle(a,b,c):
    if a+b>c:
        if a+c>b:
            if b+c>a:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def main():
    a,b,c=eval(input("请输入三条边长:"))
    if isTriangle(a,b,c):
        print("这三条边可以组成三角形")
    else:
        print("这三条边不能组成三角形")

main()
