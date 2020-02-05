### 寻找登录的post地址
- 在form表单中寻找action对应的url地址
  - post的舒徐时input标签中name的值作为键，真正的用户密码作为值的字典，post的url地址就是action对应的url地址

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
