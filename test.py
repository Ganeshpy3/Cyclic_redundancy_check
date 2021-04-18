
def crc(data,key,opt):
    temp=data+"0"*(len(key)-1)
    key0="0"*len(key)
    xor=bin(int(temp[:len(key)],2)^int(key,2))[2:]
    for _ in range(len(xor),len(key)):
        xor="0"+xor
    for i in range(len(key),len(temp)):
        if(len(xor)==len(key)):
            if(xor[1:2]=="1"):
                xor=bin(int((xor[1:]+temp[i:i+1]),2)^int(key,2))[2:]
                for _ in range(len(xor), len(key)):
                    xor = "0" + xor
            else:
                xor = bin(int((xor[1:] + temp[i:i + 1]), 2) ^ int(key0, 2))[2:]
                for _ in range(len(xor), len(key)):
                    xor = "0" + xor
    if opt=="find":
        print(data+xor[1:])
    elif opt=="check":
        if int(xor,2)==0:
            print("NO error")
        else:
            print("Error")




while True:
    inp=input("Enter your choice\n1.Find crc\n2.Check CRC\n3.Quite\n")
    if inp=="1":
        print("Finding....")
        crc(input("Enter Data:\n"),input("Enter key:\n"),"find")
    elif inp=="2":
        print("Checking....")
        crc(input("Enter the value:\n"),input("Enter key:\n"),"check")
    elif inp=="3":
         break
    else:
        print("Choose correct option")


crc("1101011011","10011","2")