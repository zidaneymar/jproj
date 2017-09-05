from scrapy import cmdline


name = 'bestfilm'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())