import scrapy
from wyijobs.items import WyijobsItem


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['163.com']
    # 修改起始的url
    start_urls = ['https://hr.163.com/position/list.do']

    def parse(self, response):
        # id属性值为动态，故而找class属性值
        job_list = response.xpath('//*[@class="position-tb"]/tbody/tr')
        # print(len(job_list))
        for i in range(len(job_list)//2):
            # 实例化建模对象
            item = WyijobsItem()
            item['name'] = job_list[2*i].xpath('.//a/text()').extract_first()
            item['link'] = 'https://hr.163.com/' + job_list[2*i].xpath('.//a/@href').extract_first()
            item['department'] = job_list[2*i].xpath('.//a/text()').extract_first()
            item['type'] = job_list[2*i].xpath('./td[2]/text()').extract_first()
            item['city'] = job_list[2*i].xpath('./td[5]/text()').extract_first()
            item['num'] = job_list[2*i].xpath('./td[6]/text()').extract_first().strip()
            item['date'] = job_list[2*i].xpath('./td[7]/text()').extract_first()
            # print(item)
            # 利用meta参数实现数据在不同解析函数中传递
            yield scrapy.Request(
                url=item['link'],
                callback=self.detail_page,
                meta={'item': item}
            )

        # 翻页（最后一页的href属性值为：javascript:void(0)）
            temp = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[9]/@href').extract_first()
            # 不能用+拼接，temp字符串会累加
            # next_url = response.url + temp
            if temp != 'javascript:void(0)':
                next_url = response.urljoin(temp)
                yield scrapy.Request(url=next_url, callback=self.parse)

    def detail_page(self, response):
        # 获取之前传入的item
        item = response.meta['item']
        item['describe'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').extract()
        item['require'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').extract()
        yield item




