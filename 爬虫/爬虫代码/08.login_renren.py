#coding=utf-8

import requests



def main():


    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
               }
    cookies = "_r01_=1; ick=eb1dd966-4d10-46e0-ad93-877185f343ee; anonymid=k69b1p5534vj36; depovince=ZGQT; ick_login=41673c5b-dc6e-4978-ad20-43a509739a53; taihe_bi_sdk_uid=13bb78ae5a7b53b3b824c20d92d39b72; taihe_bi_sdk_session=deec787b22a77547f2ede4a869445cd8; first_login_flag=1; ln_uact=940102569@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; springskin=set; jebe_key=0750826c-3ade-451f-9c16-af4574c25b45%7C1c7c11a4c02283afc788950c9fcff0d8%7C1580906796560%7C1%7C1580906795565; wpsid=15263614688257; vip=1; wp_fold=0; __gads=ID=009d129daa5ed655:T=1580907068:S=ALNI_MbrAIjhqHpd4A_DSE86P1mBP46X7Q; wp=0; jebecookies=184d0102-2519-4fac-836c-78d57c273322|||||; _de=7BC63459E74EF7A6E2A69D838E8B6F33696BF75400CE19CC; p=138324de65972bb7c06cf2e77e42a0cd1; t=2b6e25203f67a54585f089d9b49022681; societyguester=2b6e25203f67a54585f089d9b49022681; id=526950701; xnsid=ea913064; ver=7.0; loginfrom=null"
    cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
    print(cookies)




    con = requests.get("http://www.renren.com/526950701/profile",headers=headers,cookies=cookies)


    #保存页面
    with open("renren2.html","w",encoding="utf-8") as file:
        file.write(con.content.decode())

if __name__ == "__main__":
    main()