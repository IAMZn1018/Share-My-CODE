import requests
import gevent.monkey
import time
gevent.monkey.patch_all()
import gevent

URL = 'https://movie.douban.com/top250?start={}&filter='
URL_list = []

def get_one_page(pid):
    response = requests.get(URL)


def asynchronous():
    threads = []
    for i in range(10):
        threads.append(gevent.spawn(get_one_page, URL.format(i * 25)))
    gevent.joinall(threads)

if __name__ == '__main__':
    start = time.time()
    asynchronous()
    end = time.time()
    print('耗时：' + str(end - start) + '秒')
    # 耗时：0.49812793731689453秒

