from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options 
import time
import openai 
from summa.summarizer import summarize
import urllib.request as urllib
options = Options()
options.add_argument("-headless") 
driver=webdriver.Firefox(options=options)
from datetime import date
from datetime import timedelta
today = date.today()
after = today - timedelta(days = 2)
#paste - write name
#var_inp=input('Write the name to search:')
var_inp= ' "za zabójstwo" | "za morderstwo" -youtube.com -gov.pl -facebook.com -wikipedia.org after:'+str(after)
url = 'https://www.google.com/'
driver.get('https://www.google.com/search?q=cats&source=lnms&tbm=isch')
time.sleep(2)
driver.find_element(By.XPATH,"//button[@aria-label='Accept all']").click()
time.sleep(2)
driver.get(url)
time.sleep(2)
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys(var_inp)
time.sleep(1)
search_box.submit()
time.sleep(5)

def chatverify(url2):
  openai.api_key = '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'
  completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ {"role": "user", "content": "Odpowiedz TAK lub NIE czy poniższy tekt opisuje casus kryminalny:"+ url2} ] )
  time.sleep(3)
  reply = completion.choices[0].message.content
  print(reply)
  if ("NIE" or "Nie") in reply:
     return False
  time.sleep(20)
  openai.api_key = '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'
  completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ {"role": "user", "content": "Odpowiedz na ile lat został skazany sprawca:"+url2} ] )
  wyrok = completion.choices[0].message.content
  time.sleep(20)
  openai.api_key = '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'
  completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ {"role": "user", "content": "Jakie były okoliczności zbrodni:"+url2} ] )
  operandi = completion.choices[0].message.content
  #print(wyrok)
  info = ( "Wyrok: "+wyrok +"Modus operandi: "+operandi)
  print(info)  
  return info


def wyrok(url2):
  openai.api_key = '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'
  completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ {"role": "user", "content": "Odpowiedz podając tylko liczbę na ile lat został skazany sprawca:"+ url2} ] )
  time.sleep(3)
  reply = completion.choices[0].message.content
  print(reply)
  return reply






from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
search = soup.find_all('div', class_="yuRUbf")
for links in search:
 sznurek = links.a.get('href')
 print(links.a.get('href'))
 wyrok(sznurek)
 print("Wait 20s")
 time.sleep(20)

driver.quit()
