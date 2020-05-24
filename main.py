# made by Jack Conceprio
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
file = open("subChannels.txt","a")
email = ""
password = ""
addPostNotification = True
youtubeAccountAmount = int(input("how many youtube accounts do you want to sub to? must be int"))
youtubeAccountAmountArray = []
# this is where the chrome driver is located
chromeDriverFile = "includes\chromedriver.exe"

# this is when open up the google browser
browser = webdriver.Chrome(chromeDriverFile)

# this will go to the youtube page
browser.get("http://www.youtube.com")

# check to see if there login
if browser.find_element_by_xpath(
        '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button/yt-formatted-string').text == "SIGN IN":
    browser.find_element_by_xpath(
        '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button/yt-formatted-string').click()
    # find the email box
    browser.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(
        email + Keys.RETURN)
    # the reasons we have await is because the page doesn't load instant
    time.sleep(10)
    print("don't worry we are taking a 10 second nap")
    # find the password box
    browser.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(
        password + Keys.RETURN)
    # the reasons we have await is because the page doesn't load instant
    time.sleep(10)
    print("don't worry we are taking a 10 second nap")

    # this is count how many times it did not grab anything
    notGrabbedCounter = 0

    # this will run until youtubeAccountAmountArray is the same as youtubeAccountAmount
    while len(youtubeAccountAmountArray) <= youtubeAccountAmount:
        # this will get all the a tags
        a = browser.find_elements_by_tag_name("a")
        for i in a:
            # this will get the url to from the a tag
            link = i.get_attribute("href")
            # this will check if this is a youtube channel
            if str(link).find("channel") != -1:
                found = False
                for p in youtubeAccountAmountArray:
                    if link == p:
                        found = True
                        break
                if found == False:
                    youtubeAccountAmountArray.append(link)
                    print(link)
                    file.write(link+"\n")
                    print(len(youtubeAccountAmountArray))
        browser.refresh()
        counter = 0
    for i in youtubeAccountAmountArray:
        print(str(counter) + "/" +str(len(youtubeAccountAmountArray)-counter))
        counter = counter + 1
        browser.get(i)
        time.sleep(3)
        sub = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/ytd-subscribe-button-renderer/paper-button/yt-formatted-string')
        if sub.text != "SUBSCRIBED":
            sub.click()

        if addPostNotification == True:
            time.sleep(3)
            browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/ytd-subscribe-button-renderer/div[2]/ytd-subscription-notification-toggle-button-renderer/a/yt-icon-button/button').click()
            time.sleep(1)
            browser.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/iron-dropdown/div/ytd-menu-popup-renderer/paper-listbox/ytd-menu-service-item-renderer[1]/paper-item").click()