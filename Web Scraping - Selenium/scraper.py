import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import smtplib
import os

trending_youtube_url = 'https://www.youtube.com/feed/trending?bp=4gIKGgh0cmFpbGVycw%3D%3D'


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-setuid-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_videos(driver):
    video_div_class = 'ytd-video-renderer'
    #print("Fetching the page title...")
    #print(driver.title)
    driver.get(trending_youtube_url)
    videos = driver.find_elements(By.TAG_NAME, video_div_class)
    return videos


def parse_videos(video):
    #title, url, thumbnail, channel name, views, uploaded date and description
    title_tag = video.find_element(By.ID, 'video-title')
    title = title_tag.text
    url = title_tag.get_attribute('href')

    thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')

    channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
    channel = channel_div.text

    views = video.find_element(By.XPATH,
                               '//*[@id="metadata-line"]/span[1]').text
    uploaded = video.find_element(By.XPATH,
                                  '//*[@id="metadata-line"]/span[2]').text

    description_tag = video.find_element(By.ID, 'description-text')
    description = description_tag.text

    return {
        'title ': title,
        'url ': url,
        'thumbnail_url ': thumbnail_url,
        'channel name ': channel,
        'views ': views,
        'uploaded ': uploaded,
        'description ': description
    }


def send_email(body):
  
  SENDER = 'trendtrendy2022@gmail.com'
  RECEIVER = 'trendtrendy2022@gmail.com'
  PASSWORD = os.environ['gmail_password']
  
  subject = 'YouTube Trending Movies'

  email_text = f""" 
  From: {SENDER}
  To: {RECEIVER}
  Subject: {subject}
  
  {body}
  """
  try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    server_ssl.ehlo()
    server_ssl.starttls()
    print(email_text)
    server_ssl.login(SENDER, PASSWORD)
    server_ssl.sendmail(SENDER, RECEIVER, email_text)
    server_ssl.close()

    print('Email sent!')
  except:
    print('Something went wrong...')


if __name__ == "__main__":
    print("Creating driver...")
    driver = get_driver()

    print("Fetching trending videos...")
    videos = get_videos(driver)
    print(f'Found {len(videos)} videos.')

    print("Parsing Top 10 trending movies")
    video_data = [parse_videos(video) for video in videos[:10]]
    # print(video_data)

    # print('Save the data to csv')
    # videos_df = pd.DataFrame(video_data)
    # print(videos_df)

    # videos_df.to_csv('YT_trending_movies.csv', index=None)

    print('Send YT scrapped data to email')
    body = json.dumps(video_data, indent=2)
    send_email(body)

  #Attachment to emauk 

  #Send and update data to Google Sheets 
