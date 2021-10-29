# SCRAPING IMPORTS
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
from datetime import datetime
import time

class ScraperHelper():
    def __init__(self):
        pass

    def scrapeMars(self):
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)

        # NASA Mars News
        url = "https://redplanetscience.com/"
        browser.visit(url)

        html = browser.html
        soup = BeautifulSoup(html, "lxml")

        news = soup.find("div", {"id": "news"})

        rows = news.find_all("div", {"class","row"})
        first_row = rows[0]

        title = first_row.find("div", {"class", "content_title"}).text
        paragraph = first_row.find("div", {"class", "article_teaser_body"}).text

        # JPL Mars Space Images - Featured Image
        url2 = "https://spaceimages-mars.com/"
        browser.visit(url2)

        html2 = browser.html
        soup2 = BeautifulSoup(html2, "lxml")

        image = soup2.find("img", {"class": "headerimage fade-in"})
        src = soup2.find("img", {"class": "headerimage fade-in"})["src"]
        
        featured_image_url = url2 + src

        # Mars News
        url3 = 'https://galaxyfacts-mars.com/'
        browser.visit(url3)

        tables = pd.read_html(url3)

        df=tables[0]

        df.columns = df.iloc[0]
        df= df[1:]

        html_table = df.to_html()

        # Mars Hemispheres
        url4 = "https://marshemispheres.com/"
        browser.visit(url4)

        html4 = browser.html
        soup4 = BeautifulSoup(html4, "lxml")

        hemis = soup4.find_all("div", {"class":"item"})

        hemi_page = []
        for hemi in hemis:
            hemi_url = url4 + hemi.find("a", {"class":"itemLink"})["href"]
            browser.visit(hemi_url)
            time.sleep(1)
            
            html4 = browser.html
            soup4 = BeautifulSoup(html4, "lxml")
            
            image_link = soup4.find("img", {"class","wide-image"})["src"]
            title = soup4.find("h2", {"class", "title"}).text
            
            info = {
                "image_url": image_link,
                "title":title
            }
            
            hemi_page.append(info)

            browser.quit()

            all_data = {
            "title":title,
            "paragraph": paragraph,
            "featured_image_url": featured_image_url,
            "mars_earth_facts": html_table,
            "hemispheres": hemi_page,
            "last_updated": datetime.utcnow()
            }

        return (all_data)