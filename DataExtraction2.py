from selenium import webdriver
from bs4 import BeautifulSoup as Soup
from threading import Thread
import time
import math

from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys


def read_from_txt(path):
    '''
    (str) -> list of str
    Loads up all sites from the .txt file in the root directory.
    Returns the sites as a list
    '''
    # Initialize variables
    raw_lines = []
    lines = []

    # Load data from the txt file
    try:
        f = open(path, "r")
        raw_lines = f.readlines()
        f.close()
    # Raise an error if the file couldn't be found
    except:
        print("Couldn't locate <" + path + ">.")

    # Parse the data
    for line in raw_lines:
        lines.append(line.strip("\n"))

    # Return the data
    return lines


def get_data(endpoint):
    # Set up Selenium session
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('window-size=1200x600')

    s = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    hospitals = read_from_txt("Errors.txt")
    # GET page
    s.get(endpoint)
    '''
    count = 0
    count2 = 1
    for tr in s.find_elements_by_xpath('/html/body/form/div[3]/section/div[1]/div[1]/div/div/div/div[4]/div/div[4]/div/div[2]/div[3]/div/div/div[2]/div/div/table/tbody'):
        tds = tr.find_elements_by_tag_name('td')
        while count2 < len(tds):
            print(tds[count].text + ", " + tds[count2].text + "\n")
            count += 2
            count2 += 2
            file = open("ER_Ontario.txt", "a")
            file.write(tds[count].text + ", " + tds[count2].text + "\n")
            #file.write(str([td.text for td in tds]) + "\n")
            file.close()
    '''
    count = 0
    while count < len(hospitals):
        count += 1
        s.find_element_by_xpath('/html/body/form/div[3]/section/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/section/input').send_keys(hospitals[count])
        time.sleep(1)
        s.find_element_by_xpath(
            '/html/body/form/div[3]/section/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/section/input').send_keys(u'\ue015')
        time.sleep(1)
        s.find_element_by_xpath(
            '/html/body/form/div[3]/section/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/section/input').send_keys(u'\ue007')
        time.sleep(1)

        if hospitals[count] == s.find_element_by_xpath(
        '/html/body/form/div[3]/section/div[1]/div[1]/div/div/div/div[4]/div/div[3]/p[1]/span[1]').text:
            s.find_element_by_xpath('/html/body/form/div[3]/section/div[1]/div[1]/div/div/div/div[4]/div/div[4]/div/div[4]/div/button[2]').click()
            time.sleep(1)
            s.find_element_by_xpath(
                '/html/body/form/div[3]/section/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/section/input').clear()
            time.sleep(1)
        else:
            s.find_element_by_xpath(
                '/html/body/form/div[3]/section/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/section/input').clear()
            time.sleep(1)
            file = open("Errors.txt", "a")
            file.write(hospitals[count] + "\n")
            file.close()
    s.quit()


if(__name__ == "__main__"):
    # Read links
    #data = read_from_txt("ER_Ontario_List.txt")
    # Test
    data = 'https://www.hqontario.ca/System-Performance/Time-spent-in-emergency-departments'
    get_data(data)
