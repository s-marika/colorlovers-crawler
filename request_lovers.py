import re
from time import sleep
import csv

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# set result file path
result_data_colors_path = "./result_color_palletes.csv"
result_data_eval_path = "./result_color_eval.csv"
# set page number
page_num = 6

colors = []  # result of color data
evals = []  # result of eval data

# set driver option and start Chrome driver in headless
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

with open(result_data_colors_path, 'w') as fwc, open(result_data_eval_path, 'w') as fwe:
    writer_c = csv.writer(fwc)
    writer_e = csv.writer(fwe)

    # access to page url and scrape element
    for page in range(page_num):
        url = f"https://www.colourlovers.com/palettes/most-favorites/all-time/meta?page={page + 1}"
        driver.get(url)
        sleep(2)  # wait for browser create page elements

        html = driver.page_source.encode('utf-8')
        # print(html)

        # scrape color data
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.select("div.detail-row")
        # print(rows)
        for r in rows:
            cs_wrapper = r.select("a.palette")[0]
            cs = cs_wrapper.select("div.c")
            writer_c.writerow([re.search(r'#[a-zA-Z0-9]{3,6}', color['style'].split(";")[-2]).group() if re.search(
                r'#[a-zA-Z0-9]{3,6}', color['style'].split(";")[-2]).group() else None for color in cs])
            # colors.append([re.search(r'#[a-zA-Z0-9]{3,6}', color['style'].split(";")[-2]).group() if re.search(r'#[a-zA-Z0-9]{3,6}', color['style'].split(";")[-2]).group() else None for color in cs])

            meta_d = r.select('div.meta > div.right-col')
            writer_e.writerow([data.select_one('h4').text if data.select_one(
                'h4').text else None for data in meta_d][::-1])
            #evals.append([data.select_one('h4').text if data.select_one('h4').text else None for data in meta_d][::-1])
        ##print("accsess to url: ", url)
        # print(colors)

# confirm color data
# print(colors)
# print(evals)
##print("colors: ", len(colors))

# close driver
driver.close()
