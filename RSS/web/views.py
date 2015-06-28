# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from threading import Thread, Lock
from web.models import *

import queue, feedparser, threading,time,json
from random import randint

queue = queue.Queue()
myLock = Lock ()
max_feed = 5
buffer_size = 10

def save_url_rss(url):
	response = requests.get(url)
	d = feedparser.parse(response)
	for post in d.entries:
	    #print post.title + "\n"  + post.description+  "\n" + post.link+ "\n"+ post.published + "\n\n"
	     c = canales(nombre = post.title,
                    pub_fecha = post.published,
                    descripcion = post.summary_detail.value,
                    url = post.link)
	c.save()
	print (response.text)

def queuer_feed_from_rss(url):
	fp = feedparser.parse(url)
	for post in fp.entries:
		if queue.qsize() < buffer_size:
			myLock.acquire()
			time.sleep(randint(0,3))
			queue.put(Feed(post.title, post.published, post.summary_detail.value, post.link, url))
			myLock.release()
			print ('-> Produced: ', url.split("rss/")[1], '--', str(post.title), ' -- size = ' ,queue.qsize())

class Producer (Thread):
	def run (self):
		channels = canales.objects.all()
		for channel in channels:
			t = threading.Thread(target=queuer_feed_from_rss, args=(channel.url,))
			t.start()

class Consumer (Thread):
	def run (self):
		consumed = 0
		while consumed < buffer_size:
			myLock.acquire ()
			if not queue.empty():
				try:
					e = queue.get()
					print ('<- Consumed', ' -- ', e.title, ' -- size = ', consumed + 1)
				except:
					print ('no feed yet')
			myLock.release ()
			consumed =+ 1

class Feed(object):
  title = ""
  pub_date = ""
  image = ""
  link = ""
  content = ""
  def __init__(self, title, pub_date, content, link, source):
    self.title = title
    self.pub_date = pub_date
    self.content = content
    self.link = link
    self.source = source

def three_more_feeds(request):
	# Sending 3 more feeds
	data = []
	while len(data) < 3:
		try:
			data.append(queue.get())
		except:
			print ("there aren't 3 elements yet")
	return HttpResponse(data)

def home(request):
	data = []
	p1 = Producer ()
	#c1 = Consumer ()

	p1.start ()
	#c1.start ()

	# waiting for the first three products
	p1.join ()
	while len(data) < 3:
		try:
			data.append(queue.get())
		except:
			print ("there aren't 3 elements yet")
	return render_to_response('home.html',{'data':data}, RequestContext(request))