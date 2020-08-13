import os

import html2text



if __name__ == '__main__':

    article_file = os.path.join("/Users/huangzijuan/110", '“趣谈Linux操作系统”食用指南')
    with open(article_file, "w") as fw:
        fw.write(html2text.html2text(article_file))