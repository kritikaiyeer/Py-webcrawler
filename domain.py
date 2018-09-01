from urllib.parse import urlparse

#get domain name(quora.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2]+'.'+results[-1]    #returns last two words
    except:
        return ''

# get sub domain name(www.quora.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc          #always use try except when connecting to networks
    except:
        return ''

