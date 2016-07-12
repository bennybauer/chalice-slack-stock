# chalice-slack-stock
This repo uses [SlackStocks](https://github.com/savala/slackStocks) - a slack slash command that gives you pricing information on a stock ticker, 
together with [Chalice](https://github.com/awslabs/chalice) - a Python Serverless Microframework for AWS.

Unlike [Zappa](https://github.com/Miserlou/Zappa), Chalice doesn't use WSGI to serve the requests.   


## Usage
*Currently there's no simple way to initialize an existing chalice project, so follow the next steps:*

[Set up](https://github.com/awslabs/chalice#credentials) you AWS credentials

Create virtual env
		
	mkvirtualenv my-chalice

Install Chalice

	pip install chalice
	
Create a new chalice project

	chalice new-project chalice-slack-stock
	cd chalice-slack-stock
	
Overwrite `app.py` and `requirements.txt` with those of this repository

Install requirements
	
	pip install -r requirements.txt
	
Deploy

	chalice deploy

In your slack team settings, add a Slash Command Configuration
![Add a custom slash command configuration](https://github.com/savala/slackStocks/blob/master/screenshots/setup2.png)

Make sure your settings are like so:

1. Add the command name "/stock"
2. Add in the URL like so "http://<yourappurl>/stock
    * Essentially, in slack when you type in "/stock xyz", it will automatically call the above url as http://yourappurl/stock?text=xyz
3. Set the Method type to GET
4. If you've configured it correctly then you should be good to go! I've added a setup screenshot below as well

![Add a custom slash command configuration](https://github.com/savala/slackStocks/blob/master/screenshots/setup3.png)