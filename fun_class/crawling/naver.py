import requests 
from bs4 import BeautifulSoup

def crawling(soup):
  div = soup.find("div", class_ = "list_issue")
  # print(div)
  result = []
  
  for a in div.find_all("a"):
    # print(a.get_text())
    result.append(a.get_text())

  links = []
  for a in div.find_all("a"):
    # print(a['href'])
    # result.append(a.get_text())
    links.append(a['href'])

  print(result)
  print(links)

  return None


def main():

  url = "https://www.naver.com/"
  req = requests.get(url)
  soup = BeautifulSoup(req.text, "html.parser")

  print(crawling(soup))

if __name__ == "__main__":
  main()













