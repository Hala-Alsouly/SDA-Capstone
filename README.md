# Cybersecurity Machine Learning Capstone

The capstone is assign bt [SDA](https://sda.edu.sa) (Saudi Digital Acadimy) in the [Data Governance Program](https://github.com/mhkhoraidah/SDA-Python-Dash-Project/files/7786003/Data.Governance.Program.Calendar.pdf) (Data Science Bootcamp) partner with [Coding Dojo](https://www.codingdojo.com).

# Coders Arm Team:
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
  
  
# Abstract

The idea of the project is to collect data by making a survey to measure the level of cybersecurity awareness of cyber- crime in Saudi Arabia.  The survey recruited 1230 Saudi nationals with different backgrounds and relies on knowledge and attitude aspects. The collected data were gathered between August and October of 2019. The survey contains several questions, which are listed below.  Personal and skills information, Cybersecurity Activities which aims to assess current Information technology knowledge, Cybercrime Consciousness to measure what subjects believe and their opinion, Case Reports, which aimed to evaluate subjects and reactions when they faced a cybercrime incident. The purpose of the project is to study, analyze, building models and explore data to obtain the information needed to educate people about cybercrime and to inform the relevant authorities.

# Dataset source: 

https://data.mendeley.com/datasets/fbs9mgmh4y/3


# Background of the study

Many people think that security is not outside the scope of its traditional concept. But the concepts have recently expanded to include many types of security, foremost of which is cyber security, which has become an urgent necessity after the emergence of the Fourth Industrial Revolution or what is known as the data revolution, because the Internet space has become teeming with electronic transactions and transactions that need to be encrypted and secure those transactions.

The concept of cybersecurity is more comprehensive and broader than information security, especially if we considered data protection and various informational applications such as e-government, e-commerce, e-health, e-education and information society. At present, the vision of the Kingdom of Saudi Arabia aims to develop and teach a lot in the field of information technology, especially cybersecurity. Several platforms and academies have been established by the government to educate people about the importance of the field of cyber security, including the National Cyber Security Authority, the Saudi Digital Academy, the Tuwaiq platform and many more platforms. Also, there are many cyber security courses given to all age groups to raise awareness in protecting their information.  This survey was conducted to study several criteria to see people's awareness of cybercrime, including the level of study, age group, administrative regions, purpose of using the Internet, level of Internet skills, system used, practices used in the Internet, type of communication, security knowledge, type of device , the software used to protect against viruses, have you been a victim before in cybercrime or not, and many questions that aim to see the level of awareness and knowledge and also see the practices that made you exposed to a victim of cybercrime


# Business Problem 

It turns out that there are some who have no awareness of cybercrime and do not know how to protect their information. There are also bad practices in the use of computers and the Internet, including: those who browse in unsafe sites without their knowledge, and there are some who do not use virus protection programs in their devices. There are also those who use easy passwords and make them match personal information, which means it is easy to fall victim to an information crime. There are some people who do not read the terms and conditions for registering on some sensitive sites and they should be alerted about this.
Therefore, there are several points in the data that indicate a lack of awareness of cybercrime, which needs to be improved and developed.


# Motivation for the Project

Talking about how to raise societal awareness of obtaining safety and security in the world of the Internet and protecting the digital identity, we should draw attention to the Internet access guidelines according to age groups and education level.  Finding bad practices in the use of the Internet through the data collected to raise awareness.  The data are important since they evaluate the level of awareness of Saudis based on aspects not covered in previous studies, such as using participants of different backgrounds, regions and expertise in utilizing technology.  The data can be useful for Saudi authorities such as the National Cybersecurity authority as well as researchers who are interested in the cybersecurity field.  The data can be utilized for educational purposes in terms of short courses and training.


# Approaches and Methodologies 

The project uses machine learning technology to see the criteria that cause the victim of a cybercrime through the practices used by the user on the Internet and computer use. The technology used for the project is supervised learning and unsupervised concept to predict the outcomes of being a victim of cybercrime or not.  


# Data Cleaning and Preproccessing Structure

### Jupyter Notebool Files Structure:
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

# Machine Learning Models

  - [Supervised](https://github.com/mhkhoraidah/SDA-Capstone/blob/master/Supervised%20ML.ipynb)
    - Logistic Regression
    
        ```
        Training Accuracy: 0.9639175257731959
        Testing Accuracy:  0.9588477366255144 
        Precision:         0.830508 
        Recall:            1.000000
        ```
    - Decision Tree Classifier
    
        ```
        Training Accuracy: 0.9670103092783505
        Testing Accuracy:  0.9588477366255144
        Precision:         0.830508
        Recall:            1.000000
        ```
        
    - Random Forest
        
        ```
        Training Accuracy: 0.9938144329896907
        Testing Accuracy:  0.9053497942386831
        Precision:         0.837209
        Recall:            0.692308
        ```    
        
  - [Unsupervised](https://github.com/mhkhoraidah/SDA-Capstone/blob/master/Unsupervised%20ML.ipynb)
    - PCA
    
        ```    
        Training Accuracy: 0.9237113402061856
        Testing Accuracy:  0.9053497942386831
        ```   
        
    - KMeans

    - SVM
  



