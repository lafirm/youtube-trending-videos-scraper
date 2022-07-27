import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"


#requests library doesnt execute javascripts (dynamic contents)
response = requests.get(YOUTUBE_TRENDING_URL)  #downloads the webpage source code as text

print("Status Code: ", response.status_code)
# print("Output Text: ", response.text[:1000])


doc = BeautifulSoup(response.text, 'html.parser')

print('Page Title: ', doc.title.text)


#find all the video divs

video_divs = doc.find_all('div', class_='ytd-video-renderer')

print(f'Found {len(video_divs)} videos')

"""We need selenium, chromedriver and browser altogether to do the job, but replit has it pre-installed"""










