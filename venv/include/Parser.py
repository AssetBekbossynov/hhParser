import requests
from lxml import html

def get_html(url):
    page = requests.get(url, headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'})
    tree = html.fromstring(page.content)
    return tree

def get_total_page(tree):
    pageNumber = tree.xpath('/html/body/div[5]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[3]/div/a[2]/text()')
    return int(pageNumber[0])

def main():
    url = "https://hh.kz/search/resume?area=40&clusters=true&currency_code=KZT&exp_period=all_time&logic=normal&no_magic=false&order_by=relevance&pos=full_text&text=&page=2"
    baseUrl = "https://hh.kz"
    totalPage = get_total_page(get_html(url))
    for i in range(0, 3):      #Use totalPage variable instead 3
        genUrl = url[0: -2] + str(i)
        anketa = get_html(genUrl).xpath('/html/body/div[5]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/a/@href')
        urlСМ
        print (anketa)

if __name__ == '__main__':
    main()