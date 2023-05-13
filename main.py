from selenium import webdriver
from selenium.webdriver.common.by import By
from pytube import YouTube

basedurl = '*playlistlink*'
driver = webdriver.Edge()
driver.get(basedurl)
elements = driver.find_elements(By.ID, 'video-title')
links = [elem.get_attribute('href') for elem in elements]
driver.close()
for link in links:
    yt = YouTube(link)
    yt.streams.get_audio_only().download(output_path="music") #для скачивания музыки
    yt.streams.get_by_resolution('1080p').download(output_path='video') #для скачивания видео