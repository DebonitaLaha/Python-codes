

N, M = map(int, input().split())
for i in range(0,int((N-1)/2)):
    s='.|.'*i
    print(s.rjust(int((M-3)/2),'-')+'.|.'+('.|.'*i).ljust(int((M-3)/2),'-'))
print("WELCOME".center(M,'-'))
for j in reversed(range(0,int((N-1)/2))):
    s='.|.'*j
    print(s.rjust(int((M-3)/2),'-')+'.|.'+('.|.'*j).ljust(int((M-3)/2),'-'))
