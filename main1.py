from math import sqrt
def solve(n):
   sq_root = int(sqrt(n))
   if(sq_root*sq_root) == n:
     print('perfect')
   else:
     print('not perfect')
n = int(input("check a number to be sqrt  : "))
solve(n)