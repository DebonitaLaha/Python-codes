from array import  *

value = array('i', [1,8,2,3,9,2,5])

new = array (value.typecode,  (a for a in value))
for i in range (len(new)):
    print (new[i])

