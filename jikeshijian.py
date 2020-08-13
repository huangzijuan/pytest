# !/bin/python

import os
import json
from pathlib import Path
import html2text


def process_article(article_id, title):
    article_file = os.path.join(articles_dir, title.replace("/", "-"))
    print(article_file)
    if os.path.exists(article_file):
        return
    #curl_request = "curl 'https://time.geekbang.org/serv/v1/article' -H 'Connection: keep-alive' -H 'Accept: application/json, text/plain, */*' -H 'Sec-Fetch-Dest: empty' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' -H 'Content-Type: application/json' -H 'Origin: https://time.geekbang.org' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Referer: https://time.geekbang.org/column/article/" + str(article_id) + "' -H 'Accept-Language: zh-CN,zh;q=0.9' -H 'Cookie: _ga=GA1.2.220046177.1578034132; LF_ID=1578034196285-4237781-9999723; MEIQIA_TRACK_ID=1TBA6aAFkRrrKPDt387kwCC0OZF; MEIQIA_VISIT_ID=1Xb8APUJ1eiVJ9YaXcVepvTy40z; gksskpitn=5b5916cf-eaaa-455f-becc-395a836681fd; GCID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; GRID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; _gid=GA1.2.45666001.1587352871; GCESS=BAUEAAAAAAoEAAAAAAsCBAAIAQMJAQEEBAAvDQAGBPs6kXsHBLOcov0DBBU4nV4CBBU4nV4BBB6cGwAMAQE-; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1587361799,1587361804,1587361815,1587361836; _gat=1; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1587361912; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1587361913|1587361788' --data-binary '{\"id\":\"" + str(article_id) + "\",\"include_neighbors\":true,\"is_freelyread\":true}' --compressed"

    curl_request = "curl 'https://time.geekbang.org/serv/v1/article' -H 'Connection: keep-alive' -H 'Accept: application/json, text/plain, */*' -H 'Sec-Fetch-Dest: empty' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' -H 'Content-Type: application/json' -H 'Origin: https://time.geekbang.org' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Referer: https://time.geekbang.org/column/article/" + str(article_id) + "' -H 'Accept-Language: zh-CN,zh;q=0.9' -H 'Cookie: _ga=GA1.2.220046177.1578034132; LF_ID=1578034196285-4237781-9999723; MEIQIA_TRACK_ID=1TBA6aAFkRrrKPDt387kwCC0OZF; MEIQIA_VISIT_ID=1Xb8APUJ1eiVJ9YaXcVepvTy40z; gksskpitn=5b5916cf-eaaa-455f-becc-395a836681fd; GCID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; GRID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; _gid=GA1.2.45666001.1587352871; orderInfo={%22list%22:[{%22count%22:1%2C%22image%22:%22https://static001.geekbang.org/resource/image/c6/58/c6df2543493de6b964a70277ba147b58.jpg%22%2C%22name%22:%22%E8%B6%A3%E8%B0%88Linux%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%22%2C%22desc%22:%2272%E8%AE%B2%20|%2022212%E4%BA%BA%E5%B7%B2%E5%AD%A6%E4%B9%A0%22%2C%22sku%22:100024701%2C%22price%22:{%22sale%22:12900}}]%2C%22invoice%22:false%2C%22app_id%22:3%2C%22cid%22:164%2C%22isFromTime%22:true%2C%22detail_url%22:%22https://time.geekbang.org/column/intro/164%22}; GCESS=BAwBAQcEcJxhYggBAwEERFIWAAYE.zqRewUEAAAAAAoEAAAAAAQEAC8NAAIEuEShXgsCBAAJAQEDBLhEoV4-; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1587549585,1587627011,1587627184,1587627193; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1587627383|1587624468; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1587627383; _gat=1' --data-binary '{\"id\":\"" + str(article_id) + "\",\"include_neighbors\":true,\"is_freelyread\":true}' --compressed"
    response = os.popen(curl_request).read()
    article = json.loads(response)
    print(article_id)
    print(article)

    audio = article["data"]["audio_download_url"]
    content = article["data"]["article_content"]

    all_content = "<h1>" + title + "</h1>\n"
    all_content += "<a href=\"" + audio + "\">音频</a>\n"
    all_content += content

    with open(article_file, "w") as fw:
        fw.write(html2text.html2text(all_content))


