# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep
from selenium.webdriver import ActionChains
import requests
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from colorama import init,deinit,Fore
from tqdm import tqdm
from selenium.webdriver import ActionChains
init(autoreset=True)
def refresh_open_sea_meta():
    # bored_nft_url="https://opensea.io/assets/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/"
    options = webdriver.ChromeOptions()
    #options.add_experimental_option('w3c', False)
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome('chromedriver',options=options)

    print(Fore.YELLOW+" example of assets url: https://opensea.io/assets/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/")
    print(Fore.RED+"> provide me with the exact url of ur collection:",end='')
    nft_assets_url=input()
    # nft_assets_url=bored_nft_url
    print("From which number u want to refresh:",end='')
    begin_number=10

    print("To which number u want to refresh:",end='')
    end_number=2800
    update_flag = "/?force_update=true"
    screenWidth, screenHeight = pyautogui.size()
    input("stop 10 seconds and put the cursor on the refresh button in the open sea page according to ur screen")
    sleep(10)
    currentMouseX, currentMouseY = pyautogui.position()
    for i in tqdm(range(int(begin_number),int(end_number))):
        url_to_direct_to=nft_assets_url+str(i) + update_flag
        #r = requests.get(url_to_direct_to)
        #print(i, r.status_code)
        driver.get(nft_assets_url+str(i))
        #----------remove those--------
        header = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/div/div[2]")
        all_children_by_xpath = header.find_elements_by_xpath(".//*")
        #------remove those------
        sleep(0.1)
        pyautogui.moveTo(currentMouseX, currentMouseY)  # Move the mouse to the x, y coordinates 100, 150.
        pyautogui.click()
        #NEEDED_______________________________
        # screenWidth, screenHeight = pyautogui.size()
        # input("stop 10 seconds and put the cursor on the refresh button")
        # sleep(10)
        # currentMouseX, currentMouseY = pyautogui.position()
        #--------------------NEEDED----------------------


        sleep(2)
    print("Updating MetaData of Collection is finished")
def main(name):
    print(Fore.RED+"> provide me with the exact collection name:")
    nft_collection_name=input()
    options = webdriver.ChromeOptions()
    #options.add_experimental_option('w3c', False)
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome('./chromedriver',options=options)
    driver.get("https://opensea.io")
    #focus on the search collection button
    search_bar = driver.find_element(By.XPATH,
        "/html/body/div[1]/div/div[2]/nav/div[2]/div/div/div/input")
    search_bar.send_keys(Keys.NULL)
    search_bar.sendKeys(nft_collection_name)
    search_bar.submit()
    asdf=0
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    refresh_open_sea_meta()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
deinit()