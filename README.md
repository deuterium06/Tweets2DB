Personal repo for scraping tweets using Snscrape repo & then storing tweets into MYSQL database.
Check out repo source <a href='https://github.com/JustAnotherArchivist/snscrape'>here</a>.

**<h3>Installations:</h3>**
1. Python 3.10.0 and up 
2. MySQL 8.0
3. Pip installation in Python

**<h3>Setting up environment & database:</h3>**

Python
1. Create a virtual environment where you'll install dependencies. Follow along with this <a href='https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/'>instruction</a>.
2. Once you're inside your virtual env, run `pip install requirements.txt`

MySQL
1. In MySQL Command Line, configure your username & password. Then, run `CREATE DATABASE tweets;` as it's where data will be stored.
2. Open `credentials.yml.sample` in this folder and update the values accordingly. Save it as `credentials.yml`. 

Once Python & MySQL dependencies have been set up, in your command line, 
1. Run `python tweet_snscraper.py`. This will handle running of data extraction task from Twitter straight to your local database. 
2. Run `python tweet_ETL.py`. This will process the extracted raw data into a relational tables. 

To check if the code has populated data, I suggest you use MySQL Workbench. But it should also work on other IDEs you prefer. 

**<h3>(Optional) Run schedule for ETL in your local computer:</h3>**

This requires your computer to be on & should be connected to internet.
1. For Linux, use Linux's built-in utility Cron to run schedule.
2. For Windows, use Task Scheduler.

**<h3>(Optional) Connect your database to BI Tools:</h3>**
I used Power BI Desktop to check ETL activity of my program. Installation & connection is very easy! Just check out resources online to learn more. Here's my sample dashboard for ETL overview.

![sample dash for my database](/image/sample_dash.png)
