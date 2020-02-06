### 寻找登录的post地址
- 在form表单中寻找action对应的url地址
  - post的数据是input标签中name的值作为键，真正的用户密码作为值的字典，post的url地址就是action对应的url地址

- 抓包
  - 勾选perserv log按钮，防止页面跳转找不到url地址
  - 寻找post数据，确定参数
    - 参数不会变，直接用，比如密码不是动态加密的时候
    - 参数会变
      - 参数在当前的响应中
      - 通过js生成

### 定位想要的JS
- 选择会触发JS时间的按钮，点击event listener,找到js的位置
- 通过chrome中的search all file 搜索url中的关键字
- 添加断点的方式来查看js的操作，通过python来进行同样的操作


### requests小技巧
- reqeusts.utils.dict_from_cookiejar  把cookie对象转化为字典
- requests.utils.unquote(),url的解码
- 请求 SSL证书验证
    - response = requests.get("https://www.12306.cn/mormhweb/ ", verify=False)
- 设置超时
    - response = requests.get(url,1)
- 配合状态码判断是否请求成功
    - assert response.status_code == 200
```python
import requests
requests.utils.unquote("https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85%E5%90%A7")
requests.utils.quote("https://tieba.baidu.com/f?kw=李毅吧")

```
### json使用注意点
- json中的自符串都是双引号引起来的
    - 如果不是双引号
        - eval:能实现简单的字符串和python类型的转化
        - replace: 把单引号替换为双引号
        
- 往一个文件中写入多个json串，不再是一个json串，不能直接读取
    - 一行写一个json串，按照行来读取
    
```python
import json
#json.dumps()用于将dict类型的数据转成str，因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。
name_emb = {'a':'1111','b':'2222','c':'3333','d':'4444'}
jsObj = json.dumps(name_emb)
print(jsObj)
print(type(name_emb))
print(type(jsObj))
```
