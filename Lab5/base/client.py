#!/usr/bin/env python

import Pyro4

def main():
 

	ns = Pyro4.locateNS()


	uri = ns.lookup('BookDB')


	bd = Pyro4.Proxy(uri)

	
	exit = False
	while not exit:
		l = input("add? search? list? quit?")
		l = l.split()
		
		if len(l)==1:
			command = l[0].upper()
			if command=='QUIT':
				exit = True
			elif command == 'ADD':
				l = input('Insert author title and date separated by # :\n')
				processed_line = l.split('#')
				if len(processed_line) ==3:
					print ('%s %s %s'% (processed_line[0], processed_line[1], processed_line[2]))
					bd.addBook(processed_line[0], processed_line[1], processed_line[2])
			elif command == 'SEARCH':
				l = input('Insert id :\n')
				processed_line = l.split()
				print (processed_line[0])
				if len(processed_line) ==1:
					b = bd.searchBook(int(processed_line[0]))
					print (b)
			elif command == 'LIST':
				l = input('Insert name :\n')
				processed_line = l.split()
				print (processed_line[0])
				if len(processed_line) ==1:
					b_list = bd.listBooks(processed_line[0])
					print (b_list)
				
			else:
				print (bd.bib)
			
		
		if len(l)==1 and l[0]=='quit':
			exit = True
    
    

if __name__=="__main__":
    main() 
