# Cybersecurity Machine Learning Capstone

The capstone is assign by [SDA](https://sda.edu.sa) (Saudi Digital Acadimy) in the [Data Governance Program](https://github.com/mhkhoraidah/SDA-Python-Dash-Project/files/7786003/Data.Governance.Program.Calendar.pdf) (Data Science Bootcamp) partner with [Coding Dojo](https://www.codingdojo.com).

## Coders Arm Team:
- Mustafa Khoraidah
  https://github.com/mhkhoraidah
  
- Hala Alsouly: 
  https://github.com/Hala-Alsouly
  
- Amani Almutairi:
  https://github.com/wishes50
  
- Asma Alghamdi:
  https://github.com/Asma-Alghamdi
  
- Mohammed Alshehab:
  https://github.com/MohRaadi

## Objective

Create a machine learning technology to know who most targeted for cyber-crime. The machine learning use a survey dataset. The survey is measuring the level of cybersecurity awareness of cyber-crime in Saudi Arabia. The machine learning building a supervised and unsupervised models to predict the outcomes of being a victim of cyber-crime or not. The purpose is to study, analyze, building models and explore data to obtain the information needed to educate people about cyber-crime and to inform the relevant authorities.


## Dataset: 

The dataset is a survey contains around 66 questions. Some of the questions are personal and others questions related technologies and tools/software that the person used. On the other hand, collecting some cybersecurity activities which aims to assess current information technology knowledge, cyber-crime consciousness to measure what subjects believe and their opinion, case reports, which aimed to evaluate subjects and reactions when they faced a cyber-crime incident. Therefore, there are several points in the data that indicate a lack of awareness of cyber-crime, which needs to be improved and developed.

 - **Source:** https://data.mendeley.com/datasets/fbs9mgmh4y/3

 - **Note:** The survey were between August and October 2019


## Data Cleaning and Preproccessing Structure

### Jupyter Notebook Files Structure:
 - [Data Cleaning and EDA](https://github.com/mhkhoraidah/SDA-Capstone/blob/master/Data%20cleaning%20and%20EDA.ipynb)
   - Export CSV file [Cleaned data.csv](https://github.com/mhkhoraidah/SDA-Capstone/blob/master/Cleaned%20data.csv)
 - [Create a Function to Spit Multi-select String](https://github.com/mhkhoraidah/SDA-Capstone/blob/master/spit%20multi-select%20function.ipynb)
   - Ex. 'Desktop, Laptop, Smartphone' 
     - Genarate a dataframe with selection columns and set 0 or 1
     - If selection is showing in the string so will set 1 under the column name `Desktop`, `Laptop`, `Smartphone`
 - [Preprocessing (convert all strings to numbers)](https://github.com/mhkhoraidah/SDA-Capstone/blob/master/Preprocessing%20(convert%20to%20numbers).ipynb)
   - Required import `multiSelectSplitColumn(column, removeCols = [], selections = [])`
   - Use get_dummies to convert values with the same proiority to cloumns and set 0 or 1
   - Map the values which has some proiority levels to integer values accourding to their level
   - Export CSV file [enumerated data.csv](https://github.com/mhkhoraidah/SDA-Capstone/blob/master/enumerated%20dataset.csv)


## Machine Learning Models

  - [Supervised](https://github.com/mhkhoraidah/SDA-Capstone/blob/master/Supervised%20ML.ipynb)
    - Logistic Regression
    - Decision Tree Classifier
    - Random Forest
    - Support Vector Machine (SVM)
    - Artificial Neural Network (ANN) 
 
  - [Unsupervised](https://github.com/mhkhoraidah/SDA-Capstone/blob/master/Unsupervised%20ML.ipynb)
    - KMeans
    - PCA
    
  

## How to run the Project
```
>> need to add the command to run the project
```
