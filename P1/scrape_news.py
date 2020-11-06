from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

## In the following segment, we show how you can get a list of news article URLs based on a keyword search.
## We use Jacobin mag as an example but we recommend you scrape more mainstream/well-known and neutral news sources.

list_url = "https://jacobinmag.com/search?query=coronavirus"

uClient = uReq(list_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "https://jacobinmag.com"
text_sections = page_soup.find("div", {"class": "ar-mn__articles"}).find_all("a")
## The previous line will not be the same for all websites. Go to the desired website on your browser, right-click and do "Inspect element"
## to see how the website HTML is structured. This will take a bit of time and patience
article_urls = [] 

for i in text_sections:
    #print(i.href)
    if "/2020/" in i.get("href"):
        t = domain_url + i.get("href")
        print(t)
        article_urls.append(t)


                    
### The following is some code to show how you would extract each news article. For multiple URLs, 
### iterate over the list of URLs you scraped in the previous step.

cnn_url = "https://www.cnn.com/2020/04/19/us/ohio-inmates-coronavirus/index.html"
jacobin_url = "https://jacobinmag.com/2020/02/coronavirus-outbreak-free-market-pharmaceutical-industry"
# for CNN:
# <div class="zn-body__paragraph"> text </div>
# for Jacobin:
# <div id="post-content" class="po-cn__intro.po-wp__intro">


def text_from_html(read_html, site):
    page_soup = soup(read_html, "html.parser")
    if site=="cnn":
        text_sections = page_soup.find_all("div", {"class": "zn-body__paragraph"})
        joined_texts = ""
        for i in text_sections:
            joined_texts += i.text
        return joined_texts
    elif site=="jacobin":
        text_sections = page_soup.find("div", {"id": "post-content"}).find_all("p")
        joined_texts = ""
        for i in text_sections:
            joined_texts += i.text
        return joined_texts


## main

uClient = uReq(jacobin_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")

headline = page_soup.find("h1", {"class": "po-hr-cn__title"})
text_sections = page_soup.find("div", {"id": "post-content"}).find_all("p")
# These two lines will also vary across websites. Inspect element to find out how you should extract the text.

article = ""
for i in text_sections:
    article += i.text


print(headline.text) #headline printed for demo
print(article) #printed just for demo, you need to store it, maybe in a csv file
