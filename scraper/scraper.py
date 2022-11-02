import requests
from bs4 import BeautifulSoup


URL = 'https://en.wikipedia.org/wiki/Cold_War'


def get_citations_needed_count(URL):
    '''A function to return the number of times citation needed tag was used in a wikipedia page'''
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    all = soup.find_all('a', title="Wikipedia:Citation needed")
    return (len(all))

print('Number of Citations Needed in this page is: ' , get_citations_needed_count(URL))
print('\n')

def get_citations_needed_report(URL):
    '''A function that returns a string containing all the sentences that have a citation needed tag in a wikipedia page'''
    report = ''
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    all = soup.find_all('a', title="Wikipedia:Citation needed")
    for i in all:
        report = report + i.parent.parent.parent.text + '\n'
    return report

print(get_citations_needed_report(URL))