import requests
import time
from multiprocessing import Pool

URL = 'https://movie.douban.com/top250?start={}&filter='
URL_list = []

def get_one_page(url):
    r = requests.get(url)
    print(r.status_code)

def main(url):
    get_one_page(url)

if __name__ == '__main__':
    start = time.time()
    for i in range(10):
        URL_list.append(URL.format(i * 25))
    print(URL_list)
    pool = Pool(4)
    res = pool.map(main, URL_list)
    pool.close()
    pool.join()
    end = time.time()
    print('耗时：' + str(end - start) + '秒')
    # 耗时：1.7563891410827637秒