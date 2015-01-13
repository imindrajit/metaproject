from bs4 import BeautifulSoup
from time import time
import sqlite3
import urllib2
import json

conn = sqlite3.connect('summary4.db')
c = conn.cursor()
c.execute('''CREATE TABLE pages
	     (ID INTEGER PRIMARY KEY AUTOINCREMENT, link STRING UNIQUE, title STRING, timestamp STRING, meta text)''')

lines_seen = set()

if __name__ == "__main__":
	f = open("list.txt","r")
	for line in f:
		if line not in lines_seen:
			print line
		
			response = urllib2.urlopen(line).read()
			soup = BeautifulSoup(response)
			title = soup.title.string
		
			meta = soup.findAll("meta")
		
			data = {}		
		
			for tag in meta:
				if tag.has_attr("property"):
				#data = {};
					data[tag['content']]=tag['property']
			
			json_meta = json.dumps(data)
			print json_meta
			str_json = str(json_meta)

			tm = str(time())
			print time

			#sqlString = title + "," + line + "," + str(time()) + "," + json_meta

			c.execute("INSERT or IGNORE INTO pages(link, title, timestamp, meta) VALUES (?,?,?,?);", (line, title, tm, str_json ))
			conn.commit()
			
			lines_seen.add(line)
	
	if conn:
		conn.close()
		

	f.close()	
