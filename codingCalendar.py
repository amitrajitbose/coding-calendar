import urllib.request
from bs4 import BeautifulSoup
import sys
class Events(object):
    """Shows all the upcoming events that should be present on programmers calendar"""
    def __init__(self):
        page = urllib.request.urlopen('https://clist.by/')
        self.soup = BeautifulSoup(page, features="html.parser")
        self.data = {
                    'name' : [],
                    'link' : [],
                    'host' : [],
                    'start-time' : [],
                    'duration' : [],
                    'end-time': []
                }
        self.data = self._fetch_data()


    def _fetch_data(self):
        error_event_index = []
        cursor = 0
        for i in self.soup.findAll('div', class_="title"):
            temp = str(list(i.children)[1])
            temp = temp.lstrip('<a> ')
            temp = temp.rstrip('</a>')
            temp = temp.split("\"")
            try:
                #print((temp[1].split('//')[1]).split('/')[0])
                self.data['host'].append((temp[1].split('//')[1]).split('/')[0])
                self.data['link'].append(temp[1])
                self.data['name'].append(temp[3])
            except:
                error_event_index.append(cursor)
            cursor += 1

        cursor = 0
        for i in self.soup.find_all('div', class_ = 'col-md-5 col-sm-12 start-time'):
            if(cursor not in error_event_index):
                self.data['start-time'].append(i.text.strip())
            cursor += 1

        cursor = 0
        for i in self.soup.find_all('div', class_ = 'col-md-3 col-sm-6 duration'):
            if(cursor not in error_event_index):
                self.data['duration'].append(i.text.strip())
            cursor += 1

        cursor = 0
        for i in self.soup.find_all('div', class_ = 'col-md-4 col-sm-6 timeleft'):
            if(cursor not in error_event_index):
                self.data['end-time'].append(i.text.strip())
            cursor += 1

        cursor = 0
        for i in self.soup.find_all('div', class_ = 'col-md-4 col-sm-6 timeleft countdown'):
            if(cursor not in error_event_index):
                self.data['end-time'].append(i.text.strip())
        cursor += 1
        return self.data

    def top(self, limit):
        """returns <limit> number of latest upcoming events"""
        print("\n\n")
        for i in range(limit):
            print("EVENT NAME : ",self.data['name'][i])
            print("EVENT HOST : ",self.data['host'][i])
            print("EVENT LINK : ",self.data['link'][i])
            print("EVENT START TIME : ",self.data['start-time'][i])
            print("EVENT DURATION : ",self.data['duration'][i])
            print("EVENT END TIME : ",self.data['end-time'][i])
            print("_______________________________________________________\n\n")

def main():
    limit = int(sys.argv[1])
    obj = Events()
    obj.top(limit)

main()
print("-------------------------------------------\nThanks for using, written by Amitrajit Bose\n-------------------------------------------")