from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

import time

NAME = "Madera Largo"
RELOAD_TIMEOUT = 1
ERROR_TIMEOUT = 5
NUM_CYCLES = 10
FIREFOX_PATH = "/Users/sgrover/Library/Application Support/Firefox/Profiles/9w4h7jdq.default"
#"/home/sgrover/.mozilla/firefox/7g9raps5.default"
PROFILE_PATH = "/Users/sgrover/Library/Application Support/Google/Chrome/"
#"/home/sgrover/.config/google-chrome"
EXECUTABLE_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
#"/opt/google/chrome/google-chrome"
DRIVER_PATH = "/usr/local/bin/chromedriver"

def print_last_msg(NAME, list_of_chatters):
    message = []
    for l in list_of_chatters:

        name = l.find('span', {'class':"emojitext ellipsify"}).get("title")
        if name == NAME:
            times = l.findAll("span", {"class":"chat-time"})
            msgs = l.findAll("span", {'class':"emojitext ellipsify"})
            tlist = ['\n' + t.getString() for t in times]
            mlist = [msg.getString() for msg in msgs]
            mlist.remove(name)

            from_me = l.findAll("span", {"class":"icon icon-status-dblcheck"}) + l.findAll("span", {"class":"icon icon-status-check"})
            if len(from_me) > 0:
                mlist.insert(0, u'Me')
            else:
                mlist.insert(0, name)

            message = message + tlist + mlist
    return message

# FIREFOX
# fp=webdriver.FirefoxProfile(FIREFOX_PATH)
# driver = webdriver.Firefox(fp)

# CHROME
#options = webdriver.ChromeOptions()
#options.add_argument("user-data-dir=" + PROFILE_PATH)
#driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

driver = webdriver.Chrome('./chromedriver')

# GET AND LOAD WHATSAPP
url="https://web.whatsapp.com/"
driver.get(url)

wf = open("messages.log", "a")
counter = 0
GLOBAL_MSG = []

while True and counter < 2:
    # LOAD PAGE
    time.sleep(RELOAD_TIMEOUT)   # seconds
    counter += 1

    # EXTRACT CURRENT PAGE SOURCE
    html_source = driver.page_source
    soup = BeautifulSoup(html_source)

    try:
        list_of_chatters =  soup.body.div.div('div', {'class':'app two'})[0]('div', {'id':'side'})[0].findAll('div', {'class':"chat-body"})

        print(" ****** \n", list_of_chatters, "\n **************")

        input("Pulse una teclara para continuar ... ... ... ... ... ... ... ") #for python 3k


        ext_msg_time = print_last_msg(NAME, list_of_chatters)

        WRITE_TO_FILE = False
        for m in ext_msg_time:
            if m not in GLOBAL_MSG:
                GLOBAL_MSG.append(m)
                print (GLOBAL_MSG)
                WRITE_TO_FILE = True

        if WRITE_TO_FILE:
            #print ext_msg_time
            for m in ext_msg_time:
                wf.write(m)
                wf.write('|')

    except:
        driver.get(url)
        time.sleep(ERROR_TIMEOUT)

    if counter%NUM_CYCLES == 0:
        wf.close()
        time.sleep(RELOAD_TIMEOUT)
        wf = open("messages.log", "a")