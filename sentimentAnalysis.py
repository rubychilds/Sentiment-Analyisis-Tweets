import urllib
import re


def getFiles(fileList, path):
	for file_name in fileList:
		urllib.urlretrieve(path + file_name, file_name)

def getLists(fileList):
	tweets = fileToList('obama_tweets.txt')
	positiveWords = fileToList('positive.txt')
	negativeWords = fileToList('negative.txt')
	return tweets, positiveWords, negativeWords

def fileToList(fileName):
	fileText = open(fileName).read()
	return fileText.split('\n')

def analyseTweetFile(tweetFileName):
	tweets = open(tweetFileName).read()
	# To be continued -> short summary regarding entirity of tweets

def tweetWordSummary(tweets, positiveWords, negativeWords):
	for tweet in tweets:
		tweet = tweet.lower()
		tweet = tweet.translate(stringIn.maketrans("",""), string.punctuation)
		re.sub(r'\s+|\t+\n', ' ', tweet)
		wordsInTweet = tweet.split(' ')
		wordCount = len(wordsInTweet)

		# To be continued - considering what is the most useful info we can extract from tweet
		for word in wordsInTweet:
			if word in positiveWords:

			elif word in negativeWords:


def main():
	path = 'http://www.unc.edu/~ncaren/haphazard/'
	fileList = ['positive.txt', 'negative.txt', 'obama_tweets.txt']
	getFiles(fileList, path)
	tweets, positiveWords, negativeWords = getLists(fileList)

	tweetWordSummary(tweets, positiveWords, negativeWords)



if __name__ == '__main__':
	main()