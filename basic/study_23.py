import requests
from lxml import etree


def fetch_tencent_news():
    url = "https://news.qq.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/92.0.4515.159 Safari/537.36"
    }

    # 防止走系统代理 + 忽略证书验证
    resp = requests.get(
        url,
        headers=headers,
        verify=False,
        proxies={"http": None, "https": None}
    )

    if resp.status_code != 200:
        print(f"请求失败，状态码：{resp.status_code}")
        return

    tree = etree.HTML(resp.text)

    # 你提供的 XPath
    news_spans = tree.xpath('//*[@id="channel-feed-area"]/div[3]/div[7]/a/span')

    if not news_spans:
        print("未获取到新闻标题，可能是页面动态渲染。")
    else:
        for i, span in enumerate(news_spans, 1):
            print(f"{i}. {span.text}")


def douban_xpath():
    for page in range(1, 11):
        resp = requests.get(
            url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
            headers={'User-Agent': 'BaiduSpider'}
        )
        tree = etree.HTML(resp.text)
        # 通过XPath语法从页面中提取电影标题
        title_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
        # 通过XPath语法从页面中提取电影评分
        rank_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]')
        for title_span, rank_span in zip(title_spans, rank_spans):
            print(title_span.text, rank_span.text)


if __name__ == "__main__":
    # fetch_tencent_news()
    douban_xpath()
