<h1 align="center"> WallStreetBot @ ShellHacks </h1>
<br>

# 💭 What is WallStreetBot?
<p> We are Prophets of Profits. Our ML Model is for the average retail trader to use to aid in their stock trading journey.</p>

# ✨ Inspiration
<p>We were inspired by the subreddit wallstreetbets. Everyday regular people like you and us post their 4, 5, 6 and 7-figure losses in their attempt to "defeat" the hedge funds and "beat" the casino but constantly fall short. We decided to make sure these losses happen less often by informing traders.</p>

# ⚙️ What it does
<p>Put simply, our ML Model predicts whether the closing price of a stock or coin will be higher tomorrow (or next trading day) than the closing price today. (Since crypto is 24/7, open and close is the just price at midnight that day). The AI model progressively learns with more data and is getting smarter each day.</p>

# 🔨 How we built it
<p>We made an app file containing our Flask application. This was the root of it all. This app script interacts with our python script (ml model) and the different html pages. It takes care of get and post api calls and displaying the appropriate page. Forms are used within the html files to track user input. We use a RandomForestClassifier model to predict our target variable. In this case it's a 1 or 0 depending on whether the stock/coin goes up or down. We use a list of predictors that will train the model and give it a better chance of predicting our target.</p>

# 🗿 Challenges we ran into
<p>The biggest challenges we ran into were regarding version control in Git and a few display issues that were a combination of Flask, html and css issues. Due the small amount of time, we were unable to thoroughly test the accuracy of the model, but it will improve with more time and data.</p>

# 👑 Accomplishments that we're proud of
<p>We are proud of the fact that we created a working website with a sophisticated and user-friendly UI and multiple working features. The base level stock and crypto prediction is the just beginning! An advanced algorithm is being worked on right now!</p>

# 🧠 What we learned
<p>We learned about developing an application from start to finish. Our team consisted of members who knew either frontend or backend or neither. We worked together to combine the 2 sides into a working application.</p>

# 🤖 What's next for WallStreetBot
<p>The bot is getting smarter everyday as are its creators that brought it to life. We are continuing to improve the model as well as bringing new features. We are going to develop paper trading funcionality and create more advanced models for longer term predictions. We also want to give user option between short and long term options.</p>

# How to run:
#### Only local functionality is available at the moment. Need to install the modules for flask, pandas, matplotlib, plotly, scikit-learn, yfinance in order to run all functions.
#### Run the command python3 app.py, python app.py or flask run in the terminal to start the app. copy the local url into browser and use.
#### crtl C in command line to kill app
