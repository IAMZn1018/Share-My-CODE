import requests
import time

URL = 'https://movie.douban.com/top250?start={}&filter='

def main():
    for i in range(10):
        requests.get(URL.format(i))

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('耗时：' + str(end - start) + '秒')
    # 耗时：3.625061511993408秒
