#Author: Jerry Liu
#Today is February 23, 2018.
#This is the first test scraper for the Spongebob scripts. 
#What I have done: I have learned and accomplished how to get the script from 
#the 1st episode by following the plan I previously laid out in the test 
#folder. I have gotten all the lines with the tags into the variable called
#lines. We can take the text out using .get_text(), but we want to retain
#all the css tags so that it is easier to put the data into a csv file!
#Working on how to put the lines into the csv file is the next step.


from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

#type(html_soup)
#bs4.BeautifulSoup

firstEpi = "http://spongebob.wikia.com/wiki/Help_Wanted_(transcript)"
firstHTML = urlopen(firstEpi).read()

html_soup = BeautifulSoup(firstHTML,'html.parser')

#find the <ul> content, aka the actual script
content = html_soup.find('ul', attrs={'class': None})

#find each bullet
lines = content.findAll('li')

#for x in lines:
	#print(x.getText())

#print(lines)




#print(html_soup.prettify())