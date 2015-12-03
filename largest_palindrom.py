aa = '3132'
a_rev = '2313'
MOD = 1000000007

def check_exist(k):
    h = {}
    h_rev = {}
    key , an , a = 0, 1 ,10
    for i in range(0,k):
        key = (key* a + int(aa[i])) % MOD
        an = (an * a) % MOD

    h[key]=1
    print  key
    i = 1
    while (i + k - 1 < len(aa)):
        key = ( (key * a) + int(aa[i + k - 1]) - (an * int(aa[i - 1]))) % MOD
        print key
        h[key] =1    
        i=i+1 

    key , an ,   a = 0, 1 ,10
    for i in range(0,k):
        key = (key* a + int(a_rev[i])) % MOD
        an = (an * a) % MOD

    print key
    h_rev[key]=1
    if key in h:
        return True

    i = 1
    while (i + k - 1 < len(a_rev)):
        key = (key * a + int(a_rev[i + k - 1]) - an * int(a_rev[i - 1])) % MOD
        print key
        h_rev[key] =1 

        i=i+1
        if key in h:
            return True      
    return False

l , h =1,len(aa)
answer = 0
while(l<=h):
    mid = (l+h)/2
    if(check_exist(mid)):
        answer = mid
        l = mid + 1
    else:
        h = mid-1

print 'Longest palindromic substring = ' ,answer
