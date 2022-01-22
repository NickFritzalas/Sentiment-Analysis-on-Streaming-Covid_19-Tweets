# Sentiment-Analysis-on-Streaming-Covid_19-Tweets

**Semester project for my MSc in Data Science, Big Data course**

<br>

**Motivation**
Covid-19 has risen various reactions and arguments regarding several aspects of the pandemic
(e.g. vaccinations, the validity of the virus). Nowadays, social media platforms are a basic way of
expressing opinions and sentiments towards a subject and especially under the pandemic where
physical contact has been minimized. This creates a huge and constant flow of relevant data,
which need to be analyzed.

For example, depending on the news feed, the audiences’ attitude and sentiments may swift.
This results into the need of analyzing this attitude-sentiment fluctuation. Such an analysis is useful
in many ways. For instance, governments might be interested in the opinions, attitudes, and
sentiments of the public, after the announcement of a relevant policy.
<br>

**Project Objectives (Hypothesis)**
What is the general public consensus towards the pandemic and related news around the world.

Data Sources

• Twitter will be the data source - Streaming data
• Text messages directly from Twitter’s feed with hashtags such as covid, coronavirus etc.

Big Data Dimensions

• Volume – Thousands of tweets per minute
• Velocity – Increased flow depending on the news
• Veracity – Depending on the reliability of tweets’ source
• Value – Critical information from the data can greatly help in various ways

Solution Overview

• Sentiment analysis via Machine Learning and NLP.
• Collecting tweets from the Twitter API in a streaming manner, storing and processing them
with SPARK
• An ML model will be trained on a labeled dataset after experimentation for creating a high
performing algorithm
• The pretrained model will be deployed in combination with SPARK, on real time data

Tools-Libraries

• Twitter API
• Spark
• Sklearn
• Keras – Tensorflow
• Nltk, pandas, numpy etc.
