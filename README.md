# YouTube's Trending Videos Scraper
Scrape top 10 trending videos on YouTube using [**Selenium**](https://selenium-python.readthedocs.io/) and Automate the process using [**Github Actions**](https://docs.github.com/en/actions) with [Cron Jobs](https://www.freecodecamp.org/news/cron-jobs-in-linux/).

## Project Outline
Initially, we tried to scrape the contents of trending YouTube video using [**BeautifulSoup4**](https://beautiful-soup-4.readthedocs.io/en/latest/) but it was not successful, since [YouTube's Trending page](https://www.youtube.com/feed/trending?persist_gl=1&gl=US) is dynamic.
Hence we used [**Selenium**](https://selenium-python.readthedocs.io/) along with chromedriver and chromium browser to scrape.

Read [this article](https://www.pluralsight.com/guides/guide-scraping-dynamic-web-pages-python-selenium) to know more about Scraping Dynamic Web Pages with Python and Selenium.

Mainly there are 2 sections involved in our project:

1. Scrape, Store and Share
2. Automation

# 1. Scrape, Store and Share

In this section, we did the following:
  - Scraped the top 10 trending videos on YouTube using Python and Selenium
  - Store the scraped content in CSV format in a separate folder
  - Share the CSV file via email using `smtplib` library

## Scrape
Install the required libraries by running the following command,

`pip install requirements.txt`

Then import the libraries.

`get_driver()` function is used to create an instance of selenium webdriver which accepts the path for chromium browser and installs chromedriver using this method `Service(ChromeDriverManager().install())`.

## Store


## Share


# 2. Automation

We chose Github Actions to automate the process, because it has many advantages over other services like AWS Lambda, GCP, Heroku etc. And the most important advantage is that it's free and we don't have to provide Credit Card details.

To automate our Python script using Github Actions, we need to create a `.YML` file inside a directory `workflows` and the format should be like.

> .github/workflows/actions.yml

## How Workflow was created in Github Actions?

### Create YAML file

### Use Cron Jobs

### Install Python

### Install Chromedriver and Chromium Browser

After a while, found this [block of codes](https://github.com/SeleniumHQ/selenium/blob/5d108f9a679634af0bbc387e7e3811bc1565912b/.github/actions/setup-chrome/action.yml) provided by selenium to install Chromedriver and Chromium Browser on Github Actions for automation.

https://github.com/lafirm/youtube-trending-videos-scraper/blob/31fe5633cabb462d79c3464174241303858cf2a2/.github/workflows/auto-scraper.yml#L33-L50


### Execute python script

  - Use env variables

### commit and push changes


---


readme will be updated soon!
