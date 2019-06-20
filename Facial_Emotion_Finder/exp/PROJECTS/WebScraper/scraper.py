import requests
from bs4 import BeautifulSoup
result=requests.get("https://timesofindia.indiatimes.com/")
if(result.status_code==200):
	src=result.content
	soup=BeautifulSoup(src,'lxml')
	ul_tags=soup.find_all('ul')
	li_tags=[]
	for ul_tag in ul_tags:
		if ul_tag.get("data-vr-zone")=="top_stories" :
			li_tags=ul_tag.find_all("li")
#	print(li_tags)
	a_tags=[]
	for li_tag in li_tags:
		a_tags.append(li_tag.find_all("a"))
	titles=[]
	for a_tag in a_tags:
		for j in a_tag:
			if j.get("title")!=None:
				print(j.get("title"))
