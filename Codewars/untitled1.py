def my_first_kata(a,b):
    if ((type(a) and type(b)) == str) or ((type(a) or type(b))  == str): return False
    elif (a and b) == 0: return False
    else:
        return a % b ++ b % a
    
a = my_first_kata(-1,-1)
print(a)
