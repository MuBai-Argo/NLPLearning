import traceback
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
script_driver = webdriver.Chrome()

driver.get("https://trow.cc/board/s=7eb1059ef50761992f138277eaaf8bdc&showforum=82")

train_text = []
test_text = []
script_text = ""


def turn_page(driver):
    buttons = driver.find_elements(By.CLASS_NAME, 'pagelink')
    button = buttons[-1]
    button.click()
    sleep(2)

def get_text(script_driver):
    # '//*[@id="post-211598"]'
    # '//*[@id="post-211562"]'
    # '//*[@id="post-211268"]'
    # '/html/body/div/div[7]/table[1]/tbody/tr[2]/td[2]/div[1]/div'
    # '/html/body/div/div[7]/table[1]/tbody/tr[2]/td[2]/div[1]/div'
    try:
        script = script_driver.find_element(By.XPATH, '/html/body/div/div[7]/table[1]/tbody/tr[2]/td[2]/div[1]/div')
        print(script)
        print(script.text)
        return script.text
    except:
        print("ERROR2")

num = 1
def get_page(driver, i):
    # '/html/body/div/div[9]/table/tbody/tr/td[3]/div[2]/span/a'
    # '/html/body/div/div[9]/table/tbody/tr[9]/td[3]/div[2]/span/a'
    script_links = []
    script_text = ""
    links = driver.find_elements(By.XPATH, '/html/body/div/div[9]/table/tbody/tr/td[3]/div[2]/span/a[1]')
    print(links)

    try:
        for link in links:
            # print(link.text)
            if "[译]" in link.text or "原创" in link.text:
                print(link.text)
                print(link.get_attribute("href"))
                # script_links.append(link.get_attribute("href"))
                script_driver.get(link.get_attribute("href"))
                script_text = get_text(script_driver)
                with open("克苏鲁神话-训练语料"+str(i)+".txt", "w", encoding="utf-8")as f:
                    f.write(script_text)
                sleep(4)
                i += 1
    except Exception :
        print("ERROR1")
    finally:
        sleep(2)
        return i



# try:
# finally:
#     sleep(2)
#     driver.close()
try:
    for i in range(2):
        num = get_page(driver, num)
        turn_page(driver)
except:
    print("ERROR3")
finally:
    driver.close()
    script_driver.close()





