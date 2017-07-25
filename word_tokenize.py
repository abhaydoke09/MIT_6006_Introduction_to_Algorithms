import re
from bs4 import BeautifulSoup
import requests
import operator

r = requests.get('http://nautil.us/issue/49/the-absurd/why-your-brain-hates-other-people')
soup = BeautifulSoup(r.text, "html.parser")
text = soup.get_text().lower()

text = re.sub(r'[^a-zA-Z0-9_\- ]',' ', text)
text = re.sub(r'\s+',' ', text)
text = re.sub(r'\s\d+\s','', text)
text = ' '+text+' '

unigram_stats = {x:len(re.findall(x, text)) for x in text.split(' ')}
unique_words = unigram_stats.keys()
#bigram_stats = {x+' '+y:len(re.findall(x+' '+y, text)) for x in text for y in unique_words}
text_list = list(text.split())
bigram_stats = {}
for i in range(len(text_list)-1):
	bigram = text_list[i]+' '+text_list[i+1]
	if bigram in bigram_stats:
		bigram_stats[bigram]+=1
	else:
		bigram_stats[bigram]=1

print sorted(bigram_stats.items(), key=operator.itemgetter(1), reverse=True)[:10]
#print text