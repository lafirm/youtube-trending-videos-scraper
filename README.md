# YouTube Trending Videos Scraper
Scrape top 10 trending videos on YouTube using [**Selenium**](https://selenium-python.readthedocs.io/) and Automate the process using [**Github Actions**](https://docs.github.com/en/actions) with CRON.

## Project Outline
Initially, we tried to scrape the contents of trending YouTube video using [**BeautifulSoup4**](https://beautiful-soup-4.readthedocs.io/en/latest/) but it was not successful, since [YouTube's Trending page](https://www.youtube.com/feed/trending?persist_gl=1&gl=US) is dynamic.
We have to use [**Selenium**](https://selenium-python.readthedocs.io/) to scrape.



















## How Workflow was created in GithubActions?



### Install Chromedriver and Chromium Browser

After a while, found this [block of codes](https://github.com/SeleniumHQ/selenium/blob/5d108f9a679634af0bbc387e7e3811bc1565912b/.github/actions/setup-chrome/action.yml) provided by selenium to install Chromedriver and Chromium Browser on Github Actions for automation.

https://github.com/lafirm/youtube-trending-videos-scraper/blob/31fe5633cabb462d79c3464174241303858cf2a2/.github/workflows/auto-scraper.yml#L33-L50

















Readme will be updated soon.

