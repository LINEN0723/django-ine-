import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
class Stok(ABC):
    def __init__(self, area):
        self.area = area
 # 地區
    @abstractmethod
    def scrape(self):
        pass
class IFoodie(Stok):
    def scrape(self):
        url = ('https://invest.cnyes.com/twstock/TWS/'+self.area)  
        web = requests.get(url)                          # 取得網頁內容
        soup = BeautifulSoup(web.text, "html.parser")
        content =""    # 轉換內容
        title=soup.find(class_='jsx-2715122309 header_second')  .getText()         
        # 找到 h1 的內容
        a=(soup.find( class_='jsx-2214436525 info-lp')).getText()    
        b=(soup.find( class_='jsx-2214436525 change-net')).getText()
        c=soup.find( class_='jsx-2214436525 change-percent').getText()
        content +=(f'{title}\n股價:\n{a}\n{b}\n{c} ')
        return content
