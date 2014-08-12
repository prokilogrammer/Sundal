# coding: utf-8
import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
http = httplib2.Http()
status, response = http.request("http://en.wikipedia.org/wiki/Precision_and_recall")
for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
    if link.has_attr('href'):
        print link['href']

soup = BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):

response
soup = BeautifulSoup(response, parseOnlyThese=SoupStrainer('a'))
soup
for link in soup:
    if link.has_key('href'):
        print link['href']

url = "http://en.wikipedia.org/wiki/Precision_and_recall"
import urllib
import urlparse
for link in soup:
    if link.has_key('href'):
        print urlparse.urljoin(url, link['href'])

urllist = list()
for link in soup:
    if link.has_key('href'):
        urllist.add(urlparse.urljoin(url, link['href']))

for link in soup:
    if link.has_key('href'):
        urllist.push(urlparse.urljoin(url, link['href']))

for link in soup:
    if link.has_key('href'):
        urllist.put(urlparse.urljoin(url, link['href']))

for link in soup:
    if link.has_key('href'):
        urllist.append(urlparse.urljoin(url, link['href']))

len(urllist)
urls = set()
for link in soup:
    if link.has_key('href'):
        urls.add(urlparse.urljoin(url, link['href']))

len(urls)
urls
crawldocs = {}
for link in urls:
    status, response = http.request(link)
    if status == 200:
        crawldocs[link] = response

for link in urls:
    print "Reading page: " + `link`
    status, response = http.request(link)
    if status == 200:
        crawldocs[link] = response

maincontent = {}
crawldocs[1]
response
maincontent = {}
g = Goose()
from goose import Goose
g = Goose()
for link, raw_html in crawldocs.iteritems():
    maincontent[link] = g.extract(raw_html = raw_html)

len(maincontent)
len(crawldocs)
crawldocs
for link in urls:
    print "Reading page: " + `link`
    status, response = http.request(link)
    crawldocs[link] = response

len(crawldocs)
for link, raw_html in crawldocs.iteritems():
    maincontent[link] = g.extract(raw_html = raw_html)

len(maincontent)
response
originaldoc_maincontent = g.extract(raw_html=response)
from simserver
from simserver import SessionServer
from simserver import SessionServer
server = SessionServer('/tmp/my_simserver')
import logging
corpus = [{'id
corpus = [{'id':link, 'tokens':content.cleaned_text} for link, content in maincontent.iteritems()]
len(corpus)
corpus[1]
from gensim import utils
service.train(corpus, method='lsi')
server.train(corpus, method='lsi')
corpus = [{'id':link, 'tokens':(content.cleaned_text,)} for link, content in maincontent.iteritems()]
corpus[1]
server.train(corpus, method='lsi')
server.index(corpus)
corpus = [{'id':link, 'tokens':utils.simple_preprocess(content.cleaned_text,)} for link, content in maincontent.iteritems()]
server.train(corpus, method='lsi')
server.index(corpus)
originaldoc = {'tokens': utils.simple_preprocess(originaldoc_maincontent.cleaned_text)}
result = server.find_similar(originaldoc, min_score=0.5)
len(result)
result
result = server.find_similar(originaldoc, min_score=0.9)
result
url
service.delete(corpus)
server.delete(corpus)
result = server.find_similar(originaldoc)
len(result)
result
result = server.find_similar(originaldoc, min_score=0.9)
result
server.delete([c.id for c in corpus])
corpus[1]
corpus[1].id
corpus[1]['id']
server.delete([c['id'] for c in corpus])
result = server.find_similar(originaldoc, min_score=0.9)
result
result = server.find_similar(originaldoc)
result
print url
maincontent.get(0)
maincontent.get(1)
url
test = url + "#hi"
test
test.startswith(url)
for link, content in maincontent.iteritems():
    if not link.startswith(url):
        corpus.append({'id':link, 'tokens':utils.simple_preprocess(content.cleaned_text)})

len(corpus)
len(maincontent)
corpus = list()
for link, content in maincontent.iteritems():
    if not link.startswith(url):
        corpus.append({'id':link, 'tokens':utils.simple_preprocess(content.cleaned_text)})

len(corpus)
server.train(corpus, method='lsi')
server.index(corpus)
server.find_similar(originaldoc)
result = server.find_similar(originaldoc)
result[1]
result[1][1]
sortedresult = list.sorted(result, key=lambda x : result[1])
sortedresult = list.sort(result, key=lambda x : result[1])
sortedresult = sorted(result, key=lambda x : result[1])
sortedresult
url
get_ipython().magic(u'save get_webpage_similarity_scores')
get_ipython().magic(u'save get_webpage_similarity_scores 1-')
get_ipython().magic(u'save get_webpage_similarity_scores 1-113')
