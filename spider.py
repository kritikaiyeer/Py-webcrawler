from urllib.request import urlopen
from link_finder import link_finder
from general  import *
from domain import *
# the above means import all from general

#this is to bring weblinks to the queued and then from queued to crawled list
class Spider:

    #creating class variables(these can be shared among all)
    project_name=''
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue=set()
    crawled=set()

    def __init__(self,project_name,base_url,domain_name):
        Spider.project_name=project_name
        Spider.base_url=base_url
        Spider.domain_name=domain_name
        Spider.queue_file= Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider',Spider.base_url)

    @staticmethod
    def boot():
         create_project_dir(Spider.project_name)
         create_data_files(Spider.project_name,Spider.base_url)
         Spider.queue= file_to_set(Spider.queue_file)
         Spider.crawled= file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name,page_url):
         if page_url not in Spider.crawled:
             print(thread_name +' now crawling '+page_url)
             print('Queue' + str(len(Spider.queue)) + ' | Crawled '+str(len(Spider.crawled)))
             Spider.add_links_to_queue(Spider.gather_links(page_url))
             Spider.queue.remove(page_url)       #removes from queued and transfers it to crawled
             Spider.crawled.add(page_url)
             Spider.update_files()
    @staticmethod
    def gather_links(page_url):
        html_string=''
        try :
            response = urlopen(page_url)
            if 'text/html'in response.getheader('Content-Type'):
                html_bytes= response.read()
                html_string = html_bytes.decode("utf-8")
                finder = link_finder(Spider.base_url,page_url)
                finder.feed(html_string)
        except:
            print("Error : the webpage cannot be crawled ")
            return set()
        return finder.page_link()

    @staticmethod
    def add_links_to_queue(links):
         for url in links:
             if url in Spider.queue:
                 continue
             if url in Spider.crawled:
                  continue
             if Spider.domain_name not in url :
                 continue
             Spider.queue.add(url)
    @staticmethod
    def update_files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)












