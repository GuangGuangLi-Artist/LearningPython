#coding=utf-8

from lxml import etree


def main():
    text = ''' <div> 
    <ul> 
    <li class="item-1"><a href="link1.html">first item</a></li> '
    <li class="item-1"><a href="link2.html">second item</a></li> 
    <li class="item-inactive"><a href="link3.html">third item</a></li> 
    <li class="item-1"><a href="link4.html">fourth item</a></li> 
    <li class="item-0"><a href="link5.html">fifth item</a>
    </ul> </div> '''

    html = etree.HTML(text)
    #查看element对象中包含的字符串
    # print(etree.tostring(html).decode("UTF-8"))

    ret1 = html.xpath("//li[@class='item-1']/a/@href")
    print(ret1)

    ret2 = html.xpath("//li[@class='item-1']/a/text()")
    print(ret2)

    for href in ret1:
        item = {}
        item["href"] = href
        item["title"] =ret2[ret1.index(href)]
        print(item)

    print("*" * 20)

    ret3 = html.xpath("//li[@class='item-1']")
    print(ret3)
    for i in ret3:
        item1 = {}
        item1['title'] = i.xpath("a/text()")[0] if len(i.xpath("./a/text()")) >0 else None
        item1['href'] = i.xpath("./a/@href")[0] if len(i.xpath("./a/@href")) > 0 else None
        print(item1)




if __name__ == '__main__':
    main()