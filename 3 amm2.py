import json
amm1=0
amm2= {}
amm3 = []
name = input(" name :")
with open("ammar.json","r") as f:
    ammar=json.loads(f.read())
    for i in ammar :
        print(i)
        a1 = input("enter  a or b :")
        amm3.append(a1)
        if a1 ==ammar[i]:
            amm1=amm1+1
        else:
            amm1=amm1-1

    amm2 ={name:amm3}
    print(amm2)

    print("The result :",amm1)
