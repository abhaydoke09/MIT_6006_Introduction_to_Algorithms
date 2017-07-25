import re
from bs4 import BeautifulSoup
import requests

r = requests.get('http://nautil.us/issue/49/the-absurd/why-your-brain-hates-other-people')
soup = BeautifulSoup(r.text, "html.parser")
text = soup.get_text().lower()

text = re.sub(r'[^a-zA-Z0-9_ ]',' ', text)
text = re.sub(r'\s+',' ', text)
text = re.sub(r'\s\d+\s','', text)
text = ' '+text+' '

unigram_stats = {x:len(re.findall(x, text)) for x in text.split(' ')}
unique_words = unigram_stats.keys()
#bigram_stats = {x+' '+y:len(re.findall(x+' '+y, text)) for x in text for y in unique_words}
print len(unique_words)
#print text