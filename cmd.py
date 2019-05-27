import os
import string

print(os.system("tasklist"))

while(1):
    i = input("1.이름으로 죽이기 2.PID로 죽이기 :")

    if(i == '1'):
        pid = input("Input PID! : ")
        id=os.system("taskkill /f /PID {}".format(pid))
        break

    elif(i == '2'):
        IM = input("Input IM! : ")
        id = os.system("taskkill /f /IM {}".format(IM))
        break

print("끗!")


