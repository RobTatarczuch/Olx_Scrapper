import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


ad_list = {}


def saving_in_dir(name,cost,ad_list): #Saving ads in dictionary
    ad_list[name] = cost
    return ad_list

def avg_price(ad_list):
    number_of_items  = len(ad_list.values())
    total_sum = 0
    for i in ad_list.values():
        total_sum = total_sum + i

    price_avg = total_sum / number_of_items


    print("Avarege price: ",round(price_avg))

#web page:
url = 'https://www.olx.pl/'
browser = webdriver.Chrome()
browser.get(url)

#waiting for cookie box to appear
time.sleep(5)

#clicing box
accept_box = browser.find_element(By.ID,"onetrust-accept-btn-handler")
accept_box.click()
time.sleep(0.5)

#text box fill
text_box = browser.find_element(By.NAME,"q")
text_box.send_keys("gambler")

time.sleep(1)

#search
search = browser.find_element(By.XPATH, '//*[@id="submit-searchmain"]')
search.click()
time.sleep(2)

text_box = browser.find_element(By.NAME,"range-from-input")
text_box.send_keys("5000")
time.sleep(5)

#page changing loop
while True:
    time.sleep(0.5)
    ads = ""
    ads = browser.find_elements(By.CLASS_NAME, "css-u2ayx9")

    #ad search
    for ad in ads:
        j = 0
        number_string = ""
        number_int = 0

        #remove sponsored ads and ad without prices
        try:
            name = ad.find_element(By.TAG_NAME,"h6")
            cost = ad.find_element(By.TAG_NAME,"p")

            #Loop that change text to numbers
            for i in cost.text:
                if i in "0123456789":
                    number_string += i

            #condition that eliminate "Zamienie"
            if number_string != '':
                number_int = int(number_string)
            else:
                continue

            #name check
            name_check = name.text
            name_check =  name_check.lower()

            #Item filter by cost and name
            if number_int > 5000 and number_int < 15000 and "gambler" and "scott" in name_check:
              #Saving ads
              saving_in_dir(name.text, number_int, ad_list)

        except selenium.common.exceptions.NoSuchElementException:
            continue

    #try moving to next page, or stop program
    try:
        time.sleep(1)
        page_list = browser.find_element(By.CLASS_NAME,'css-j8u5qq')
        next = page_list.find_element(By.CSS_SELECTOR,'[data-testid="pagination-forward"]')
        next.click()
        time.sleep(1)
        continue
    except:
        break


for key, item in ad_list.items():
    print(key,"****", item)

avg_price(ad_list)