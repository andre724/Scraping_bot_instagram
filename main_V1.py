from Verifyer import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#import para salvar as fotos
import os 
import wget
#------------ Log in --------------------------------------------------------------------------------------------------------------------#
confirm='sim'
conta_count=0
contas_list=[]
dic_conta_posts={}

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    username = driver.find_element_by_name("username")

    password = driver.find_element_by_name("password")
    log_in = driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']")

except:
    driver.quit()

username.clear()
password.clear()
username.send_keys("")
password.send_keys("")
log_in.click()

try:
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
    not_now2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

except:
    driver.refresh()
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
    not_now2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()


#-------------------------------------Page Search and link scraping----------------------------------------------------------------------------------------------#

while  confirm=='sim':
    nome_conta= input('Nome da conta: ')
    if nome_conta != 0:
        dic_conta_posts.update({nome_conta:[]})
       
    confirm=input('Quer pesquisar mais contas?(sim/não) ')

for i in dic_conta_posts.keys():
    links=[]
    links_post=[]
    driver.get("https://www.instagram.com/" + i + "/")
    reached_page_end = False
    last_height = driver.execute_script("return document.body.scrollHeight")
    while not reached_page_end:
        elems=driver.find_elements_by_xpath("//a[@href]")
        for link in elems:
            links.append(link.get_attribute("href"))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
                reached_page_end = True
        else:
                last_height = new_height
    links_post=set(filter(lambda k: 'https://www.instagram.com/p/' in k, links))
    dic_conta_posts.update({i:links_post})

#-----------------Posts Scraping----------------------------------------------------------------------------------#

driver.close()
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

ptc=0
time.sleep(1)
for i in dic_conta_posts.keys():
    for x in dic_conta_posts[i]:
            driver.get(x)
            time.sleep(1)
            try:
                path=os.getcwd()
                path = os.path.join(path, i + '_posts')
                os.mkdir(path)
            except:
                pass
            try:
                check=verificador(driver)
                if check== 'r' or check== 'a':
                    print('under development')
                    time.sleep(2)
                elif check=='v':
                    video=driver.find_element_by_tag_name('video.tWeCl')
                    video= video.get_attribute('src')
                    save_v= os.path.join(path, i + '_post_'+ str(ptc) + '.mp4')
                    wget.download(video, save_v)
                    time.sleep(5)
                    ptc+=1
                else:
                    img= driver.find_element_by_tag_name('img.FFVAD')
                    img= img.get_attribute('src')
                    save_i= os.path.join(path, i + '_post_'+ str(ptc) + '.jpg')
                    wget.download(img, save_i)
                    time.sleep(5)
                    ptc+=1
            except:
                driver.refresh()
    




