#pip install selenium
#pip install webdriver_manager
#pip install pandas
#pip install python-dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service  #to install chrome driver
from webdriver_manager.chrome import ChromeDriverManager  #to install chrome driver
from selenium.webdriver.chrome.options import Options  #to add options while creating driver object
from selenium.webdriver.common.by import By  #to use By parameter in find_elements method
import pandas as pd   #to work with dataframe and CSVs
import smtplib    #to create smtp client server object
from email.message import EmailMessage       #to create emails
import ssl   #to encrypt our email message
from dotenv import load_dotenv    #to load env vars
import os   #to fetch env vars
import json  #to create JSON
from  datetime import date  #to get current date


YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending?persist_gl=1&gl=US"  #for location -> USA


def get_driver():
    """
    Creates an instnace of selenium webdriver and returns an objects called 'driver'
    with required options and arguments like headless, chromedriver file location
    and browser location.
    """
    chrome_options = Options()  #creating an instance of Options() class
    #pass the browser location to selenium, otherwise it throws error
    try:
        chrome_options.binary_location = "/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    except:
        chrome_options.binary_location = "/usr/bin/google-chrome"
    chrome_options.add_argument("--headless")      #to not display the browser window
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def get_video_divs(driver):
    """
    It is used to collect only the (parent) divs from the webpage. Each parent divs contains the entire
    information about a single video like title, url, thumbnail_url, channel, views, uploaded time, description etc.
    returns a list of video div.
    """
    #companies can define their own tags in html, "ytd-video-renderer" is a tag developed by youtube
    driver.get(YOUTUBE_TRENDING_URL)
    video_div_tag = "ytd-video-renderer"
    video_divs = driver.find_elements(By.TAG_NAME, value=video_div_tag)
    return video_divs

def parse_video_div(video_div):
    """
    It is used to parse each parent video divs which contains the entire information
    about a single video like title, url, thumbnail_url, channel, views, uploaded time, description etc.
    Returns a dictionary of title, url, thumbnail_url, channel, views, uploaded time, description.
    """
    title_tag = video_div.find_element(By.ID, 'video-title')
    title = title_tag.text
    # title tag itself contains video URL, so let's use that to fetch video URL
    url = title_tag.get_attribute('href')

    thumbnail_tag = video_div.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')

    channel_name_div = video_div.find_element(By.CLASS_NAME, 'ytd-channel-name')
    channel_name = channel_name_div.text

    description = video_div.find_element(By.ID, 'description-text').text

    views_tag = video_div.find_element(By.ID, 'metadata-line')
    # views tag itself contains uploaded time, let's use it to fetch uploaded time
    if 'views' in views_tag.text:
        views = views_tag.text.split("\n")[0].split(" ")[0]
        uploaded_time = views_tag.text.split("\n")[1]
    else:  #for GoogleDoodles, views are N/A
        views = None
        uploaded_time = views_tag.text

    scraped_time = date.today().strftime("%d/%m/%Y")

    return {
        'title': title,
        'url': url,
        'thumbnail_url': thumbnail_url,
        'channel': channel_name,
        'views': views,
        'uploaded_time': uploaded_time,
        'scraped_time': scraped_time,
        'description': description
    }


def send_email(csv_name):
    load_dotenv()
    sender_email = os.getenv('EMAIL_ID')
    password = os.getenv('EMAIL_PASSWORD')
    receiver_email = os.getenv('EMAIL_ID')

    subject = 'YouTube Top 10 Trending Videos - Scraped CSV'
    body = 'Hi,\nPlease find the attached Top 10 Youtube Trending Videos CSV file from Web Scraper Project using Python'

    email_object = EmailMessage()      #creating an email message object to format email
    email_object['From'] = sender_email
    email_object['To'] = receiver_email
    email_object['Subject'] = subject
    email_object.set_content(body)   #to set the email content (body)

    with open(csv_name, 'rb') as file:
        email_object.add_attachment(file.read(),
                               maintype='application',
                               subtype='vnd.ms-excel',
                               filename=csv_name)

    context = ssl.create_default_context()

    #used with keyword to avoid using close method for server object at the end
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as ssl_server: # creating a server object with SSL
        ssl_server.login(sender_email, password)
        ssl_server.sendmail(sender_email, receiver_email, email_object.as_string())

if __name__ == '__main__':     #to run this code only if it's executed as a python file, not when used as a module
    print("Creating driver")
    driver = get_driver()
    print("Fetching the browser page for trending videos")
    video_divs = get_video_divs(driver)
    print(f'Found {len(video_divs)} videos')

    print('Parsing Top 10 Trending Videos')

    top_10_videos_data = [parse_video_div(video_div) for video_div in video_divs[:10]]

    videos_df = pd.DataFrame(top_10_videos_data)
    #print(videos_df)
    videos_df.to_csv('trending_videos.csv', index=None)
    print('CSV created')

    print('Sending Email')
    # body = json.dumps(top_10_videos_data, indent=2)
    send_email(csv_name='trending_videos.csv')
    print('Email Sent')

    driver.close()
    driver.quit()
