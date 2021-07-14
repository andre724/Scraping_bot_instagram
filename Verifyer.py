from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def verificador(driver):
    try:
        if driver.find_element_by_tag_name('button._6CZji').is_enabled():

            return 'a'
    except:
        try:
            if driver.find_element_by_tag_name('video.tWeCl').is_enabled():
                video=driver.find_element_by_tag_name('video.tWeCl')
                video= video.get_attribute('src')
                if video[0] == 'b':
                    return 'r'
                else:
                    return 'v'
        except:
            if driver.find_element_by_tag_name('img.FFVAD').is_enabled():
                return 'i'
