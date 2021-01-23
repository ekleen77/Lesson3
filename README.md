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

### <a name="BusinessUnderstanding"></a>Business Understanding

### <a name="DataUnderstanding"></a>Data Understanding

### <a name="ETLPipeline"></a>ETL Pipeline

### <a name="MLPipeline"></a>ML Pipeline

### <a name="Evaluation"></a>Evaluation

### <a name="Deployment"></a>Deployment

## <a name="License"></a>Licensing, Authors, Acknowledgements

