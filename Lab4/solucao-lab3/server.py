#!/usr/bin/env python

import library
import Pyro4


def main():
	remoteLibrary = Pyro4.expose(library.library)

	bd = remoteLibrary("mylib")

	daemon = Pyro4.Daemon(host='194.210.229.140')

	ns = Pyro4.locateNS(host='193.136.128.104')
	print (ns)

	try:
		ns.createGroup(':libraries')
	except:
		pass

	uri = daemon.register(bd, "BookDB_Xavi")
	ns.register("BookDB_Xavi", uri)

	try:
		daemon.requestLoop()
	finally:
		daemon.shutdown(True)

if __name__=="__main__":
	main()
