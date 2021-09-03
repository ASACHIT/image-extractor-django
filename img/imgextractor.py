import requests

from bs4 import BeautifulSoup


class Assets:
    def __init__(self, url: str):
        self.url = url

    def pull_images(self):
        htmlcontent = requests.get(f"{self.url}").text
        noodle_soup = BeautifulSoup(htmlcontent, "html.parser")
        anchors = noodle_soup.find_all("img")
        filtered_list = list(set(anchors))

        return [self.url + str(link["src"]) for link in filtered_list]


print(Assets("https://thenishantsapkota.github.io/about.html").pull_images())
