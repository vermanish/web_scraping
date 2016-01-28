
import urllib
import re
symbolslist=["aapl","spy","goog","nflx"]
i=0
file_object=open("symbol.txt","r")
mylist=[]
newfile=open("new_file.txt","w")
newfile.write("{}\t{}".format("Symbol","Current Price")+'\n')
for line in file_object:
	#newsym1=file_object.readline()
	#newsym=newsym1.replace("\n","")
	newsym=line.replace("\n","")
	print newsym
	url = "http://finance.yahoo.com/q?s="+newsym+"&ql=1"
	print url
	htmlfile=urllib.urlopen(url)
	#print file_object.readline()
	
	htmltext=htmlfile.read()
	regex = '<span id="yfs_l84_'+newsym+'">(.+?)</span>'
	pattern=re.compile(regex)
	price=re.findall(pattern,htmltext)
	print 'price:'
	print price
	zip(newsym,price[0])

	newfile.write("{}\t{}".format(newsym,price[0])+'\n')
	
	i+=1
file_object.close()
newfile.close()
