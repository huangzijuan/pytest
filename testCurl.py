import json
import os
import html2text

if __name__ == '__main__':
    article_title = '开篇词 | 为什么我们要学习Java虚拟机？'
    article_id = '11074'
    article_file = os.path.join("/Users/huangzijuan/110", article_title)
    curl_request = "curl 'https://time.geekbang.org/serv/v1/article' -H 'Connection: keep-alive' -H 'Accept: application/json, text/plain, */*' -H 'Sec-Fetch-Dest: empty' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' -H 'Content-Type: application/json' -H 'Origin: https://time.geekbang.org' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Referer: https://time.geekbang.org/column/article/" + str(article_id) + "' -H 'Accept-Language: zh-CN,zh;q=0.9' -H 'Cookie: _ga=GA1.2.220046177.1578034132; LF_ID=1578034196285-4237781-9999723; MEIQIA_TRACK_ID=1TBA6aAFkRrrKPDt387kwCC0OZF; MEIQIA_VISIT_ID=1Xb8APUJ1eiVJ9YaXcVepvTy40z; gksskpitn=5b5916cf-eaaa-455f-becc-395a836681fd; GCID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; GRID=be9e9fa-1d4c5e1-5a11e7c-b137e8c; _gid=GA1.2.45666001.1587352871; GCESS=BAMEm7SeXgUEAAAAAAwBAQgBAwsCBAAEBAAvDQACBJu0nl4HBGVu3noJAQEGBPs6kXsKBAAAAAABBB6cGwA-; _gat=1; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1587459169,1587459228,1587546208,1587546818; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1587546847; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1587546847|1587546099' --data-binary '{\"id\":\"" + str(article_id) + "\",\"include_neighbors\":true,\"is_freelyread\":true}' --compressed"
    response = os.popen(curl_request).read()
    article = json.loads(response)
    print(article)

    audio = article["data"]["audio_download_url"]
    content = article["data"]["article_content"]

    all_content = "<h1>" + article_title + "</h1>\n"
    all_content += "<a href=\"" + audio + "\">音频</a>\n"
    all_content += content

    with open(article_file, "w") as fw:
        fw.write(html2text.html2text(all_content))