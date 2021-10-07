
**Introduction**

When selling used goods online, a combination of tiny, nuanced details in a product description can make a big difference in drumming up interest.

Avito, Russia’s largest classified advertisements website is challenging to predict demand for an online advertisement based on its full description (title, description, images, etc.), its context (geographically where it was posted, similar ads already posted) and historical demand for similar ads in similar contexts. With this information, Avito can inform sellers on how to best optimize their listing and provide some indication of how much interest they should realistically expect to receive.

Source: https://www.kaggle.com/c/avito-demand-prediction

**Data Description :**

**File and column descriptions**

- train.csv - Train data.
- item_id - Ad id.
- user_id - User id.
- region - Ad region.
- city - Ad city.
- parent_category_name - Top level ad category as classified by Avito's ad model.
- category_name - Fine grain ad category as classified by Avito's ad model.
- param_1 - Optional parameter from Avito's ad model.
- param_2 - Optional parameter from Avito's ad model.
- param_3 - Optional parameter from Avito's ad model.
- title - Ad title.
- description - Ad description.
- price - Ad price.
- item_seq_number - Ad sequential number for user.
- activation_date- Date ad was placed.
- user_type - User type.
- image - Id code of image. Ties to a jpg file in train_jpg. Not every ad has an image.
- image_top_1 - Avito's classification code for the image.
- deal_probability - The target variable. This is the likelihood that an ad - actually sold something. It's not possible to verify every transaction with certainty, so this column's value can be any float from zero to one.
- test.csv - Test data. Same schema as the train data, minus deal_probability.

**Evaluation Criteria**

The regression model should be evaulated for Root Mean Squared Error 𝑅𝑀𝑆𝐸.

RMSE is defined as:

![rmse](https://imgur.com/ZsHq13D.png)



**Summary**

In this notebook we will explore Supervised Machine Learning methods. Regression models such as linear regression, Ridge, ElasticNet, Lasso, decision tree and ensemble models such as RandomForest, XGBoost, LightGBM will trained to predict weekly sales using Scikit Learn, LightGBM and XGBoost. We will use Pandas, Numpy, Matplotlib, Seaborn and Plotly to perform exploratory data analysis and gather insights for machine learning. We will do the following

- Install and Import libraries
- Explore the dataset and merge different files as required
- Translate the business problem to a machine learning problem
- EDA - exploratory data analysis
- Feature Engineering
- Data preparation - Train Val Split, Encoding, Imputing and Scaling
- Select input features
- Define evaluation criteria (here. RMSE - as defined above)
- Define baseline model
- Select best model (without hyperparameter tuning)
- Hyperparameter tuning for select models
- Make predictions
- Save the best model
- Summarise insights and learnings
