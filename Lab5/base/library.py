# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 10:02:24 2014

@author: jnos
"""
import book
import pickle


class library:
	def __init__(self, name):
		self.name = name
		try:
			f = open('bd_dump'+name, 'rb')
			self.bib = pickle.load(f)
			f.close()
		except IOError:
			self.bib = {}
	def addBook(self, author, title, year):
		b_id = len(self.bib)
		self.bib[b_id] = book.book(author, title, year, b_id)
		f = open('bd_dump'+self.name, 'wb')
		pickle.dump(self.bib, f)
		f.close()

	def listBooks(self, name):
		ret_value = []
		for b in self.bib.values():
			if b.author == name:
				ret_value.append( (b.id, b.title))
		return ret_value
	def searchBook(self, b_id):
		return self.bib[b_id]
