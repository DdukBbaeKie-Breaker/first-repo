import os

print("shutdown 명령!")

while(1):
    ris = input("1:부팅 시간 설정 2:명령어 and 시간설정 3:초기화~~!:")

    if(ris == '1'):
        con = input("시간대 설정!~ :")
        os.system("shutdown -s -t {}".format(con))
        break
    elif(ris == '2'):
        con1 = input("명령어! :")
        con2 = input("시간대! :")
        os.system("shutdown -{} -t {}".format(con1,con2))
        break

    elif(ris == '3'):
        os.system("shutdown -a")
        print("멈췄다구!")
        break

print("수고했어!")