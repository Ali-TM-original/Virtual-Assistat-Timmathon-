import speech_recognition as sr
import os
import pyttsx3
import datetime
import wikipedia
import webbrowser
from selenium import webdriver

Chrome_path = 'C:\\Program Files (x86)\\chromedriver.exe'

chrome_driver = webdriver.Chrome(Chrome_path)
chrome_driver.get('https://youtube.com')

engine = pyttsx3.init()
engine.say('Sir, here is google')
engine.runAndWait()
