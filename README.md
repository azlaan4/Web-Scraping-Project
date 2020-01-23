# Web Scraping Project  
  
It is a web-scraper built with Python and Beautiful Soup. It is built to scrap StackOverflow website.   
  
## What is Web Scraping?  
  
Web scraping, also called web data mining or web harvesting, is the process of constructing an agent which can extract, parse, download and organize useful information from the web automatically.  
  
Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol, or through a web browser.   
  
## What is Web Scraper?  
  
A Web Scraper is a program that quite literally scrapes or gathers data off of websites. Take the below hypothetical example, where we might build a web scraper that would go to twitter, and gather the content of tweets.  
  
# Scraping Stack Overflow  
  
This program is made to perform following tasks on [StackOverflow](https://stackoverflow.com/) website:  
  
 ## List Trending Languages 
 To achive it we have to list down most tagged Languages along with their Tags Count.  
  
 ### Steps: 
 1. Download Webpage from stackoverflow.  
 2. Parse the document content into BeautifulSoup  
 3. Extract Top Languages  
 4. Extract their respective Tag Counts  
 5. Put all code together and join the two lists  
 6. Plot Data  
	 
## List Trending Questions *(top 50 most voted)*  
To achive it we have to list down questions with most votes along with their attributes, like:  
Tags, Number of Votes, Number of Answers, & Number of Views.
  
### Steps:  

 1. Download Webpage from stackoverflow  
 2. Parse the document content into BeautifulSoup  
 3. Extract Top Questions  
 4. Extract their respective Summary  
 5. Extract their respective Tags  
 6. Extract their respective no. of votes, answers and views  
 7. Put all code togther and join the lists  
 8. Plot Data  
  
# Required Libraries and Packages  
  
These are some required packages and libraries that you need to run this program correctly without any error:  
- Numpy    *(to perform linear algebra tasks)*  
- Pandas *(for data framing i.e., data is aligned in a tabular fashion in rows and columns)*  
- Requests *(getting web page content)*  
- Beautiful Soup 4 *(scraping web pages)*  
- Matplotlib *(graphical visualization and styling of data)*