def print_rangoli(size):
    if size==1:
        print("a")
    else:
        for i in range(size,0,-1):
            alpha,beta,gamma,b="","","",""
            for j in range(size,i-1,-1):
                alpha = alpha+'-'+chr(97+(j-1))
            if i==1:
                alpha=alpha.rjust(((size*2)-1),'-').rstrip('-')
                print(alpha.lstrip('-'),end="")
            else:
                print( alpha.rjust(((size*2)-1),'-').rstrip('-'),end="")

            for k in range (i+1,size+1,1):
                beta = beta+'-'+chr(97+(k-1))
            print(beta.ljust(((size*2)-2),'-'))
        #reversed
        for n in reversed(range(size,1,-1)):
            delta,pie ="",""
            for o in range(size,n-1,-1):
                delta = delta+'-'+chr(97+(o-1))
            print( delta.rjust(((size*2)-1),'-').rstrip('-'),end="")

            for p in range (n+1,size+1,1):
                pie=pie+'-'+chr(97+(p-1))
            print(pie.ljust(((size*2)-2),'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)