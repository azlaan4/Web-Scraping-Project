import numpy as np  # linear algebra
import pandas as pd     # data processing, CSV file I/O (e.g. pd.read_csv)
import requests     # Getting Web page content
from bs4 import BeautifulSoup as bs     # Scraping web pages
import matplotlib.pyplot as plt     # Visualization
import matplotlib.style as style    # For styling plots
from matplotlib import pyplot as mp     # For Saving plots as images

# For displaying plots in jupyter notebook
# %matplotlib inline

style.use('fivethirtyeight')  # matplotlib Style

# Using requests module for downloading webpage content
response = requests.get('https://stackoverflow.com/tags')

# Getting status of the request
# 200 status code means our request was successful
# 404 status code means that the resource you were looking for was not found
response.status_code

# Parsing html data using BeautifulSoup
soup = bs(response.content, 'html.parser')

# body
body = soup.find('body')

# printing the object type of body
type(body)

# getting tags
# Using this class along with a tag, we can extract all the language links in a list
lang_tags = body.find_all('a', class_='post-tag')
lang_tags[:2]

# extracting language from tags
# we will extract all the language names
languages = [i.text for i in lang_tags]
languages[:5]

# counting tags
# we will extract all the tag count spans in a list
tag_counts = body.find_all('span', class_='item-multiplier-count')
tag_counts[:2]

# we will extract all the Tag Counts
no_of_tags = [int(i.text) for i in tag_counts]
no_of_tags[:5]

# =================================================================================================
# ======== Goal One is to plot the graph on top trending languages
# =================================================================================================
# Put all code together and join the two lists We will use Pandas.DataFrame to put the two
# lists together. In order to make a DataFrame, we need to pass both the lists (in dictionary form)
# as argument to our function. Function to check, if there is any error in length of the extracted
# bs4 object

def error_checking(list_name, length):
    if (len(list_name) != length):
        print("Error in {} parsing, length not equal to {}!!!".format(list_name, length))
        return -1
    else:
        pass


def get_top_languages(url):
    # Using requests module for downloading webpage content
    response = requests.get(url)

    # Parsing html data using BeautifulSoup
    soup = bs(response.content, 'html.parser')
    body = soup.find('body')

    # Extracting Top Langauges
    lang_tags = body.find_all('a', class_='post-tag')
    error_checking(lang_tags, 36)  # Error Checking
    languages = [i.text for i in lang_tags]  # Languages List

    # Extracting Tag Counts
    tag_counts = body.find_all('span', class_='item-multiplier-count')
    error_checking(tag_counts, 36)  # Error Checking
    no_of_tags = [int(i.text) for i in tag_counts]  # Tag Counts List

    # Putting the two lists together
    df = pd.DataFrame({'Languages': languages,
                       'Tag Count': no_of_tags})

    return df

# Plot Data
URL1 = 'https://stackoverflow.com/tags'
df = get_top_languages(URL1)
df.head()

# Now, we will plot the Top Languages along with their Tag Counts
plt.figure(figsize=(8, 3))
plt.bar(height=df['Tag Count'][:10], x=df['Languages'][:10])
plt.xticks(rotation=90)
plt.xlabel('Languages')
plt.ylabel('Tag Counts')
plt.savefig('lang_vs_tag_counts.png', bbox_inches='tight')
plt.show()


# =================================================================================================
# ======== Goal Two is to list most voted questions
# =================================================================================================
# Now that we have collected data using web scraping one time, it won’t be difficult the next time.
# For Goal 2, we have to list questions with most votes along with their attributes like; Tags,
# Number of Votes, Number of Answers, Number of Views

# Using requests module for downloading web-page content
response1 = requests.get('https://stackoverflow.com/questions?sort=votes&pagesize=50')

# Getting status of the request
# 200 status code means our request was successful
# 404 status code means that the resource you were looking for was not found
response1.status_code

# Parsing the document into Beautiful Soup
# Parsing html data using BeautifulSoup
soup1 = bs(response1.content, 'html.parser')

# body
body1 = soup1.select_one('body')

# printing the object type of body
type(body1)

# This will give us exactly 50 Tags
question_links = body1.select("h3 a.question-hyperlink")
question_links[:2]

# List comprehension, to extract all the questions
questions = [i.text for i in question_links]
questions[:2]

# Extract Summary
# we can extract all the question links in a list
summary_divs = body1.select("div.excerpt")
print(summary_divs[0])

# List comprehension, to extract all the questions
# This is to remove both leading and trailing unwanted characters from a string
summaries = [i.text.strip() for i in summary_divs]
summaries[0]

