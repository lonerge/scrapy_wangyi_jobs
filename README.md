# scrapy_wangyi_jobs
利用scrapy框架爬取网易招聘信息


1.创建项目
scrapy startproject wyijobs

2.建模
分析需要抓取的字段
items.py
其中包括：
招聘标题：name
招聘详情页：link
所属部门：department
类型：type
城市：city
人数：num
日期：date
详情页的职位描述：describe
详情页的职位要求：require



3.项目创建爬虫
scrapy genspider jobs hr.163.com

4.完善爬虫
spiders里面的jobs.py
其中主要功能：
爬取每一页目标字段，爬取详情页目标字段，翻页
利用scrapy.Request(url, callback, meta={})中的meta参数在首页与详情页解析函数中传递数据，得到完整的item对象

5.管道处理
保存为json文件
pipelines.py

6.设置setting
修改setting.py
其中包括：
添加user-agent
取消rebots协议
开启管道

7.启动爬虫
scrapy crawl jobs

最后得到wyijobs.json文件
