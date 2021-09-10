# pylint: disable=missing-docstring,invalid-name
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.senscritique.com/films")

search_input = driver.find_element_by_id('_25jdusMm9PFEdy9TPVD0IK') # Open the inspector in Chrome and find the input id!
search_input.send_keys('james bond')

# driver.quit()