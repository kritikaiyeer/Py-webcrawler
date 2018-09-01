import  threading
from queue import  Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME='sitpune.edu'
HOMEPAGE = 'https://www.sitpune.edu.in/'
DOMAIN_NAME= get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREAD = 7

#create worker threads(will die when main exists) ,use _ because only want to loop 7 times
def create_workers():
    for _ in range(NUMBER_OF_THREAD):
        t=threading.Thread(target =work)
        t.daemon = True
        t.start()
# do job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()

#thread queue
queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

# each queued link is new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#check if items in queue,if so crawl them
def crawl():
    queued_links=file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + 'links in queue')
        create_jobs()

create_workers()
crawl()

