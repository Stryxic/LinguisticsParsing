import requests
from bs4 import BeautifulSoup, SoupStrainer
import time
from axion import parse_content
# from seleniumrequests import Firefox, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

total_id = 1

def extractGroundArticles():
    url = "https://ground.news/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    total_articles = []
    # soup = BeautifulSoup(page.content, "html.parser")
    for link in BeautifulSoup(page.content, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if "/article/" in str(link):
                # print("-------------------")
                if link["href"] not in total_articles:
                    total_articles.append(link['href'])
                    


    # print(total_articles)

def pullArticles(service, url, article_name):
    driver = webdriver.Firefox()
    driver.maximize_window()
    all_urls = []

    driver.get(url)
    time.sleep(3)
    all_loaded = False
    while not all_loaded:
        time.sleep(2)

        try:
            button = driver.find_element("id", "more-stories")
        except NoSuchElementException:
            button = None
            print("Exception")

        if button:
            driver.execute_script("arguments[0].scrollIntoView();", button)
            driver.execute_script("window.scrollBy(0,-100)")
            time.sleep(1)
            button.click()
        else:
            all_loaded = True

    content = driver.page_source
    for link in BeautifulSoup(content, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr("href"):
            if "www" in link["href"] and "ground" not in link["href"]:
                all_urls.append(link["href"])
    # filename = "trump-davos"
    id = 1
    driver.close()
    total_id = 1
    for url in all_urls:
        page_content = scrape_text(url, service)
        if page_content:


        #JSON Signature integration
            # parse_content(parse_content, total_id)
            # total_id += 1




            f = open(f"articles/{article_name}-{id}.txt", "w", encoding="utf-8")
            id += 1
            # print(page_content)
            f.write(page_content)

def scrape_text(url, service):
    driver = webdriver.Chrome(service=service)
    driver.maximize_window() 
    driver.get(url)
    time.sleep(3)
    selenium_output = driver.execute_script(r"return [...document.body.querySelectorAll('p')].map((p) => p.outerText).filter(t => t !== '').map(t=> t.replace(/(\r\n|\n|\r)/gm, '').trim());")
    article_strings = [x for x in selenium_output[1:] if ("." or "?" or "!" or "'" or '"') in x]
    # print(" \n".join(article_strings))
    driver.close()
    return " \n".join(article_strings)

service=Service(ChromeDriverManager().install())


# content = scrape_text("https://www.sfchronicle.com/crime/article/ziz-zizians-rationalism-group-20149075.php", service)
# f = open("zizian.txt", "w", encoding="utf-8")
# f.write(content)


url = "https://ground.news/"
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
total_articles = []
# soup = BeautifulSoup(page.content, "html.parser")
for link in BeautifulSoup(page.content, 'html.parser', parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        if "/article/" in str(link):
            # print("-------------------")
            if link["href"] not in total_articles:
                total_articles.append(link['href'])
#url = "https://ground.news/article/trump-tells-davos-elite-to-invest-in-us-or-face-tariffs_a2c55c"
ground_urls = ["https://ground.news"+x for x in total_articles]
names = ["-".join(x.split("/")[2].split("-")[0:5]) for x in total_articles]

# print(ground_urls)
# print(names)

pos_count = 0

for i in range (0, len(ground_urls)):
    name = names[i]
    url = ground_urls[i]
    pullArticles(service, url, name)

for url in ground_urls:
    pullArticles(service)


