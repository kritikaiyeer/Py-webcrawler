import os
#Each website you crawl is new project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project'+directory)
        os.makedirs(directory)

#Create queued and crawled files(if not present)

def create_data_files(project_names,base_url):
     queue= project_names + '/queue.txt'
     crawled= project_names +'/crawled.txt'
     if not os.path.isfile(queue):
         write_file(queue,base_url)
     if not os.path.isfile(crawled):
         write_file(crawled,'')

#create a new file
def write_file(path,data):
    f= open(path,'w')
    f.write(data)
    f.close()

#Add data to existing files
def append_file(path,data):
    with open(path,'a')as file:
        file.write(data+'\n')

#Delete data from contents file
def delete_file_contents(path,data):
     open(path,'w').close()

#Read a file and convert each file into set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# iterate each line of set to file
def set_to_file(links,file_name):
    with open(file_name,"w")as f:
     for link in sorted(links):
         append_file(file_name,link)

















