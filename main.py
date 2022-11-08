import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#web page:
url = 'https://www.olx.pl/'
browser = webdriver.Chrome()
browser.get(url)

#waiting for cookie box to appear
time.sleep(2)

#clicing box
accept_box = browser.find_element(By.ID,"onetrust-accept-btn-handler")
accept_box.click()
time.sleep(0.5)

#text box fill
text_box = browser.find_element(By.NAME,"q")
text_box.send_keys("reign")

time.sleep(1)

#search
search = browser.find_element(By.XPATH, '//*[@id="submit-searchmain"]')
search.click()
time.sleep(2)


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

            #Item filter by cost
            if number_int > 5000 and number_int < 10000 :

                #Printing results
                print(name.text, " ------ ", number_int, "zł")

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