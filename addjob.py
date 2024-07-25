from job import Job
from urllib.request import Request, urlopen
from chercherimage import Chercherimage
from bs4 import BeautifulSoup



URL = "https://www.enchantedlearning.com/wordlist/jobs.shtml"
req = Request(URL , headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")
results = soup.find_all("div", class_="wordlist-item")
print(results)
jobdb=Job()
name=None
for link in results:
        name=link.get_text()
        #picf=Chercherimage("woman "+name).dlpic()["nom"]
        #picm=Chercherimage("man "+name).dlpic()["nom"]
        #jobdb.create({"name":name,"picf":picf,"picm":picm})
        jobdb.create({"name":name})
                      
