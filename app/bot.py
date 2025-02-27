import tweepy
import re

from app.config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET, BEARER_TOKEN

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

def list_urls(text: str):
		matches = re.findall(r"(https://twitter.com/[^ \n]+)|(https://x.com/[^ \n]+)", text)
		urls_list = [x[0]+x[1] for x in matches]
		return urls_list

def auto_reply(urls: str, text: str):
	list = list_urls(urls)
	
	count = 1
	for url in list:
		id = re.findall(r'[0-9]+', url.split('/')[-1])
		id = id[0]	
		try:
			response = client.create_tweet(text=text, in_reply_to_tweet_id=id)
			status = "Successful"
			print(f"{count}.", status)
		except Exception as e:
			status = str(e).split('\n')[-1]
			print(f"{count}.", status)
		
		count += 1