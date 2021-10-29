from flask import Flask, render_template, redirect
from scrapinghelper import ScraperHelper
from mongohelper import MongoHelper

app = Flask(__name__)

# global helper classes
mongoHelper = MongoHelper()
scraperHelper = ScraperHelper()

# HTML Renders
@app.route("/")
def index():
    scrape_info = mongoHelper.findLastInfo()
    return render_template("index.html", mars=scrape_info)

# BUTTON Routes
@app.route("/scrape")
def scrapeMars():
    data = scraperHelper.scrapeMars()
    response = mongoHelper.insertInfo(data)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)