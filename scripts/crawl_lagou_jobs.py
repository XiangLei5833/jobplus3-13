import scrapy

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = ['https://www.lagou.com']

    def parse(self, response):
        for job in response.xpath('//*[@id="jobList"]/div[1]/ul/li'):
            yield {
                    'jobname': job.xpath('.//div[1]/div[1]/div/h2/a/text()').extract_first(),
                    'wage_area': job.xpath('.//div[1]/div[1]/span[@class="salary fr"]/text()').extract_first(),
                    'release_date' : job.xpath('.//div[1]/div[1]/div/span/text()').extract_first(),    
                    'working_address': job.xpath('.//div[2]/div/div[2]/span[3]/text()').extract_first(),
                    'experience': job.xpath('.//div[1]/div[2]/span[1]/text()').extract_first(),
                    'education': job.xpath('.//div[1]/div[2]/span[2]/text()').extract_first(),
                    'logo': job.xpath('.//div[2]/a/img/@src').extract_first(),
                    'company_name': job.xpath('.//div[2]/div/div[1]/a/text()').extract_first(),
                    'offical_websit': job.xpath('.//div[2]/div/div[1]/a/@href').extract_first(),
                    'industry': job.xpath('.//div[2]/div/div[2]/span[1]/text()').extract_first(),
                    'stage': job.xpath('.//div[2]/div/div[2]/span[2]/text()').extract_first(),
                    'city': job.xpath('.//div[2]/div/div[2]/span[3]/text()').extract_first()
                    
                }
