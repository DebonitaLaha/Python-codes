def find_007(find_here):
    for i in range(0,find_here[len-2]):
        if find_here(i)==0 and find_here(i+1) and find_here(i+2):
            return True,i  
        else: 
            return False,0
        
def sender():
    send_this= input("enter your list to")
    decide,position= find_007(send_this)
    if decide == True:
        print("you have found 007 in "+i+" place")
    else :
        print("not found")
    
    