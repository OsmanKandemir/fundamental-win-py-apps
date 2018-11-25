#! // WINDOWS //
#! -*- coding = utf-8 -*-


import win32api
import ctypes
import datetime
from bs4 import BeautifulSoup
import urllib
import time


def main():
	
	ClockList = Request()

	print ClockList

	SetClockWin32Api(year = 18,
					month = 11,
					day = 22,
					hour = ClockList[0],
					minute = ClockList[1])


def Request():
	liste = []
	try:
		try:
			urlgir = "https://www.timeanddate.com/worldclock/turkey"
			data = urllib.urlopen(urlgir).read()
			parse = BeautifulSoup(data)
			den = parse.find('span', attrs={'id':"ct"})
			hour = int(den.text.split(":")[0])
			minute = int(den.text.split(":")[1])
			den2 = parse.find('span', attrs={'id':"ctdat"})
			#second = int(den.text.split(":")[2])
			print den2
			liste.append(hour)
			liste.append(minute)
			#liste.append(second)
			return liste
		except:
			Request()
	except RuntimeError,IOError:
			print "Internet Connection Failed"
			time.sleep(5)
			Request()
	
	


def SetClockWin32Api(**kwargs):
	liste2 = [kwargs.values()[0],kwargs.values()[1],kwargs.values()[2],kwargs.values()[3],kwargs.values()[4]]
	print liste2

	date_time = datetime.datetime(liste2[4],liste2[0],liste2[2],liste2[3],liste2[1])
	win32api.SetLocalTime(date_time)
	ctypes.windll.user32.MessageBoxA(0,"Change is succesfully complete","",5)




if __name__ == '__main__':
	main()
