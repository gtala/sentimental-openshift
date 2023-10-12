# Openshift - Sentiment Analysis
###################

sentiment-spanish is a python library that uses convolutional neural networks to predict the sentiment of spanish sentences. The model was trained using over 800000 reviews of users of the pages eltenedor, decathlon, tripadvisor, filmaffinity and ebay. This reviews were extracted using web scraping with the project opinion-reviews-scraper

Using the rate in the user reviews we trained the model to learn from the language in them. For that we use the libraries Keras and Tensorflow. We achieved a validation accuracy (accuracy over fresh data, no used for training) of 88%. For more details regarding the training of the neural network model check the repo sentiment-analysis-model-neural-network

https://pypi.org/project/sentiment-analysis-spanish/

#Enable Pod Balance
------------------

Router -> edit YAML


	kind: Route
	metadata:
	  annotations:
		haproxy.router.openshift.io/balance: roundrobin
		haproxy.router.openshift.io/disable_cookies: 'true'
