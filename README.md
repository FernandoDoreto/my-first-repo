# README file from student to deliver Milestone project

## Project Purpose
* In this project, you'll build a Data Web App to ....


## External user’s goal
* The Data Web App stakeholders are interested to ....

## Data Web App owner's goal
* The goal of this Data Web App is to ....


## Business Requirements 
* 1- We are interested to (know ....)
* 2 -We are interested to (predict ...)
* 3 - We want to analyze (how we ...)
* 4 - We also want (.....)


## Assessment Criteria
### LO35 - 35.2
* ML Task 1: Regression - mapped to Business Requirement 1 - describe what this ML task is doing specifically (ex.: predicting churn levels, recommending personalized product)
* ML Task 2: Classification - mapped to Business Requirement 2 - describe what this ML task is doing specifically


### LO35 - 35.3
* Reg1_BR1: Regression task related to Business Requirement 1 - Linear Model showed better performance (R2) than RandomForest and Decision Tree
* Clf1_BR2: Binary Classifier related to Business Requirement 2 - Logistic Regression showed better performance (Recall) than RandomForest and Decision Tree


### LO35 - 35.4
* Stakeholders:
* Team Structure and role
* End users


### LO36 - 36.1
* Business Requirement 1
  * xxx
  * xxxxx
  * xxxxx
* Business Requirement 2
  * xxxxx
  * xxxx

### LO36 - 36.2
* Reg1_BR1
  * We will create an App to inform....
  * The success metrics are:...  The ML model is considered a failure if ...
  * The output is defined as ....
  * The training data to fit the model come from.... 
  * Heuristics: If we didnt use ML ...

*  Clf1_BR2
   * We will create an App to inform....
   * The success metrics are:...  The ML model is considered a failure if ...
   * The output is defined as ....
   * The training data to fit the model come from.... 
   * Heuristics: If we didnt use ML ...

### LO36 - 36.3
* how to transform Data App to ML API


### LO37 - 37.1
* Data documentation
  * xxxx
  * xxxxx
  * xxxxx
  * xxxxx

### LO37 - 37.2
* CRISP-DM
  * Step 1 Business Understanding: (jsut refer to the business requirements)
  * Step 2 Data Understanding: (might be sth related to EDA)
  * Step 3 Data Preparation: (might be sth related to data cleaning/feat engineering)
  * Step 4 Modeling: (might be one script to define/train a model/pipeline)
  * Step 5 Evaluation: (script related to evaluation)
  * Step 6 Deployment: script related to deployment


### LO37 - 37.3
* xxxxx


### LO38 - 38.1
* script src/processing/data_management.py
  * function xxx, line xxxx, pd.DataFrame() is used for ...
  * function xxx, line xxxx, .groupby() is used for ...

### LO38 - 38.2
* script src/processing/xxxxxx.py
  * function xxx, line xxxx, xxx is used for ...

### LO38 - 38.3
* xxxxxxx







## Mini App Example
* This example is to validate if Python packages from Data Practitioner Course 
(Streamlit, Numpy, Pandas, Matplotlib, Seaborn, Plotly, Sklearn, Tensorflow etc) 
will run properly at **Gitpod** and at **Code Challenge System**

## App Strucutre
* User Story: Explains App Objective
* EDA: Pairplot, Heatmap, 3D plot - validates seaborn and plotly run at gitpod
* Sklearn: Decision Tree model - validates Sklearn runs at gitpod 
* Tensorflow': Sequential model - validates Tensorflow runs at gitpod


## Narrative
* As a Data Analyst from Botanic Garden, you are requested by Special Flower division to develop a 
system capable to distinguish among 3 distinct Iris flowers. 
* Their next field mission at XYZ forest, which is officialy declared as contaminated area and is in 
the middle of nowehere.
The team will harvest the flowers and store on boxes, but each box should have 1 specie type. 
The mission will happen in 10 days and will take 20 days. 

## Business Requirements 
* xxxxx
* xxxxx
* xxxxxxx

## ML Business Case Example
* We will create an App to inform what is the flower species based on sepal and petal measurements. 
It is a 3-class, single-label, classification model: 0 (Setosa), 1 (Versicolour) and 2 (Virginica).
* Our ideal outcome is to provide Special Flowers botanics team a intelligent solution to speed up
species diagnostic during the mission. The field operator will measure, with a ruler or something, 
the petal and sepal and will feed the App.

* The success metrics are: 95% overall accuracy, from the 30th prediction. We expect to have 
15 predictions per day. 
The ML model is considered a failure if Setosa species' Precision and Recall is not 100%. 
This species cant be mixed with other species under no circunstance.


* The output is defined as species class prediction based on flower measurements, 
it will be displayed into the App UI, the field operator will catalogue the measurement/prediction and 
will confirm that prediction belongs to that set of measurements. All measurements and predictions will be
stored locally in the App. There are not latency requirements. 
The ML model needs only inputs from field operator.

* The training data to fit the model come from Botanic Garden database. 
There are, in total, 150 records of all Iris flowers with petal and sepal measurments and 
its correspondent species. 
Botanic Garden warranties the measurments are accurate and free of any bias or error. 


* Heuristics: If we didnt use ML, an alternative option could be to take a flower DNA sample 
and analyze on the field which species that sample belong, but this may take 3h to be done.

