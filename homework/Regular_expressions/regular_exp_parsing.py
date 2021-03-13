from bs4 import BeautifulSoup
import re
import requests

url = "http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5%D1%81_" \
      "%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82%D0%BE%D0%B2%D0%B8" \
      "%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1" \
      "%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1" \
      "%81%D0%B8%D1%82%D0%B5%D1%82%D1%83"

headers = {
    "Accept": "text/css,*/*;q=0.1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/88.0.4324.192 Safari/537.36"
}

PATTERN = r"\(?P<text>[А-ЯҐЄІЇа-яґєії -]*)\s(?P<email>[\w]*).?([\w\-]+@[\w\-.]*)"


def get_html():
    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "html.parser").body
    parsing = re.finditer(PATTERN, soup, flags=re.M)
    result = []
    for elem in parsing:
        text = elem.group("text")
        email = elem.group("email")
        result.append((text, email))

    return result


if __name__ == "__main__":
    print(get_html())

