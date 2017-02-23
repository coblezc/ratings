from selenium import webdriver
import time
from flask import Flask, render_template, request
import collections

# declare flask app
app = Flask(__name__)

driver = webdriver.PhantomJS()

cabinet = {'https://www.google.com/search?q=Mike+Pence&tbm=nws': ['Mike Pence, ', 'Vice President, '],
	'https://www.google.com/search?q=Donald+Trump&tbm=nws': ['Donald Trump, ', 'President, '],
    'https://www.google.com/search?q=Rex+Tillerson&tbm=nws': ['Rex Tillerson, ', 'Secretary of State, '],
    'https://www.google.com/search?q=Betsy+DeVos&tbm=nws': ['Betsy DeVos, ', 'Secretary of Education, '],
    'https://www.google.com/search?q=Steven+Mnuchin&tbm=nws': ['Steven Mnuchin, ', 'Secretary of Treasury, '],
    'https://www.google.com/search?q=James+Mattis&tbm=nws': ['James Mattis, ', 'Secretary of Defense, '],
    'https://www.google.com/search?q=Jeff+Sessions&tbm=nws': ['Jeff Sessions, ', 'Attorney General, '],
    'https://www.google.com/search?q=Elaine+Chao&tbm=nws': ['Elaine Chao, ', 'Secretary of Transportation, '],
    'https://www.google.com/search?q=John+F+Kelly&tbm=nws': ['John F. Kelly, ', 'Secretary of Homeland Security, '],
    'https://www.google.com/search?q=Steve+Bannon&tbm=nws': ['Steve Bannon, ', 'White House Chief Strategist, '],
    'https://www.google.com/search?q=Jared+Kushner&tbm=nws': ['Jared Kushner, ', 'Senior Advisor to the President, '],
    'https://www.google.com/search?q=Melania+Trump&tbm=nws': ['Melania Trump, ', 'First Lady, '],
    'https://www.google.com/search?q=Ivanka+Trump&tbm=nws': ['Ivanka Trump, ', 'Businesswoman, '],
    'https://www.google.com/search?q=Reince+Priebus&tbm=nws': ['Reince Priebus, ', 'White House Chief of Staff, '],
    'https://www.google.com/search?q=Nikki+Haley&tbm=nws': ['Nikki Haley, ', 'Ambassador to the United Nations, '],
    'https://www.google.com/search?q=Scott+Pruitt&tbm=nws': ['Scott Pruitt, ', 'Administrator of the Environmental Protection Agency, '],
    'https://www.google.com/search?q=Mick+Mulvaney&tbm=nws': ['Mick Mulvaney, ', 'Director of the Office of Management and Budget, '],
    'https://www.google.com/search?q=Linda+McMahon&tbm=nws': ['Linda McMahon, ', 'Administrator of the Small Business Administration, '],
    'https://www.google.com/search?q=Mike+Pompeo&tbm=nws': ['Mike Pompeo, ', 'Director of the Central Intelligence Agency, '],
    'https://www.google.com/search?q=Sean+Spicer&tbm=nws': ['Sean Spicer, ', 'White House Press Secretary, '],
    'https://www.google.com/search?q=Kellyanne+Conway&tbm=nws': ['Kellyanne Conway, ', 'Counselor to the President, '],
    'https://www.google.com/search?q=Bob+Dole&tbm=nws': ['Bob Dole, ', 'Bob Dole, ']
}

# get number of hits for each person
def get_page():
    time.sleep(1)
    # get 'About x results' data
    hits = driver.find_element_by_id("resultStats")
    # remove comma from number of hits so we can sort
    num = hits.text.replace(',', '')
    # get the number
    popularity = [int(s) for s in num.split() if s.isdigit()]
    return popularity

# run through dict and trigger get_page()
for key in cabinet:
	driver.get(key)
	cabinet.setdefault(key, []).append(get_page())

# declare flask app in root, display with ratings.html template
# return dict ordered by number of hits
@app.route('/')
def home():
	return render_template("ratings.html", cabinetRated = collections.OrderedDict(sorted(cabinet.items(), key=lambda kv: kv[1][2], reverse=True)))

# start flask app
if __name__ == '__main__':
	app.run()

# close phantomJS windown
driver.quit()