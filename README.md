# How Machine Learning Can Improve Disaster Response
![](https://nplusonemag.com/wp-content/uploads/2017/09/37178284932_44dedea535_z.jpg)
<br><sub>source: https<span></span>://nplusonemag<span></span>.com/online-only/online-only/austerity-natural-disaster/</sub>

## Table of Contents
1. [Folder Structure](#Structure)
2. [Installation](#Installation)
3. [Project Motivation](#Motivation)
4. [ETL Pipeline](#ETLPipeline)
5. [ML Pipeline](#MLPipeline)
6. [Evaluation](#Evaluation)
7. [Deployment](#Deployment)
8. [Licensing, Authors, Acknowledgements](#License)

## <a name="Structure"></a>Folder Structure
-   app  
    | - template  
    | |- master.html  # main page of web app
    | |- go.html  # classification result page of web app  
    |- run.py  # Flask file that runs app
-   data  
    |- disaster_categories.csv  # data to process  
    |- disaster_messages.csv  # data to process  
    |- process_data.py  # python code to combine and clean datasets
    |- DisasterResponse.db # database to save clean data to
-   models  
    |- train_classifier.py  # python code that generates and exports the ML model
    |- classifier.pkl  # saved model
-   README.md

## <a name="Installation"></a>Installation
1. Additional Libraries: No additional libraries are required.

2. ETL Process: In the 'data' folder execute the command line below to process the datasets and output the sqlite database.
<br>'python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db'

2. ML Model: In the 'models' folder execute the command line below to use the cleaned date to generate the ML model.
<br>'python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl'

3. Flask Web App: In the 'app' folder execute the command line below to initiate the web app then open in web browser.
<br>'python run.py'

### <a name="Motivation"></a>Project Motivation
Use real-world data to explore the use of Pipelines and Machine Learning models in Python classify text messages during a disaster.

### <a name="ETLPipeline"></a>ETL Pipeline
The original data is contained in 2 separate files, one containing text messages in original language and an English translation.  The second file contains all of the classifications that relate to each message.  Some of the challenges with the raw data are 1) a single message may appear multiple times with different unique id numbers, 2) the categories for each message combined into a single text string and need to be parsed, and 3) some messages have a category indicator of 2 while the only values allowed should be 0 or 1.  During this process, the data is read in from both files and joined using the \[id\] field.  The categories are then separated into individual columns and the numerical values of 0 and 1 are then used to indicate if the message is or is not associated.  Finally, the rows with duplicate messages or invalid numerical values are removed from the data.  The resulting clean dataset is then exported to a sqlite database for use by the ML Pipeline process.

### <a name="MLPipeline"></a>ML Pipeline

### <a name="Evaluation"></a>Evaluation

### <a name="Deployment"></a>Deployment

## <a name="License"></a>Licensing, Authors, Acknowledgements

