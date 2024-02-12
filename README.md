## Disinformation Project Demo

**TL;DR: I used YouTube captions to train an ML model to tell me whether some piece of text was fake news.**

These are the Python modules that I wrote as part of my undergraduate capstone project, which was a Chrome browser extension that allowed the user to select text from a given webpage and check whether it could be classified as 'disinformation.' We called it _RealNews_.

It was a group project, and the three of us had pretty distinct roles: Marco built the frontend, Jorge built the backend, and I did the data engineering.

I'm not a web developer and have very little experience with building APIs, so I cleaned up the repository so that it only demonstrates the code that used to gather the data and  to train the ML model for the browser extension.

Here's how I did it:

I made a list of YouTube channels that focused on wacky conspiracy theories and another list of YouTube channels for reputable news sources (e.g., NYT, WSJ). Then I used Selenium and a random YouTube python module to crawl through each channel and download the auto-generated captions from every video that each channel in each respective list had ever posted (`/ml_tools/youtube_caption_crawler.py`). I classified the captions from the former list as `FAKE`, and the captions from the latter list as `REAL`.

Then, I put all of that data into an enormous CSV file, cleaned up the caption text using the Natural Language Toolkit Python module (`clean_text.py`) and fed the data to scikit-learn to train a machine learning model using Logistical Regression. There's some code in there that suggests that I split the data into test and train datasets to calculate accuracy scores, but I suspect that I conducted those tests in a different script and lost it. In any case, I settled on the Logistic Regression algorithm and dumped the ML model into a pickle file. We then used that pickle to make our predictions about a given piece of text.

#### Had I known what I know now, I would have done the following: 
  _Note: I didn't learn a single thing about cloud platforms OR source control in my undergraduate coursework. Go ASU Sun Devils :P_
- Invested in the free trial for Azure that Microsoft offers for students.
- Used an Azure Function instance to run the code to ingest the data. **That script took over 24 hours to run on my Dell Latitude.**
  - If I had felt even more ambitious, I'd have configured a Kubernetes cluster to do the data ingestion. 
- Used Azure's ML as a Service product to test and train the ML model more thoroughly.
- Experimented more with ML algorithms before landing on Linear Regression. I didn't understand the difference between different ML algorithms, so I'm pretty sure I settled on the Logistic Regression algorithm because I thought it sounded cool.
- Used multithreading.
- Found a way to continue to grow the dataset with which to continuously retrain the ML model.
- Made better use of Git.

Some of the shortcomings of this project were due a lack of knowledge on my part, but a lot of them came from a sheer lack of time - I was working full-time as a barista, server, bartender, and Uber driver (sometimes concurrently) while developing this.
