import time
import random
import os
s=0
m="clear"
l="Score: "
g="<Game "
while 1:
 ss=str(s)
 print(g+"Started>")
 print(l+ss)
 k=random.randint(1,1000) % 26
 f=97+k
 c=chr(f)
 a=time.time()
 print("Press Key: "+c)
 i=str(input())
 b=time.time()
 if abs(b-a)<(4-(s/10)) and c==i:
  s=s+1
 else:
  s=0
  os.system(m)
  print(g+"Over>")
  print(l+ss)
  time.sleep(2)
 os.system(m)
