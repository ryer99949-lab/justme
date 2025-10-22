#hi guys, so this is just a crude lil model i made that calculates average product and total product for a hypothetical silk factory





print("we assume the machine has one year value and dep at 40 percent")

e = int(input("mate how many values do you want to run this for"))

for i in range(e):
    print(f"\n--- Entry {i+1} ---")
    
    
    n = int(input("num of cocoons "))
    p = int(input("average output of the machines"))
    w = int(input("average output of all of labour "))

    d = p - p % 40
    r = n % 2 + p - d + w
    a = n % 2 + p - d + w / w

    if a== 0:
        print("Stop")
    elif r== 0:
        print("No")
    else:
        print("Total product:", r)
        print("Average product:", a)

        

print("Calculation done")









































































