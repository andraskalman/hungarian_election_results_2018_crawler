# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HungarianElectionResultsPipeline(object):

    def process_item(self, item, spider):
        # Normalize page generated text
        if 'page_generated_at' in item:
            item['page_generated_at'] = item['page_generated_at'].replace('Frissitve:', '').replace(u'\xa0', u' ').strip()

        if 'district' in item:
            item['district'] = item['district'].replace('.számú egyéni választókerületi szavazás', '').replace(u'\xa0', u' ').strip() # 2018
            item['district'] = item['district']\
                .replace(' megye', '').replace(' főváros', '') \
                .replace('. számú egyéni választókerület', '').replace(u'\xa0',u' ').strip() # 2014

        return item
