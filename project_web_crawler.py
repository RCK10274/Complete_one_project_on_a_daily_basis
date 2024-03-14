from bs4 import BeautifulSoup as bs
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import time
from tqdm import tqdm
import os

def get_resp(url):
    try:
        resp = requests.get(url)
        resp.status_code == 200

    except requests.exceptions.RequestException as e:
        return f"發生{e}錯誤"
    return resp

def re_row(row):#正則排除\s對象
    res =re.sub(r'\s+', ' ', row).strip()
    return res

def filter_func(tag):#塞選<span>的函數
    # 返回True表示包含，返回False表示排除
    return tag.name == 'a' and 'span' not in tag  and 'pull-left"' not in tag.get('class', []) and "上一頁" not in tag.text and "下一頁" not in tag.text

def get_csv_from_web(file_name, file_type):
    #主要tag:
    #<div class="panel-heading">關鍵字</div>
    #<ul class="list-group">
    #   <span class="badge">
    #   <a>

    Keywords = pd.DataFrame({"keywords":[0], "counts":[0], "years":[0]})

    for year in range(1964, 2025):
        print(f"下載年分:{year}")
        for page in tqdm(range(0,3)):
            time.sleep(0.1)
            soup = bs(get_resp(f"https://tdr.lib.ntu.edu.tw/simple-search?query=&sort_by=score&order=desc&rpp=10&filter_field_1=degree&filter_type_1=equals&filter_value_1=%E7%A2%A9%E5%A3%AB&filter_field_2=dateIssued&filter_type_2=contains&filter_value_2={year}&etal=0&subject_page={page}").text, 'lxml')
            panel_heading = soup.find('div', class_='panel-heading', string='關鍵字')
            if panel_heading:
                page_find=True
            else:
                print(f"Can not find the page in {page}, stopping loop")
                break
            if not page_find:
                continue
            
            if panel_heading:
                ul = panel_heading.find_next_sibling('ul', class_='list-group')
                if ul:
                    tag_a = ul.find_all(filter_func)
                    tag_span = ul.find_all("span", class_="badge")

            for i in range(len(tag_a)):
                if tag_a[i].has_attr('title'):
                    if tag_a[i].text in Keywords["keywords"]:
                        break
                    else:
                        Keywords = Keywords._append({"keywords":tag_a[i].text, "counts":tag_span[i].text, "years":year}, ignore_index=True)

    Keywords=Keywords.drop(0)
    Keywords["keywords"] = Keywords["keywords"].map(re_row)#爬蟲下來的文字檔會有許多空白與換行號, 用re刪除每個字串的空白與\n:r'\s+'
    file_name = 'Keywords'
    file_type = '.csv'
    #將DataFrame儲存成csv檔案
    Keywords.to_csv(file_name+file_type, index=False)
    print("Rlready saved")
    
def close_message():#假如有警告訊息忽略它
    requests.packages.urllib3.disable_warnings()

def process_data(csv_name):
    df =pd.read_csv(csv_name)
    print(df)

#-------
ntu_url="https://tdr.lib.ntu.edu.tw/simple-search?query=&sort_by=score&order=desc&rpp=10&filter_field_1=degree&filter_type_1=equals&filter_value_1=%E7%A2%A9%E5%A3%AB&filter_field_2=dateIssued&filter_type_2=contains&filter_value_2={year}&etal=0&subject_page={page}"
page=55775#1~55776
file_name = 'Keywords'
file_type = '.csv'
get_csv_from_web(file_name,file_type)
#process_data(file_name+file_type)