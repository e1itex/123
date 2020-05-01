import os
import request

try:
    from torrequest import TorRequest
except:
    os.system("pip install torrequest && clear")
    from torrequest import TorRequest
 
with TorRequest(password='Risk1234') as tr:
 
request = {'User-Agent':'Mozilla'}
a = str(input("URL    - "))
x = int(input("Amount - "))
 
def run():
    for i in range(x):
        tr.reset_identity()
        response= tr.get(a)
        print(i+1)
 
run()
