# Chapter 11.11


# Practice Project 3
# Play the 2048 game automatically with UP, RIGHT, DOWN, LEFT keystrokes.

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time, requests

browser = webdriver.Chrome()

browser.get('https://play2048.co/')

time.sleep(2)

game = browser.find_element_by_tag_name('body')

over = browser.find_element_by_class_name('retry-button')

control = ['\ue013','\ue014','\ue015','\ue012']

act = 0

while True:
     if over.is_displayed() is False:
         if act == 4:
             act = 0
         game.send_keys(control[act])
         act += 1
         
         time.sleep(0.1)

     else:
          print('Done')
          time.sleep(3)
          # over.click()      # Remove '#' to retry the game after finish.
          # break             # Remove '#' for one time play.
         


