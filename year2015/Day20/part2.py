from pynapl import APL


apl = APL.APL()



# it is better to just let it run until it finds the answer.
limit=36000000/11


i = 165000
i = 800000
while True:
    i += 100
    
    print(i)
    
    val = apl.eval(f'⌊/⍸3272727<{{+/⍵{{((⍺÷50)≤⍵)/⍵}}(∪⊢∨⍳)⍵}}¨(⍳100)+{i-1}')
    if val < i + 1000:
        print(val+i)
        break
