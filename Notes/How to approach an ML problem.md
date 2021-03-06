
1. Identify the problem is Supervised or UnSupervised. 
   * Supervised: You know what needs to be predicted. 
   * UnSupervised: No targets, we looks for structure/pattern of the data. 
     * Supervised:
        - Classification
        - Regression
     * Unsupervised
        - Clustering
        - Dimensionality Reduction 
        - Association/Recommendation 

![image](https://user-images.githubusercontent.com/63992365/126795442-d34889ea-0da9-4305-b593-3d1ab46252df.png)
    
 
2. Loss Functions and Evaluation Metrics  
    - Evaluation Metrics Used in Regression Task
      * RMSE (Root Mean Squared Error)
      * RMSLE (Root Mean Squared Logarithmic Error)
      * MAE (Mean Absolute Error)
      * R-Squared (R²)

    - Evaluation Metrics Used in 0/1 Prediction in Binary Classification Task
      * Accuracy and Error Rate
      * Precision and Recall
      * F1-Score and Fbeta-Score
      * MCC (Matthews Correlation Coefficient)
      * Balanced Accuracy
      * Log Loss (or Cross Entropy or Negative Log-Likelihood)
      * AUCROC (Area Under the Receiver Operating Characteristic Curve)

![image](https://user-images.githubusercontent.com/63992365/126806563-be9e27ab-b720-4c60-80fc-659a78f7c484.png)

3. Data Cleaning 
    - Download the datasets using `opendatasets` and merge datasets if needed.
    - Load using `pandas`
    - Check the data range - describe(), duplicate or invalid, negative data etc.
    - Null values - Check distribution of data, if normal distribution, `mean` / average is       fine, if exponential distribution then `median` should be fine or drop the rows, or         put 'Unknown' or fill with the average value of top and bottom rows etc. 
   - Check of how much data is available, like do we have date for entire year to make a full year of prediction etc.
    
    
4. Data Viz and EDA
  - Study individual (all) column distribution - uniform, normal or exponential based on       that you can fill the missing values, if one column is exponential and it's correlation     with to target is exponential, then taking logarithm of the column would give you           better result. 
  - Detect anomalies or errors in the data (e.g. missing/incorrect/zeros values)
  - Study the relationship of target column with other columns (linear, non-linear etc.)
  - Gather insights about the problem and the dataset
  - Come up with ideas for preprocessing and feature engineering (ex: deriving new columns     from existing columns, day/month/week/weekday/weekend etc, add holiday, promotions,         weather etc)


5. Data Preprocessing
  - time based train/val set (if you have to predict some data in future rather than random     split.
  - target should not be in train or val dataset (only columns in test set can be there in train & val dataset)
  - Categorize the numerical and categorical columns. Make sure that we are not making columns categorical (if the count is a lot) -> curse of dimentionality; starts overfitting. 
  - Impute missing value 
  - Scale the data
  - One Hot encode
  - Create - X_train, X_val and X_test

6. Baseline Models
  - create a base model to compare your model
7. 
