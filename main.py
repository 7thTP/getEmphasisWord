import requests
from bs4 import BeautifulSoup


def main():
    urls = ["https://fabcross.jp/topics/fabnavi/20240319_rokugobase.html",
            "https://fabcross.jp/topics/special/20231226_10th_anniversary.html",
            "https://fabcross.jp/topics/research/20231225_fabspace.html",
            "https://fabcross.jp/topics/special/20231219_switchscience_2023.html"]
    tags = ["strong", "b"]

    for url in urls:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        print("ページタイトル：", soup.find_all("title")[0].get_text())
        for tag in tags:
            items = soup.find_all(tag)
            for element in items:
                print(element.get_text())
        print("---------")


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    main()
