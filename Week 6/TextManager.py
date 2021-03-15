from concurrent.futures import ThreadPoolExecutor  #module for async tasks
import threading
import requests
import codecs #for encoding/decoding of text 

class NotFoundException(Exception):  # kommer ikke til at bruge den her, da URL altid vil være der? 
    def __init__(self, message="404 - Findes ikke"):
        print(message)
 
    
class TextManager ():
    def __init__(self, url_list):
        self.url_list = url_list
        self.currentIndex = 0
        
        
    def download(self, url, filename):
        try:
            response = requests.get(url) #  returværdien af get, som er en instans af response, ligges i en variabel(response)
            with codecs.open(filename, "w", "utf-8") as file_object:
                for line in response.text:
                    file_object.write(line)
        except ConnectionError:
            raise NotFoundException
            
            
    def multi_download(self):
         #concurrent call to the download function with url_list as *iterables
             #return value: filenames as it is the return value from download func 
        with ThreadPoolExecutor(max_workers=6) as executor:
            for key in self.url_list:
                executor.submit(self.download,key,self.url_list[key])
            
      
        
    def iter(self):
        return iter(self.url_list)

    def next(self):
        if self.currentIndex >= len(self.url_list.values()):
            raise StopIteration
        else:
            val = list(self.url_list.values())[self.currentIndex]
            self.currentIndex+= 1
            return val

    def url_list_generator(self):
        for k in self.url_list:
            yield k

    def avg_vowels(self,text):
        vowel_count = 0
        word_count = 0
        vowels = "aeiuoAEIOU"
        with codecs.open(text, "r", "utf-8") as file:
            for line in file:
                for word in line.split(" "):
                    if word is not ""  or word is not " ":
                        word_count += 1
                        for character in word:
                            if character in vowels:
                                vowel_count += 1
        return vowel_count / word_count

    def hardest_read(self):
        tasks = dict()
        res = dict()
        with ThreadPoolExecutor(max_workers=6) as executor:
            for url in self.url_list_generator():
                filename = self.url_list[url]
                tasks[filename] = executor.submit(self.avg_vowels,filename)
        executor.shutdown(wait="true")
        for t in tasks:
            res[t] = tasks[t].result()
        return max(res, key=res.get)


