from bs4 import BeautifulSoup as bs
import requests
import time
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.patches import Ellipse

def real_url(L,M,R):
    number = input('系/院 編號 :')
    try:
        resp = requests.get(f'https://tdr.lib.ntu.edu.tw/handle/123456789/{number}/browse?type=subject&submit_browse=%E9%97%9C%E9%8D%B5%E5%AD%97')
        resp.status_code == 200
    except requests.exceptions.RequestException as e:
        return f"發生{e}錯誤"
    soup = bs(resp.text, 'lxml')
    tag_count = soup.find('div', class_="panel-heading text-center").text
    tag_count = tag_count[20:24]
    url = L + number + M + tag_count + R
    print(url)
    return url

def req_getdata(url):#抓取HTML並輸出兩個list分別為lib_item與lib_num,項目與個數
    try:
        resp = requests.get(url)
        resp.status_code == 200
    except requests.exceptions.RequestException as e:
        return f"發生{e}錯誤"

    lib_item = []#科目
    lib_num = []#數量

    soup = bs(resp.text, 'lxml')
    tag_ul = soup.find('ul', class_='list-group')
    tag_li = tag_ul.find('li', class_="list-group-item")
    f_list_str = list(tag_li.find('a').text.rstrip(',').split(','))
    for item in (f_list_str):
        if item not in lib_item:
            lib_item.append(item)
            lib_num += [1]
        else:
            item_index = lib_item.index(item)
            lib_num[item_index] = lib_num[item_index] + 1

    tag_count = soup.find('div', class_="panel-heading text-center").text
    #tag_count = int(tag_count[10:15])

    while True:
        tag_li = tag_li.find_next_sibling('li', class_="list-group-item")
        tag_str = tag_li.find('a').text
        list_str = tag_str.rstrip(',').split(',')
    
        for item in (list_str):
            if item not in lib_item:
                lib_item.append(item)
                lib_num += [1]
            else:
                item_index = lib_item.index(item)
                lib_num[item_index] = lib_num[item_index] + 1
        #time.sleep(0.1)
    return lib_item,lib_num

def close_message():#假如有警告訊息忽略它
    requests.packages.urllib3.disable_warnings()

def hover(event):#看不懂
    if event.inaxes == ax:
        for label, point, item in zip(label_objects, scatter.get_offsets(), lib_item):
            contains, _ = label.contains(event)
            if contains:
                label.set_visible(True)
                label.set_text(item)
            else:
                label.set_visible(False)
        fig.canvas.draw_idle()

def plt_bar(x, y):
    plt.rcParams["font.sans-serif"] = "mingliu"
    
    global fig, ax, scatter, label_objects

    fig, ax = plt.subplots()
    scatter = ax.bar(x, y)

    label_objects = []
    for i, item in enumerate(x):
        point = i, 0
        label_text = ax.text(point[0], point[1], '', visible=False, ha='center', va='bottom')
        label_objects.append(label_text)

    fig.canvas.mpl_connect('motion_notify_event', hover)

    plt.title('Research Trends in 2006-2023')
    plt.xlabel('Subject')
    plt.ylabel('Count')
    plt.xticks([])
    plt.show()

if __name__=="__main__":

    #資訊網路與多媒體研究所 論文搜尋關鍵字
    o_url = 'https://tdr.lib.ntu.edu.tw/handle/123456789/160/browse?type=subject&order=DESC&rpp=1369&submit_browse=%E6%9B%B4%E6%96%B0'
                                                    #學院/學系編號(1~205)                   #關鍵字搜尋數量
    L_url = 'https://tdr.lib.ntu.edu.tw/handle/123456789/'
    M_url = '/browse?type=subject&order=DESC&rpp='
    R_url = '&submit_browse=%E6%9B%B4%E6%96%B0'
    
    url = real_url(L_url,M_url,R_url)
    lib_item,lib_num = req_getdata(url)
    close_message()
    


    
    with open('data.txt', 'w', encoding='utf-8-sig') as fp:
        fp.write(str(dict(zip(lib_item,lib_num))))