from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options 
import time
import openai 
#from summa.summarizer import summarize
import urllib.request as urllib
options = Options()
#options.add_argument("-headless") 
driver=webdriver.Firefox(options=options)
from datetime import date
from datetime import timedelta
today = date.today()
after = today - timedelta(days = 2)
#paste - write name
#var_inp=input('Write the name to search:')
#var_inp= ' "za zabójstwo" | "za morderstwo" -youtube.com -gov.pl -facebook.com -wikipedia.org after:'+str(after)
#url = 'https://www.google.com/'
#driver.get('https://www.google.com/search?q=cats&source=lnms&tbm=isch')
##driver.find_element(By.XPATH,"//button[@aria-label='Accept all']").click()
#driver.get(url)
#search_box = driver.find_element(By.NAME, 'q')
#search_box.send_keys(var_inp)
#search_box.submit()


#import sqlite3 
#db = 'crimes.db' 
#conn = sqlite3.connect(db)
#print('connected') 
#print(conn) 

def search1 ():
 var_inp= ' "za zabójstwo" | "za morderstwo" -youtube.com -gov.pl -facebook.com -wikipedia.org after:'+str(after)
 url = 'https://www.google.com/'
 driver.get('https://www.google.com/search?q=cats&source=lnms&tbm=isch')
 time.sleep(2)
 driver.find_element(By.XPATH,"//button[@aria-label='Accept all']").click()
 driver.find_element(By.XPATH, "//div[text()='Zaakceptuj wszystko']").click()
 time.sleep(2)
 # nowosc
 url = "https://www.perplexity.ai/"
 driver.get(url)
 time.sleep(2)
 search_box = driver.find_element(By.NAME, 'q')
 search_box.send_keys(var_inp)
 time.sleep(1)
 search_box.submit()
 time.sleep(5)


def search2 ():
 var_inp= ' "za nękanie" | "za stalking" | "nękał latami" | "nękał mięsiącami"  -youtube.com -gov.pl -facebook.com -wikipedia.org after:'+str(after)
 url = 'https://www.google.com/'
 driver.get('https://www.google.com/search?q=cats&source=lnms&tbm=isch')
 time.sleep(2)
 driver.find_element(By.XPATH,"//button[@aria-label='Accept all']").click()
 driver.find_element(By.XPATH, "//div[text()='Zaakceptuj wszystko']").click()
 time.sleep(2)
 driver.get(url)
 time.sleep(2)
 search_box = driver.find_element(By.NAME, 'q')
 search_box.send_keys(var_inp)
 time.sleep(1)
 search_box.submit()
 time.sleep(5)
 
 
def search3 ():
 var_inp= ' "za molestowanie" | "za przestępstwo seksualne" -youtube.com -gov.pl -facebook.com -wikipedia.org after:'+str(after)
 url = 'https://www.google.com/'
 driver.get('https://www.google.com/search?q=cats&source=lnms&tbm=isch')
 time.sleep(2)
 #driver.find_element(By.XPATH,"//button[@aria-label='Accept all']").click()
 driver.find_element(By.XPATH, "//div[text()='Zaakceptuj wszystko']").click()
 time.sleep(2)
 driver.get(url)
 time.sleep(2)
 search_box = driver.find_element(By.NAME, 'q')
 search_box.send_keys(var_inp)
 time.sleep(1)
 search_box.submit()
 time.sleep(5)
#return driver.page_source
 

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
 time.sleep(1)
 search_box.submit()
 time.sleep(5)


import openai
openai.api_key = 'sk-None-RqPdpmbMXYP787AJxuDAT3BlbkFJvhrUQLH6LeFX6SZlkFLu'
def comp(PROMPT, MaxToken=50, outputs=3): 
    # using OpenAI's Completion module that helps execute  
    # any tasks involving text  
    response = openai.Completion.create(model='gpt-3.5-turbo-instruct', prompt=PROMPT, max_tokens=MaxToken, n=outputs, output = list())
    for k in response['choices']: 
        output.append(k['text'].strip() 
    return output

def chatverify(url2):
  openai.api_key = 'sk-None-RqPdpmbMXYP787AJxuDAT3BlbkFJvhrUQLH6LeFX6SZlkFLu'
  completion = openai.ChatCompletion.create( model='gpt-3.5-turbo-instruct', messages=[ {"role": "user", "content": "Odpowiedz TAK lub NIE czy poniższy tekt opisuje casus kryminalny:"+ url2} ] )
                      #completion = openai.ChatCompletion.create( model=gpt-3.5-turbo, messages=[ {"role": "user", "content": "Odpowiedz TAK lub NIE czy poniższy tekt opisuje casus kryminalny:"+ url2} ] )
                      # PROMPT = "Za jakie przestępstwa jest dożywocie?"
                      #reply = comp(PROMPT, MaxToken=3000, outputs=1)
  time.sleep(3)
  reply = completion.choices[0].message.content
  print(reply)
  if ("NIE" or "Nie") in reply:
     return False
  time.sleep(20)
  openai.api_key = 'sk-None-RqPdpmbMXYP787AJxuDAT3BlbkFJvhrUQLH6LeFX6SZlkFLu'
  completion = openai.ChatCompletion.create( model='gpt-3.5-turbo-instruct', messages=[ {"role": "user", "content": "Odpowiedz na ile lat został skazany sprawca:"+url2} ] )
  wyrok = completion.choices[0].message.content
  time.sleep(20)
  openai.api_key = 'sk-None-RqPdpmbMXYP787AJxuDAT3BlbkFJvhrUQLH6LeFX6SZlkFLu'
  completion = openai.ChatCompletion.create( model='gpt-3.5-turbo-instruct', messages=[ {"role": "user", "content": "Jakie były okoliczności zbrodni:"+url2} ] )
  operandi = completion.choices[0].message.content
  print(wyrok)
  info = ( "Wyrok: "+wyrok +"Modus operandi: "+operandi)
  print(info)  
  return info


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

driver.quit() 
