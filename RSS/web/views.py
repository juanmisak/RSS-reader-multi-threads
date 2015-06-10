# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from threading import Thread, Lock
import Queue

queue = Queue.Queue()
myLock = Lock ()
max_feed = 5

def get_feed_from_rss(url):
	response = requests.get(url)
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