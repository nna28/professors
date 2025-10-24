
from typing import Dict, List
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from GraphBuilder.utils.custom_queue import CustomQueue


seeds = [
    "/wiki/Danh_s%C3%A1ch_ng%C6%B0%E1%BB%9Di_%C4%91o%E1%BA%A1t_gi%E1%BA%A3i_Nobel_V%E1%BA%ADt_l%C3%BD",
    "/wiki/Danh_s%C3%A1ch_ng%C6%B0%E1%BB%9Di_%C4%91o%E1%BA%A1t_gi%E1%BA%A3i_Nobel_H%C3%B3a_h%E1%BB%8Dc",
    "/wiki/Danh_s%C3%A1ch_ng%C6%B0%E1%BB%9Di_%C4%91o%E1%BA%A1t_gi%E1%BA%A3i_Nobel_V%C4%83n_h%E1%BB%8Dc"
]

my_headers = {
    'User-Agent': 'ScienceNetworkBot/1.0 (mailto:hnc203204@gmail.com)'
}




def get_infobox(data) -> BeautifulSoup:
    # print(data.prettify())
    for e in data.find_all("table"):
        if "infobox" in e.get("class"):
            return e


    return None



def processed(link) -> List[str]:
    page = requests.get(f"https://vi.wikipedia.org{link}", headers=my_headers)

    soup = BeautifulSoup(page.content, "html.parser")
    wiki_tables = soup.find_all("table", class_ = "wikitable")
    try:
        print(get_infobox(soup).prettify().encode("utf-8"))
    except Exception as e:
        print(e)
    hrefs = []
    for table in wiki_tables:
        for link in table.find_all("a"):
            hrefs.append(link.get("href"))
    return hrefs


def bfs(seeds: List[str]):
    q: CustomQueue = CustomQueue()

    for link in seeds:
        # print(link)
        q.enqueue(link)

    visited: Dict[str, bool] = defaultdict(lambda: False)

    while not q.isEmpty():
        link = q.dequeue()
        print(link)
        visited[link] = True
        for new_link in processed(link):
            if not visited[new_link]:
                q.enqueue(new_link)


if __name__ == "__main__":
    processed("/wiki/Henri_Becquerel")





