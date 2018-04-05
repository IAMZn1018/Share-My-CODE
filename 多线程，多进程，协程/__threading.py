import requests
import time
import queue as Queue
import threading

URL = 'https://movie.douban.com/top250?start={}&filter='
URL_list = []

queue = Queue.Queue()
class ThreadUrl(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue=queue

    def run(self):
        while True:
            url = requests.get(URL)
            print(url.status_code)
            self.queue.task_done()

def main():
    for i in range(10):
        t = ThreadUrl(queue)
        t.setDaemon(True)           # 设置为守护线程
        t.start()

        URL_list.append(URL.format(i * 25))
    print(URL_list)

    for Url in URL_list:
        queue.put(Url)
    queue.join()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('耗时：' + str(end - start) + '秒')
    # 耗时：0.38639187812805176秒