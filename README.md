## Mini App Example
* This example is to validate if Python packages from Data Practitioner Course 
(Streamlit, Numpy, Pandas, Matplotlib, Seaborn, Plotly, Sklearn, Tensorflow etc) 
will run properly at **Gitpod** and at **Code Challenge System**

## App Strucutre
* User Story: Explains App Objective
* EDA: Pairplot, Heatmap, 3D plot - validates seaborn and plotly run at gitpod
* Sklearn: Decision Tree model - validates Sklearn runs at gitpod 
* Tensorflow': Sequential model - validates Tensorflow runs at gitpod


## Narrative and Business Requirements
* As a Data Analyst from Botanic Garden, you are requested by Special Flower division to develop a 
system capable to distinguish among 3 distinct Iris flowers. 
* Their next field mission at XYZ forest, which is officialy declared as contaminated area and is in 
the middle of nowehere.
The team will harvest the flowers and store on boxes, but each box should have 1 specie type. 
The mission will happen in 10 days and will take 20 days. 

### ML Business Case
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


