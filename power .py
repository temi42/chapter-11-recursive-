#recursive power function
#@params:b(float), n (non negative integer)
#@return: b * n
def powBN(b,n):
    #base cases(s)
    if n == 0:
        return 1
    
    #recursive cases(s)
    else:
        return b * powBN(b, n-1) 
    
   

print(powBN(3.14,10))
