import sys
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_currency(date, currency_code):  # 获得现汇卖出价
    driver = webdriver.Chrome()
    driver.get("https://www.boc.cn/sourcedb/whpj")
    time.sleep(2)
    # 控制Google Chrome打开网页

    start_time = driver.find_element(By.NAME, "erectDate")
    start_time.clear()
    start_time.send_keys(date)

    end_time = driver.find_element(By.NAME, "nothing")
    end_time.clear()
    end_time.send_keys(date)
    # 输入查询时间 查找某一天的价格

    currency = driver.find_element(By.NAME, "pjname")
    currency.click()
    currency.send_keys(currency_code)
    currency.click()
    # 输入查询货币代码

    query = driver.find_element(By.XPATH,
                                '//input[@type="button" and @class="search_btn" and ''@onclick''="executeSearch()"]')

    query.click()
    # 点击查询

    time.sleep(2)
    rate_output = driver.find_element(By.XPATH, '/html/body/div/div[4]/table/tbody/tr[2]/td[4]').text
    return rate_output
    # 获取结果并输出


def get_date(date_str):  # 获取查询日期 转换为年月日格式
    year = int(date_str[:4])
    month = int(date_str[5:6])
    day = int(date_str[7:8])
    formatted_date = datetime(year, month, day).strftime("%Y-%m-%d")
    return formatted_date


def get_currency_code(currency_str):  # 获取查询货币 转换为中文格式
    currency_dict = {
        'GBP': '英镑',
        'HKD': '港币',
        'USD': '美元',
        'CHF': '瑞士法郎',
        'DEM': '德国马克',
        'FRF': '法国法郎',
        'SGD': '新加坡元',
        'SEK': '瑞典克朗',
        'DKK': '丹麦克朗',
        'NOK': '挪威克朗',
        'JPY': '日元',
        'CAD': '加拿大元',
        'AUD': '澳大利亚元',
        'EUR': '欧元',
        'MOP': '澳门元',
        'PHP': '菲律宾比索',
        'THB': '泰国铢',
        'NZD': '新西兰元',
        'KRW': '韩国元',
        'RUB': '卢布',
        'MYR': '林吉特',
        'TWD': '新台币',
        'ESP': '西班牙比塞塔',
        'ITL': '意大利里拉',
        'NLG': '荷兰盾',
        'BEF': '比利时法郎',
        'FIM': '芬兰马克',
        'INR': '印度卢比',
        'IDR': '印尼卢比',
        'BRL': '巴西里亚尔',
        'AED': '阿联酋迪拉姆',
        'ZAR': '南非兰特',
        'SAR': '沙特里亚尔',
        'TRY': '土耳其里拉'
    }
    formatted_currency = currency_dict[currency_str]
    return formatted_currency


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("输入命令有误，请重新输入！")
    else:
        date_input = sys.argv[1]
        # date_input = '20211231'
        try:
            currency_input = sys.argv[2]
            # currency_input = 'USD'
        except KeyError:
            print("输入的货币符号有误")
    # 获取命令行参数

    rate = get_currency(get_date(date_input), get_currency_code(currency_input))
    print(rate)
    # 查询并打印现汇卖出价
    with open('result.txt', 'w') as f:
        f.write(rate)
        f.close()
    # 将结果保存到result.txt文件
