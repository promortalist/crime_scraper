from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#from selenium.webdriver.firefox.options import Options 
#from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
options = Options()
#options.add_argument("--headless")
#options.headless = True
#options.add_experimental_option("detach", True)
options.add_argument("--user-data-dir=/home/v/.config/google-chrome")
import undetected_chromedriver as uc
driver = uc.Chrome(options=options, service=Service(ChromeDriverManager().install()))
url='https://bard.google.com'
driver.get(url)
sleep(3)
prompt = "Kto jest królem Ubu w polsce?"
def query(prompt):
 text_area = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'rich-textarea > div > p')))
 text_area.send_keys(prompt)
 send_button = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="send-button-container"] > button'))) 
 send_button.click()
 sleep (6)
 WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.CSS_SELECTOR, 'message-content[class*="model-response-text"]')))
 response_elements = driver.find_elements(By.CSS_SELECTOR, 'message-content[class*="model-response-text"]')
 #response_element = driver.find_element(By.CSS_SELECTOR, 'message-content[class*="model-response-text"]')
 #response_text = response_element.text 
 answer= response_elements[-1].text
 return answer


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options 
import time
#from summa.summarizer import summarize
import urllib.request as urllib
options = Options()
#options.add_argument("-headless") 
driver=webdriver.Firefox(options=options)
from datetime import date
from datetime import timedelta
today = date.today()
after = today - timedelta(days = 2)

def search4 ():
 var_inp= ' "za molestowanie dziecka" | "za pedofilie" -youtube.com -gov.pl -facebook.com -wikipedia.org after:'+str(after)
 url = 'https://www.google.com/'
 driver.get('https://www.google.com/search?q=crime&source=lnms&tbm=isch')
 time.sleep(2)
#driver.find_element(By.XPATH,"//button[@aria-label='Accept all']").click()
 driver.find_element(By.XPATH, "//div[text()='Zaakceptuj wszystko']").click()
 time.sleep(2)
 driver.get(url)
 time.sleep(2)
 search_box = driver.find_element(By.NAME, 'q')
 search_box.send_keys(var_inp)
 time.sleep(1

def chatverify(url2):
  reply = query("Odpowiedz TAK lub NIE czy poniższy tekt opisuje casus kryminalny: "+ url2)
  #query("Powiedz TAK lub NIE czy poniższy tekt opisuje casus kryminalny:"+ url2)
  if ("NIE" or "Nie") in reply:
     return False
  wyrok =query("Odpowiedz na ile lat został skazany sprawca: "+url2)
  operandi = query("Jakie były okoliczności zbrodni: "+url2)
  info_dict = {"url": url2, "wyrok": wyrok, "opis": operandi}
  #info = ( "URL:" + url2,"Wyrok: "+wyrok +"Modus operandi: "+operandi)
  return info_dict


from typing import Dict

if isinstance(my_dict, Dict):
    # True
else:
    # False



search4()

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
search = soup.find_all('div', class_="yuRUbf")
for links in search:
 sznurek = links.a.get('href')
 print(links.a.get('href'))
 chatverify(sznurek)
 print("Wait 20s")
 time.sleep(20)
:
