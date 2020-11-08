# Data Scientist Nanodegree Program

# Capstone Project

# Project: Sparkify

### GitHub link: 
https://github.com/suramyapathak/Udacity_Data_Science_Projects/tree/master/Folder/Spark



### Instructions:
1. Run Sparkify Git.ipynb


### Installations

This project requires **Python 3.x** and the following Python libraries installed:
- pandas
- numpy
- matplotlib
- seaborn
- pyspark


Install [iPython Notebook](http://ipython.org/notebook.html)

Install [Anaconda](https://www.anaconda.com/products/individual), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.


###Summary of the Project

Sparkify Project Workspace

Suppose, we are the data team of a popular digital music service similar to Spotify or Pandora. The users stream their favorite songs either using the free tier that place advertisements between songs or use the premium plan for which they pay a monthly fee without any advertisements between songs. Users can upgrade, downgrade or altogether cancel their services. The dataset given to us contains a log of the activities of each user on the service whether they are playing songs, logging out, upgrading their service or cancelling it. All this data contains key insights in keeping the users of the service happy. Our task in this project is to develop a model that predict which users are at risk. If we can identify users that are at risk to churn either by downgrading from premium or by cancelling their service, the business can offer them incentives and discounts potentially saving millions in revenues.

The models are evaluated using the F1 score since we have a small number of churned users. F1 score is a better measure to use when there is an uneven class distribution. For our dataset, Gradient Boosted Tree Classifier gives the best F1 score. We also calculate the accuracy of each of the models but we base our decision of selecting a model based on the F1 score calculated.
