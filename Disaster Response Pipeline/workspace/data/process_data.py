import sys
import pandas as pd
from sqlalchemy import *

def load_data(messages_filepath, categories_filepath):
    ''' 
        Takes input of message and categories csv files datapath.
        Merge them into a new dataframe df on 'id'
        Return dataframe df
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, on='id', how='outer')
    return df

def clean_data(df):
    ''' 
        Takes the input of dataframe df, that was merged into last function.
        Perform data cleaning on the dataframe before modeling
        Splits Categories into separate category columns
        Replace categories column in df with new category columns
        Remove duplicates 
    '''
    # create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(';', expand=True)
    # select the first row of the categories dataframe
    row = categories.iloc[0]
    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    category_colnames = list(map(lambda c:c.split("-")[0], categories.iloc[0].values.tolist()))
    # rename the columns of `categories`
    categories.columns = category_colnames    
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]
        # convert column from string to numeric
        categories[column] = categories[column].apply(pd.to_numeric)
        
    # drop the original categories column from `df`
    df=df.drop('categories', axis=1)
    # check number of duplicates
    duplicate_count=df[df.duplicated()].shape[0]
    print(duplicate_count)
    
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)
    
    # drop duplicates
    df.drop_duplicates(inplace=True)
    return df


def save_data(df, database_filename):
    ''' 
    Saves the clean database to a table with the name provided as the function parameter
    '''
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('Response', engine, index=False) 
      


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()