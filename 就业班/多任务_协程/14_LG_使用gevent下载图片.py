#coding=utf-8

import urllib.request
import gevent
from gevent import monkey


def down_load_img(file_name,img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(file_name,"wb") as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(down_load_img,"1.jpg","https://rpic.douyucdn.cn/live-cover/appCovers/2019/11/18/5362514_20191118233433_small.jpg/webpdy1"),
        gevent.spawn(down_load_img,"2.jpg","https://rpic.douyucdn.cn/live-cover/roomCover/2019/11/15/7519583e52c4955464682a4be6ed288d_big.jpg/webpdy1")
    ])


if __name__ == "__main__":
    main()