def isPythagorean (a, b, M): 
    if (a*a + b*b) == (M - a - b)*(M - a - b):
        return True
    else:
        return False

def findPythagorean (MAX):
    for an in range(1,MAX):
        for bn in range(an,MAX):
            if isPythagorean(an,bn,MAX) is True:                
                return (an * bn * (MAX-an-bn))