# Extract Tags
tags_divs = body1.select("div.summary > div:nth-of-type(2)")
tags_divs[0]

# we can use list comprehension to extract a tags in a list, grouped per question
a_tags_list = [i.select('a') for i in tags_divs]

# Printing first question's a tags
a_tags_list[0]

# run a for loop for going through each question and use list comprehension inside it,
# to extract the tags names
tags = []

for a_group in a_tags_list:
    tags.append([a.text for a in a_group])

tags[0]

# Extract Number of votes, answers and views
# No. of Votes
vote_spans = body1.select("span.vote-count-post strong")
print(vote_spans[:2])

# extract vote counts.
no_of_votes = [int(i.text) for i in vote_spans]
no_of_votes[:5]

# No. of Answers
answer_divs = body1.select("div.status strong")
answer_divs[:2]

# extract answer counts.
no_of_answers = [int(i.text) for i in answer_divs]
no_of_answers[:5]

# No. of Views
div_views = body1.select("div.supernova")
div_views[0]

# extract vote counts
no_of_views = [i['title'] for i in div_views]
no_of_views = [i[:-6].replace(',', '') for i in no_of_views]
no_of_views = [int(i) for i in no_of_views]
no_of_views[:5]

# =================================================================================================
# =================================================================================================
# Putting all of them together in a data-frame
def get_top_questions(url, question_count):
    # WARNING: Only enter one of these 3 values [15, 30, 50].
    # Since, stackoverflow, doesn't display any other size questions list
    url = url + "?sort=votes&pagesize={}".format(question_count)

    # Using requests module for downloading webpage content
    response = requests.get(url)

    # Parsing html data using BeautifulSoup
    soup = bs(response.content, 'html.parser')
    body = soup.find('body')

    # Extracting Top Questions
    question_links = body1.select("h3 a.question-hyperlink")
    error_checking(question_links, question_count)  # Error Checking
    questions = [i.text for i in question_links]  # questions list

    # Extracting Summary
    summary_divs = body1.select("div.excerpt")
    error_checking(summary_divs, question_count)  # Error Checking
    summaries = [i.text.strip() for i in summary_divs]  # summaries list

    # Extracting Tags
    tags_divs = body1.select("div.summary > div:nth-of-type(2)")

    error_checking(tags_divs, question_count)  # Error Checking
    a_tags_list = [i.select('a') for i in tags_divs]  # tag links

    tags = []

    for a_group in a_tags_list:
        tags.append([a.text for a in a_group])  # tags list

    # Extracting Number of votes
    vote_spans = body1.select("span.vote-count-post strong")
    error_checking(vote_spans, question_count)  # Error Checking
    no_of_votes = [int(i.text) for i in vote_spans]  # votes list

    # Extracting Number of answers
    answer_divs = body1.select("div.status strong")
    error_checking(answer_divs, question_count)  # Error Checking
    no_of_answers = [int(i.text) for i in answer_divs]  # answers list

    # Extracting Number of views
    div_views = body1.select("div.supernova")

    error_checking(div_views, question_count)  # Error Checking
    no_of_views = [i['title'] for i in div_views]
    no_of_views = [i[:-6].replace(',', '') for i in no_of_views]
    no_of_views = [int(i) for i in no_of_views]  # views list

    # Putting all of them together
    df = pd.DataFrame({'question': questions,
                       'summary': summaries,
                       'tags': tags,
                       'no_of_votes': no_of_votes,
                       'no_of_answers': no_of_answers,
                       'no_of_views': no_of_views})

    return df


# Plotting Votes v/s Views v/s Answers
URL2 = 'https://stackoverflow.com/questions'

df1 = get_top_questions(URL2, 50)
df1.head()

# =================================================================================================
# =================================================================================================
f, ax = plt.subplots(3, 1, figsize=(12, 8))

ax[0].bar(df1.index, df1.no_of_votes)
ax[0].set_ylabel('No of Votes')

ax[1].bar(df1.index, df1.no_of_views)
ax[1].set_ylabel('No of Views')

ax[2].bar(df1.index, df1.no_of_answers)
ax[2].set_ylabel('No of Answers')

plt.savefig('votes_vs_views_vs_answers.png', bbox_inches='tight')

plt.show()

# =================================================================================================
# =================================================================================================
# =================================================================================================
# observe that there is no co-linearity between the votes, views and answers related to a question
# =================================================================================================
# =================================================================================================
# =================================================================================================