def get_articles():
    #curl_request = "curl 'https://time.geekbang.org/serv/v1/column/articles' -H 'Connection: keep-alive' -H 'Accept: application/json, text/plain, */*' -H 'Sec-Fetch-Dest: empty' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' -H 'Content-Type: application/json' -H 'Origin: https://time.geekbang.org' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Referer: https://time.geekbang.org/column/intro/164?tab=catalog' -H 'Accept-Language: zh-CN,zh;q=0.9' -H 'Cookie: _ga=GA1.2.220046177.1578034132; LF_ID=1578034196285-4237781-9999723; MEIQIA_TRACK_ID=1TBA6aAFkRrrKPDt387kwCC0OZF; MEIQIA_VISIT_ID=1Xb8APUJ1eiVJ9YaXcVepvTy40z; gksskpitn=5b5916cf-eaaa-455f-becc-395a836681fd; GCID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; GRID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; _gid=GA1.2.45666001.1587352871; GCESS=BAsCBAAJAQEHBClYiXYCBC4VnV4DBC4VnV4IAQMGBPs6kXsEBAAvDQABBB6cGwAFBAAAAAAMAQEKBAAAAAA-; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1586335536,1586347505,1587352871,1587352879; _gat=1; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1587353146; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1587353147|1587352870' --data-binary '{\"cid\":100024701,\"size\":200,\"prev\":0,\"order\":\"earliest\",\"sample\":false}' --compressed"
    curl_request = "curl 'https://time.geekbang.org/serv/v1/column/articles' -H 'Connection: keep-alive' -H 'Accept: application/json, text/plain, */*' -H 'Sec-Fetch-Dest: empty' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' -H 'Content-Type: application/json' -H 'Origin: https://time.geekbang.org' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Referer: https://time.geekbang.org/column/intro/161?tab=catalog' -H 'Accept-Language: zh-CN,zh;q=0.9' -H 'Cookie: _ga=GA1.2.220046177.1578034132; LF_ID=1578034196285-4237781-9999723; MEIQIA_TRACK_ID=1TBA6aAFkRrrKPDt387kwCC0OZF; MEIQIA_VISIT_ID=1Xb8APUJ1eiVJ9YaXcVepvTy40z; gksskpitn=5b5916cf-eaaa-455f-becc-395a836681fd; GCID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; GRID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; _gid=GA1.2.45666001.1587352871; orderInfo={%22list%22:[{%22count%22:1%2C%22image%22:%22https://static001.geekbang.org/resource/image/c6/58/c6df2543493de6b964a70277ba147b58.jpg%22%2C%22name%22:%22%E8%B6%A3%E8%B0%88Linux%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%22%2C%22desc%22:%2272%E8%AE%B2%20|%2022212%E4%BA%BA%E5%B7%B2%E5%AD%A6%E4%B9%A0%22%2C%22sku%22:100024701%2C%22price%22:{%22sale%22:12900}}]%2C%22invoice%22:false%2C%22app_id%22:3%2C%22cid%22:164%2C%22isFromTime%22:true%2C%22detail_url%22:%22https://time.geekbang.org/column/intro/164%22}; GCESS=BAwBAQcEcJxhYggBAwEERFIWAAYE.zqRewUEAAAAAAoEAAAAAAQEAC8NAAIEuEShXgsCBAAJAQEDBLhEoV4-; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1587549585,1587627011,1587627184,1587627193; _gat=1; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1587627277; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1587627278|1587624468' --data-binary '{\"cid\":100024501,\"size\":200,\"prev\":0,\"order\":\"earliest\",\"sample\":false}' --compressed"
    response = os.popen(curl_request).read()
    articles = json.loads(response)["data"]["list"]
    for item in reversed(articles):
        print(item["id"], item["article_title"])
        process_article(item["id"], item["article_title"])


def process():
    get_articles()

def test():
    curl_request = "curl 'https://time.geekbang.org/serv/v1/column/articles' -H 'Connection: keep-alive' -H 'Accept: application/json, text/plain, */*' -H 'Sec-Fetch-Dest: empty' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' -H 'Content-Type: application/json' -H 'Origin: https://time.geekbang.org' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Referer: https://time.geekbang.org/column/intro/164?tab=catalog' -H 'Accept-Language: zh-CN,zh;q=0.9' -H 'Cookie: _ga=GA1.2.220046177.1578034132; LF_ID=1578034196285-4237781-9999723; MEIQIA_TRACK_ID=1TBA6aAFkRrrKPDt387kwCC0OZF; MEIQIA_VISIT_ID=1Xb8APUJ1eiVJ9YaXcVepvTy40z; gksskpitn=5b5916cf-eaaa-455f-becc-395a836681fd; GCID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; GRID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; _gid=GA1.2.45666001.1587352871; GCESS=BAUEAAAAAAoEAAAAAAsCBAAIAQMJAQEEBAAvDQAGBPs6kXsHBLOcov0DBBU4nV4CBBU4nV4BBB6cGwAMAQE-; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1587361799,1587361804,1587361815,1587361836; _gat=1; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1587362253; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1587362253|1587361788' --data-binary '{\"cid\":100024701,\"size\":200,\"prev\":0,\"order\":\"earliest\",\"sample\":false}' --compressed"
    response = os.popen(curl_request).read()
    article = json.loads(response)
    print(article)


if __name__ == '__main__':
    articles_id = "110"

    home = str(Path.home())
    articles_dir = os.path.join(home, articles_id)
    if not os.path.exists(articles_dir):
        os.makedirs(articles_dir)

    process()
    #test()
