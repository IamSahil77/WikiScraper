from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import pyttsx3

se=input("Enter a Topic you want to know : ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.wikipedia.org/')

container=driver.find_element(By.CLASS_NAME,'search-input')
search = container.find_element(By.TAG_NAME,"input")
search.send_keys(se)
time.sleep(0.2)

search.send_keys(Keys.ENTER)

title = driver.find_element(By.CLASS_NAME,'mw-page-title-main').text

para1 = driver.find_element(By.XPATH,'//p[1]').text
para2 = driver.find_element(By.XPATH,'//p[2]').text
para3 = driver.find_element(By.XPATH,'//p[3]').text

print(title,"\n")
print(para1,"\n")
print(para2,"\n")
print(para3,"\n")

filename = "content.csv"
with open(filename, "w", newline="") as out_file:
    writer = csv.writer(out_file)
    writer.writerow([title])
    try:
        writer.writerow([para1])
    except Exception as e:
        print(e)
    try:
        writer.writerow([para2])
    except Exception as e:
        print(e)
    try:
        writer.writerow([para3])
    except Exception as e:
        print(e)

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",148)
engine.say(title)
engine.say(para1)
engine.say(para2)
engine.say(para3)
engine.runAndWait()
