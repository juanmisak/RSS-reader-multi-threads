# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from threading import Thread, Lock
import Queue
#libreria para obtener y parsear xml
import urllib2
import feedparser


queue = Queue.Queue()
myLock = Lock ()
max_feed = 5

def save_url_rss(url):
	response = requests.get(url)

	d = feedparser.parse(response)
	
	for post in d.entries:
	    #print post.title + "\n"  + post.description+  "\n" + post.link+ "\n"+ post.published + "\n\n"
	     c = canales(nombre = post.title,
                    pub_fecha = post.published,
                    descripcion = post.description,
                    url = post.link)
        c.save()

	print response.text


def get_feed_from_rss(url):
	response = requests.get(url)

	d = feedparser.parse(response)
	

	#obteniendo datos del feed 
	for post in d.entries:
	     feed = Feed(title = post.title,
                    pub_date = post.published,
                    image = post.image,
                    content = post.description,
                    link = post.link)

	print response.text

class Feed(object):
	tittle = ""
	pub_date = ""
	image = ""
	link = ""
	content = ""

	def __init__(self, tittle, pub_date, image, content, link):
		self.tittle
		self.pub_date
		self.image
		self.content
		self.link

class Producer (Thread):
	def run (self):
		for i in range (max_feed):
			#time.sleep(1)
			myLock.acquire ()
			queue.put(i)
			myLock.release ()
			print '-> Produced %d' % i

class Consumer (Thread):
	def run (self):
		consumed = 0
		while consumed < max_feed:
			#time.sleep(2)
			myLock.acquire ()
			if not queue.empty():
				e = queue.get()
			myLock.release ()
			print '<- Consumed %d' % e
			consumed += 1

def home(request):
	data = []
	p1 = Producer ()
	c1 = Consumer ()

	p1.start ()
	c1.start ()

	p1.join ()
	c1.join ()

	return render_to_response('home.html',{'data':data}, RequestContext(request))