
import requests
import time
import json
from lxml import etree

def get_user_content(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    header = {'user-agent':ua}
    response = requests.get(url,headers = header)
    selector = etree.HTML(response.text)
    content_dict = {}
    for i in range(1,16):
        content = selector.xpath(f"//div[@class='List-item'][{i}]/div/div[2]/div/span/p/text()")
        content_dict[f'{i}'] = content
    content_str  = json.dumps(content_dict,ensure_ascii=False)
    with open('content.json','w',encoding='utf-8') as f:      
        f.write(content_str)

if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/433415189'
    get_user_content(url)


