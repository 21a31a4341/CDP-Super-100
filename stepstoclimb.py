def steps(a,n):
    if a>n:
        return 0
    elif a==n:
        return 1
    result1=steps(a+1,n)
    result2=steps(a+2,n)
    #print(result1,result2)
    return result1+result2
print(steps(0,5))