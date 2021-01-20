import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """Read messages and categories data and merge them into a single dataframe
    using the [categories] column.
    
    Positional arguments:
    messages_filepath -- file path of messages csv file
    categories_filepath -- file path of categories csv file
    
    Returns:
    dataframe: messages and categories merged dataframe
    """
    
    # read in messages data file
    messages = pd.read_csv(messages_filepath)
    
    # read in categories data file
    categories = pd.read_csv(categories_filepath)
    
    # merge the two dataframes using the 'id' column and return the merged dataframe
    df = messages.merge(categories, how='inner', left_on="id", right_on="id")
    return df


def clean_data(df):
    """Cleans the data in the merged dataframe.
    
    Positional arguments:
    df -- messages and categories merged dataframe
    
    Returns:
    dataframe: cleaned data
    """
    
    # expand 'categories' column into 36 individual columns in a new dataframe
    categories = df["categories"].str.split(pat=";", expand=True)
    
    # use first row of data to rename each column
    row = categories.loc[0]
    category_colnames = list(row.apply(lambda x: x[0:len(x)-2]))
    categories.columns = category_colnames
    
    # convert string values to integer values using the last character
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1:]
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    
    # replace 'categories' column in original dataframe with the expanded columns
    df.drop(["categories"], axis=1, inplace=True)
    df = pd.concat([df, categories], axis=1)
    
    # drop duplicates and return clean dataframe
    columns = df.drop(["id"], axis=1).columns
    df.drop_duplicates(subset=columns, keep="first", inplace=True)
    return df

def save_data(df, database_filename):
    """Writes dataframe to sqlite database containing a table name 'Messages'.
    
    Positional arguments:
    df -- messages and categories merged dataframe
    
    Returns:
    nothing
    """
    
    # write data to a SQLite file in current directory
    db = database_filename
    engine = create_engine('sqlite:///{}.db'.format(db))
    df.to_sql('Messages', engine, index=False, if_exists="replace", chunksize=20)  


def main():
    """Main method begins execution when the program is called.
    
    Positional arguments:
    nothing
    
    Returns:
    nothing
    """
    
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
