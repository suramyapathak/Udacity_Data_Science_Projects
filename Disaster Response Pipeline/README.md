<img src="https://live.staticflickr.com/5328/9554405492_b8f8e73fe6_b.jpg" alt="Disaster Response" />
# Data Scientist Nanodegree Program
#Data Engineering
# Project: Disaster Response Pipeline


### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


### Installations

This project requires **Python 3.x** and the following Python libraries installed:

- scikit-learn==0.21.3
- pandas==0.25.1
- numpy==1.18.1
- matplotlib==3.3.1
- seaborn==0.9.0
- sqlalchemy==1.3.9
- nltk==3.4.5

Install [iPython Notebook](http://ipython.org/notebook.html)

Install [Anaconda](https://www.anaconda.com/products/individual), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.

## Project Motivation

As per Udacity Data Scientist Nanodegree project Disaster Response Pipeline Project, the project uses data from Figure Eight to build a model for an API to classify disaster messages.

###Summary of the Project

The project gives a opportunity to work on real world problem, a data set containing real messages that were sent during disaster events, we created a machine learning pipeline to categorize these events so that you can send the messages to an appropriate disaster relief agency.


### Licensing, Authors, Acknowledgements 

- Data provided is as per Udacity Nanodegree program 
- This project is part of Data scientist Nanodegree Program from udacity 
- The findings here are observational, not the result of a formal study.

Header image is covered by the Creative Commons Zero license. The  license was released by the non-profit organization Creative Commons. You can get more information about Creative Commons and their license on the official license page.

The Header Image is "Forest fire" by Ervins Strauhmanis is licensed with CC BY 2.0. To view a copy of this license, visit https://creativecommons.org/licenses/by/2.0/