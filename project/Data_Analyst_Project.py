#!/usr/bin/env python
# coding: utf-8

# # Proyek Analisis Data: E-Commerce
# - **Nama:** Raissa Calista Salsabila
# - **Email:** salsabilaahsn@gmail.com
# - **ID Dicoding:** calistaas

# ## Defining Business Questions

# - Which state have the highest concentration of customers placing orders?
# - What is the product category with the highest number of orders? 
# - What was the month with the highest number of orders in 2017? Can we get the any insight from that data to use for this year (2018)?
# - How is our customer segmentation? (RFM Analysis)

# ## Import All Packages/Libraries Used

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# ## Data Wrangling

# ### Gathering Data
# To read the data I use read_csv function from pandas with the addition using the escape char "r" to read the file path

# 1. Read the customer data and save it in customers_df variable.

# In[2]:


customers_df = pd.read_csv(r"D:\Bangkit\Assessment\Dicoding Assesment\dataset\customers_dataset.csv")
customers_df.head()


# 2. Read the geolocation data and save it in geos_df variable.

# In[3]:


geos_df = pd.read_csv(r"D:\Bangkit\Assessment\Dicoding Assesment\dataset\geolocation_dataset.csv")
geos_df.head()


# 3. Read the order items data and save it in order_items_df variable.

# In[4]:


order_items_df = pd.read_csv(r"D:\Bangkit\Assessment\Dicoding Assesment\dataset\order_items_dataset.csv")
order_items_df.head()


# 4. Read the order reviews data and save it in order_reviews_df variable.

# In[5]:


order_reviews_df = pd.read_csv(r"D:\Bangkit\Assessment\Dicoding Assesment\dataset\order_reviews_dataset.csv")
order_reviews_df.head()


# 5. Read the order data and save it in order_data_df variable.

# In[6]:


order_data_df = pd.read_csv(r"D:\Bangkit\Assessment\Dicoding Assesment\dataset\orders_dataset.csv")
order_data_df.head()


# 6. Read the products data and save it in products_data_df variable.

# In[7]:


products_data_df = pd.read_csv(r"D:\Bangkit\Assessment\Dicoding Assesment\dataset\products_dataset.csv")
products_data_df.head()


# 7. Read the product category name in English data and save it in products_eng variable.

# In[8]:


products_eng_df = pd.read_csv(r"D:\Bangkit\Assessment\Dicoding Assesment\dataset\product_category_name_translation.csv")
products_eng_df.head()   


# 8. Read the seller data and save it in seller_data_df variable.

# In[9]:


seller_data_df = pd.read_csv(r"D:\Bangkit\Assessment\Dicoding Assesment\dataset\sellers_dataset.csv")
seller_data_df.head()


# ### Assessing Data

# #### Assessing Customer Data

# In[10]:


#using the info function to know the structure of the data frame
customers_df.info()


# In[11]:


#check the missing value for each column
customers_df.isna().sum()


# In[12]:


#check the duplicates
print("Total of duplicates: ",customers_df.duplicated().sum())


# In[13]:


#check the summary statistics for the numerical column
customers_df.describe()


# #### Assessing Geolocation Data

# In[14]:


#using the info function to know the structure of the data frame
geos_df.info()


# In[15]:


#check the missing value for each column
geos_df.isna().sum()


# In[16]:


#check the duplicates
print("Total of duplicates: ",geos_df.duplicated().sum())


# In[17]:


#check the summary statistics for the numerical column
geos_df.describe()


# #### Assessing Order Items Data

# In[18]:


#using the info function to know the structure of the data frame
order_items_df.info()


# As the ouput from the code above, the date still use object as the datatype, I will change it later during the cleaning process

# In[19]:


#check the missing value for each column
order_items_df.isna().sum()


# In[20]:


#check the duplicates
print("Total of duplicates: ",order_items_df.duplicated().sum())


# #### Assessing Order Reviews Data

# In[21]:


#using the info function to know the structure of the data frame
order_reviews_df.info()


# In[22]:


#check the missing value for each column
order_reviews_df.isna().sum()


# Too many empty values for the comment title and its message, as I can say only giving the score is mandatory

# In[23]:


#check the duplicates
print("Total of duplicates: ",order_reviews_df.duplicated().sum())


# In[24]:


#check the summary statistics for the numerical column
order_reviews_df.describe()


# #### Assessing Products Data

# In[25]:


#using the info function to know the structure of the data frame
products_data_df.info()


# the product quantity still use float as its datatype, meanwhile to measure a quantity we should use an integer datatype

# In[26]:


#check the missing value for each column
products_data_df.isna().sum()


# In[27]:


#check the duplicates
print("Total of duplicates: ",products_data_df.duplicated().sum())


# In[28]:


#check the summary statistics for the numerical column
products_data_df.describe()


# #### Assessing Product Category (Eng Trans) 

# In[29]:


products_eng_df.info() 


# In[30]:


#check the missing value for each column
products_eng_df.isna().sum()


# #### Assessing Order Data

# In[31]:


#using the info function to know the structure of the data frame
order_data_df.info()


# All the date variable still using the object datatype.Of course we should change it to gather more information.

# In[32]:


#check the duplicates
print("Total of duplicates: ",products_eng_df.duplicated().sum())


# In[33]:


#check the missing value for each column
order_data_df.isna().sum()


# Missing values on 3 diff variables

# In[34]:


#check the duplicates
print("Total of duplicates: ",order_data_df.duplicated().sum())


# #### Assessing Seller Data

# In[35]:


#using the info function to know the structure of the data frame
seller_data_df.info()


# In[36]:


seller_data_df.info()


# In[37]:


#check the duplicates
print("Total of duplicates: ",seller_data_df.duplicated().sum())


# In[38]:


#check the summary statistics for the numerical column
seller_data_df.describe()


# ### Cleaning Data

# #### Cleaning Customer Data
# For clening this data, I prefer to drop the zip columns, since the same state could have a different zip code

# In[39]:


#removing the zip code and city columns
#axis 1 refers to column
#inplace means that the changed will go directly to the orginal table
customers_df.drop(["customer_zip_code_prefix"],axis=1,inplace=True)


# In[40]:


customers_df.head()


# Try to make the values of the city looks neat. So, I want to make it with capital each word format

# In[41]:


customers_df["customer_city"] = customers_df["customer_city"].str.title()


# In[42]:


customers_df.head()


# #### Cleaning Geolocation Data
# For this data, I prefer to only keep the city name and its code, it could make me easire to proceed the data with other table. Another reason is because one city could have many zipcode.

# In[43]:


geos_df.drop(["geolocation_zip_code_prefix","geolocation_lat","geolocation_lng"],axis=1,inplace=True)


# In[44]:


#take the disctinct data of the city to reduce duplication
#assigning the aggregation result in aggregate data variable
aggregate_data = geos_df.groupby(by="geolocation_state").agg({
    "geolocation_city":"first"
},inplace=True)

#assigning it back
geos_df = aggregate_data


# In[45]:


#make each first letter start with uppercase 
geos_df['geolocation_city']= geos_df['geolocation_city'].apply(lambda x: x.title())

#renaming the coloumn state to code
geos_df.rename({"geolocation_state": "geolocation_code"},axis = 1, inplace = True)


# In[46]:


#check the duplicates
print("Total of duplicates: ",geos_df.duplicated().sum())


# Since there is one more duplication, I choose to drop it

# In[47]:


#drop the rows and only keep the last duplicate
geos_df.drop_duplicates(keep='last',inplace=True)


# In[48]:


#recheck the duplicates
print("Total of duplicates: ",geos_df.duplicated().sum())


# #### Cleaning Order Items Table
# For this data, I will handle the dataype and renaming a column

# In[49]:


#handling a datatype
order_items_df['shipping_limit_date'] = pd.to_datetime(order_items_df['shipping_limit_date'])


# In[50]:


order_items_df.head(1)


# In[51]:


#for float datatype only accept one number after comma
order_items_df["price"]= order_items_df["price"].apply(lambda x: round(x, 1))
order_items_df["freight_value"]= order_items_df["freight_value"].apply(lambda x: round(x, 1))


# As I can see in the order_item_id, it still has an ambigus meaning. If that;s suppose to be an id as in primary key, there is no distinct. So , I will change the name of it to quantity.

# In[52]:


order_items_df.rename({'order_item_id' : "product_quantity"},axis=1, inplace=True)


# #### Cleaning Order Reviews Table
# As for the review title and message have a lot of missing value, I choose to drop it, only using the score already could help me. 

# In[53]:


order_reviews_df.drop(["review_comment_title","review_comment_message","review_answer_timestamp"],axis=1,inplace=True)


# In[54]:


order_reviews_df.head()


# The missing values come from a datetime series so I use interpolation to find a value that I will use in my imputation method.

# In[55]:


#handling the datatype
order_reviews_df['review_creation_date'] = pd.to_datetime(order_reviews_df['review_creation_date'])

#handling the missing value using the linear interpolation
order_reviews_df['review_creation_date']= order_reviews_df['review_creation_date'].interpolate(method='linear')


# In[56]:


#rearrange the column position
order_reviews_df = order_reviews_df[['review_id', 'order_id', 'review_creation_date', 'review_score']]


# In[57]:


order_reviews_df.head()


# #### Cleaning Order Data
# The issues of this data are the datatype for its datetime variable, so I will change it.

# In[58]:


#handling the datatype
order_data_df['order_approved_at']             = pd.to_datetime(order_data_df['order_approved_at'])
order_data_df['order_purchase_timestamp']      = pd.to_datetime(order_data_df['order_purchase_timestamp'])
order_data_df['order_delivered_carrier_date']  = pd.to_datetime(order_data_df['order_delivered_carrier_date'])
order_data_df['order_delivered_customer_date'] = pd.to_datetime(order_data_df['order_delivered_customer_date'])
order_data_df['order_estimated_delivery_date'] = pd.to_datetime(order_data_df['order_estimated_delivery_date'])


# For this data, I will only picked the status order of delivered

# In[59]:


#handling the missing value
order_data_df = order_data_df[order_data_df['order_status'] == 'delivered']

order_data_df.head()


# In[60]:


#handling the missing value using the linear interpolation
order_data_df['order_approved_at']              = order_data_df['order_approved_at'].interpolate(method='linear')
order_data_df['order_delivered_carrier_date']   = order_data_df['order_delivered_carrier_date'].interpolate(method='linear')
order_data_df['order_delivered_customer_date']  = order_data_df['order_delivered_customer_date'].interpolate(method='linear')


# In[61]:


order_data_df.isna().sum()


# #### Cleaning Seller Data
# Not many cleaning process I will do in this data, more then to make it looks neat, like applying capital each word in its city name

# In[62]:


#make each first letter start with uppercase 
seller_data_df['seller_city']= seller_data_df['seller_city'].apply(lambda x: x.title())


# In[63]:


#renaming the coloumn state to code
seller_data_df.rename({"seller_state": "seller_city_code"},axis = 1, inplace = True)


# In[64]:


seller_data_df.head()


# #### Cleaning Product Data
# For the the product category, I use the imputation method to fill in the missing values. Simply by using the most fruquent value that appears in in product category.

# In[65]:


#counting the most frequent name that appears
products_data_df.product_category_name.value_counts()


# In[66]:


#fill in the missing category name with the most frequent data
products_data_df['product_category_name'].fillna(value="cama_mesa_banho ", inplace=True)


# For the numerical column, I choose to fill in the data with the median value. Before that, I want to round up all the value so that will only 1 number after comma.

# In[67]:


products_data_df['product_name_lenght'] = products_data_df['product_name_lenght'].apply(lambda x: round(x, 1))
products_data_df['product_description_lenght'] = products_data_df['product_description_lenght'].apply(lambda x: round(x, 1))
products_data_df['product_weight_g'] = products_data_df['product_weight_g'].apply(lambda x: round(x, 1))
products_data_df['product_length_cm'] = products_data_df['product_length_cm'].apply(lambda x: round(x, 1))
products_data_df['product_width_cm'] = products_data_df['product_width_cm'].apply(lambda x: round(x, 1))
products_data_df['product_height_cm'] = products_data_df['product_height_cm'].apply(lambda x: round(x, 1))


# Finding the median of each value using this code:
# median_value = customers_df['column_name'].median()

# In[68]:


nl_median = products_data_df['product_name_lenght'].median()
dl_median = products_data_df['product_description_lenght'].median()
pq_median = products_data_df['product_photos_qty'].median()
pw_median = products_data_df['product_weight_g'].median()
pl_median = products_data_df['product_length_cm'].median()
pw_median = products_data_df['product_width_cm'].median()
ph_median = products_data_df['product_height_cm'].median()


# Fill in the missing value for each column using the median result

# In[69]:


products_data_df['product_name_lenght'].fillna(nl_median, inplace=True)
products_data_df['product_description_lenght'].fillna(dl_median, inplace=True)
products_data_df['product_photos_qty'].fillna(pq_median, inplace=True)
products_data_df['product_weight_g'].fillna(pw_median, inplace=True)
products_data_df['product_length_cm'].fillna(pl_median, inplace=True)
products_data_df['product_width_cm'].fillna(pw_median, inplace=True)
products_data_df['product_height_cm'].fillna(ph_median, inplace=True)


# For the photos quantity, I change the datatype from float to integer

# In[70]:


products_data_df['product_photos_qty'] = products_data_df['product_photos_qty'].astype(int)


# Merge the english products_eng_df with the products_data

# In[71]:


products_df = pd.merge(products_data_df, products_eng_df,on="product_category_name",how="left")


# In[72]:


#replacing the underscore with space
products_df['product_category_name'] = products_df['product_category_name'].str.replace("_"," ")
products_df['product_category_name_english'] = products_df['product_category_name_english'].str.replace("_"," ")

#capitalize each word using title
products_df['product_category_name'] = products_df['product_category_name'].str.title()
products_df['product_category_name_english'] = products_df['product_category_name_english'].str.title()


# In[73]:


products_df.head(1)


# In[74]:


#rearrage the colum position
products_df = products_df[['product_id','product_category_name','product_category_name_english','product_name_lenght','product_description_lenght','product_photos_qty','product_weight_g','product_length_cm','product_height_cm','product_width_cm']]


# In[75]:


products_df.head(1)


# ## Exploratory Data Analysis (EDA)

# ### Explore Order Review
# I want to categorize each of review given by the customer simply by this:
# - 5 being very good
# - 4 being good
# - 3 being average
# - 2 being poor
# - 1 being very poor

# In[76]:


#using the loc to give the reference of df and column I want to modify
# the : indicates to select all the rows
order_reviews_df.loc[:,"status"] = order_reviews_df["review_score"].apply(lambda x: "Very Good" if x == 5 else "Good" if x==4 else "Average" if x==3 else "Poor" if x==2 else "Very Poor")
order_reviews_df.sample(5)


# Using pivot table to display the total of review based on status

# In[77]:


order_reviews_df.groupby(by="status").review_id.count().sort_values(ascending=False)


# The majority of customer give a **very good** review

# #### Explore Customer Data and Geolocation Data
# From this exploration I would like to know where most of the customer lives

# In[78]:


#merge customers data and city
#merge customers data and the city
customers_city_df = pd.merge(
    left = customers_df,
    right = geos_df,
    how = "left",
    left_on = "customer_state",
    right_on = "geolocation_state"
)


# In[79]:


customers_city_df = customers_city_df[['customer_id','customer_unique_id','customer_state','geolocation_city']]
customers_city_df = customers_city_df.rename(columns={'geolocation_city': 'customer_city'})
customers_city_df.head()


# In[80]:


customers_city_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False)


# Sao Paulo holding the position as where the majority of customer comes from

# #### Explore Order Item Data

# In[81]:


order_items_df.loc[:,"total_price"] = order_items_df["product_quantity"]*order_items_df["price"]
order_items_df.head(1)


# Finding the most pricey order

# In[83]:


order_items_df.groupby(by="order_id").total_price.sum().sort_values(ascending=False)


# #### Explore The Order and Product Data

# In[84]:


product_ordered = pd.merge(
    left=order_items_df,
    right=products_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)

product_ordered.head()


# Find the maximum and minimum price for each product category

# In[85]:


product_ordered.groupby(by="product_category_name_english").agg({
    "product_quantity":["max","min","mean"],
    "total_price":["max","min","mean"],
    "freight_value":["max","min","mean"]
    
})


# We could know the maximum, minimum, and average value of the product quantity, total price, and fright value for each of the product's category

# #### Explore The Order Data

# In[86]:


order_data_df.head()


# Get to know the order status of each order

# In[87]:


order_data_df.groupby(by="order_status").order_id.count().sort_values(ascending=False)


# In[88]:


#dt.days is used to extract the numebr of days
order_data_df["delivery_duration"] = (order_data_df["order_delivered_customer_date"]-order_data_df["order_purchase_timestamp"]).dt.days


# In[89]:


order_data_df.head(1)


# #### Merge the order data with the customer data

# In[90]:


orders_customers = pd.merge(
    left=order_data_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)


# #### Merge the orders_customers data with the product_ordered

# In[91]:


all_df = pd.merge(
    left=product_ordered,
    right=orders_customers,
    how="left",
    left_on="order_id",
    right_on="order_id"
)

all_df.head()


# ## Visualization & Explanatory Analysis

# In[97]:


all_df.head()


# ### Question 1: Which state have the highest concentration of customers placing orders?

# In[98]:


#groupping the data
customer_geography = all_df.groupby(by="customer_city").order_id.nunique().reset_index()
customer_geography.rename({'order_id':'total_order'},axis=1,inplace=True)

customer_geography.head()


# In[99]:


#pick the top 5 
temp_sorted = customer_geography.sort_values(by="total_order",ascending=False)

#assigning the data
top_five = temp_sorted.head(5)
top_five.head()


# In[100]:


#creating data visualization
plt.figure(figsize=(10,5))

#data plotting
#sns.set_color_codes("pastel")

#creating the list of color
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x = "total_order",
    y = "customer_city",
    data = top_five,
    palette = colors
)

plt.title("Top 5 States with The Highest Number of Orders", loc="center",fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
plt.show


# ### Question 2: What is the product category with the highest number of orders? 

# In[101]:


all_df.head()


# In[102]:


#grouping the data
ordered_product = all_df.groupby(by="product_category_name_english").order_id.nunique().reset_index()

ordered_product.rename({"order_id":"total_order"},axis=1, inplace=True)
ordered_product.rename({"product_category_name_english":"product_category"},axis=1, inplace=True)

ordered_product.head()


# In[103]:


#sorting the data to only pick the five largest
#pick the top 5 
temp_sorted = ordered_product.sort_values(by="total_order",ascending=False)

#assigning the data
top_five = temp_sorted.head(5)
top_five.head()


# In[104]:


#creating data visualization
plt.figure(figsize=(10,5))

#data plotting
#sns.set_color_codes("pastel")

#creating the list of color
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    y = "total_order",
    x = "product_category",
    data = top_five,
    palette = colors
)

plt.title("Top 5 Most Sold Products", loc="center",fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=10)
plt.show


# ### Question 3: What was the month with the highest number of orders in 2017? Can we get the any insight from that data to use for this year (2018)?

# In[105]:


all_df.head()


# In[106]:


year_filter_2017 = all_df[(all_df['order_purchase_timestamp'] >= "2017-01-01") & (all_df['order_purchase_timestamp'] <= "2017-12-31")]


# In[107]:


#selecting the data using groupby

#resample is use to specify rhe frequency which M stand for Month
monthly_orders_2017 = year_filter_2017.resample(rule='M', on='order_purchase_timestamp').agg({
    "order_id":"nunique",
    "total_price":"sum"
})

#formatting the month name
#strftime is use to convert the obejct to a string representing the datetime
#index holds the labels or identifiers for the row, in this case autoamtically refers to the datetime value
monthly_orders_2017.index = monthly_orders_2017.index.strftime('%B')
monthly_orders_2017       = monthly_orders_2017.reset_index()  

#rename the column
monthly_orders_2017.rename({"order_purchase_timestamp":"month","order_id":"total_order","total_price":"total_revenue"}, 
                           axis=1, inplace = True)

monthly_orders_2017.tail()


# In[108]:


#filtering for 2018
year_filter_2018 = all_df[(all_df['order_purchase_timestamp'] >= "2018-01-01") & (all_df['order_purchase_timestamp'] <= "2018-09-30")]


# In[109]:


#selecting the data using groupby

#resample is use to specify rhe frequency which M stand for Month
monthly_orders_2018 = year_filter_2018.resample(rule='M', on='order_purchase_timestamp').agg({
    "order_id":"nunique",
    "total_price":"sum"
})

#formatting the month name
#strftime is use to convert the obejct to a string representing the datetime
#index holds the labels or identifiers for the row, in this case autoamtically refers to the datetime value
monthly_orders_2018.index = monthly_orders_2018.index.strftime('%B')
monthly_orders_2018       = monthly_orders_2018.reset_index()  

#rename the column
monthly_orders_2018.rename({"order_purchase_timestamp":"month","order_id":"total_order","total_price":"total_revenue"}, 
                           axis=1, inplace = True)

monthly_orders_2018.tail()


# In[110]:


#create a figure and two subplots
#1 row 2 columns
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,5))


#plotting the line chart
ax1.plot(monthly_orders_2017['month'], monthly_orders_2017['total_order'], marker='o',linestyle='-',linewidth=2, color='blue',label='2017')
ax1.set_title("Monthly Order in 2017")
ax1.set_xlabel("Months")
ax1.set_xticklabels(monthly_orders_2017['month'], rotation=45)
ax1.set_ylabel("Total of Order")

ax2.plot(monthly_orders_2018['month'], monthly_orders_2018['total_order'], marker='o',linestyle='-',linewidth=2, color='green',label='2018')
ax2.set_title("Monthly Order in 2018")
ax2.set_xlabel("Months")
ax2.set_xticklabels(monthly_orders_2017['month'], rotation=45)
ax2.set_ylabel("Total of Order")

#adjusting the layout
plt.subplots_adjust(bottom=0.4)  # Adjust the bottom margin to 0.4

plt.show()


# ### RFM Analysis

# In[111]:


all_df.info()


# In[112]:


#find the recent puchase from the order data
recent_date = order_data_df["order_purchase_timestamp"].dt.date.max()

#conver to time series
recent_date = pd.Timestamp(recent_date)


# In[113]:


rfm_df = all_df.groupby(by="customer_id").agg({
    #to find the recency
    "order_purchase_timestamp":lambda x: (recent_date - x.max()).days,
    
    #find the frequency
    "order_id": lambda x: len(x),
    
    #find the monetary
    "total_price": lambda x: x.sum()
})

rfm_df.rename({'order_purchase_timestamp':'recency','order_id':'frequency','total_price':'monetary'},axis=1,inplace=True)


# #### RFM Score
# To get the RFM Score, we scroed based on the quantiles of recency, monetary, and rececy dimension

# #### Determining the RFM Quantiles
# Dividing the quantiles to four
# - x<= 0.25
# - 0.25<x<=0.50
# - 0.50<x<=0.70
# - 0.70<x

# In[114]:


#calculating the quantiles for each numeric column
quantiles = rfm_df.quantile(q=[0.25,0.5,0.75])


# In[115]:


quantiles


# In[116]:


#using dictionary for further use
quantiles = quantiles.to_dict()
quantiles


# #### Creating the RFM Segmentation Table

# In[117]:


rfm_segmentation = rfm_df


# In[118]:


#dimension refers to the r,f,m
def rfm_class(value,key,quantiles):
    if value <= quantiles[key][0.25]:
        return 4
    elif value <= quantiles[key][0.50]:
        return 3
    elif value <= quantiles[key][0.75]:
        return 2
    else:
        return 1


# In[119]:


#applying the fucntion to each value in the recency column
rfm_segmentation['R_Quartile'] = rfm_segmentation['recency'].apply(rfm_class, args=('recency', quantiles))
rfm_segmentation['F_Quartile'] = rfm_segmentation['frequency'].apply(rfm_class,args=('frequency',quantiles,))
rfm_segmentation['M_Quartile'] = rfm_segmentation['monetary'].apply(rfm_class,args=('monetary',quantiles,))


# In[120]:


rfm_segmentation.head()


# The RFM Score is produced by connecting all the quartile result

# In[121]:


rfm_segmentation['RFMClass'] = rfm_segmentation['R_Quartile'].map(str)+\
rfm_segmentation['F_Quartile'].map(str)+\
rfm_segmentation['M_Quartile'].map(str)


# In[122]:


rfm_segmentation.head()


# In[123]:


plt.scatter(rfm_df['recency'],rfm_df['frequency'],
            color = 'red',
            marker = '*', alpha = 0.3
           )
plt.title('Scatter Plot for Recency and Frequency') 
plt.xlabel('Recency')
plt.ylabel('Frequency')
plt.show()


# The customer buys frequently when their recency is less.

# In[124]:


plt.scatter(rfm_df['frequency'],rfm_df['monetary'],
            color = 'red',
            marker = '*', alpha = 0.3
           )
plt.title('Scatter Plot for Frequency and Monetary') 
plt.xlabel('Recency')
plt.ylabel('Frequency')
plt.show()


# The customer who buy frequently are spending the less amount, the reason might a lot, one of those is everytime they palced an order, it is only for a cheap price product

# In[125]:


rfm_segmentation.info()


# #### Segmenting Customer Based on The RFM Scores

# In[126]:


segment = []

for row in rfm_segmentation['RFMClass']:
    #converting to string
    row = str(row)
    if int(row[0]) ==4 and int(row[1]) == 4 and int(row[2]) == 4:
        segment.append('Best Customer')
    elif int(row[0])==1 and int(row[2])==1:
        segment.append('Lost Cheap Customer')
    elif int(row[0])==1 and int(row[2])==4:
        segment.append('Lost Big Spend Customer')
    elif int(row[0])==2 and int(row[2])==4:
        segment.append('Almost Lost Big Spender')
    elif int(row[0])==2:
        segment.append('Almost Lost')
    elif int(row[1])==4:
        segment.append('Loyal')
    elif int(row[2])==4:
        segment.append('Big Spender')
    else:
        segment.append('Failed')


# In[127]:


rfm_segmentation['segment'] = segment
rfm_segmentation.head()


# In[128]:


rfm_segmentation.reset_index(inplace=True)


# In[129]:


#grouping the data
customer_segmentation= rfm_segmentation.groupby(by="segment").customer_id.nunique().reset_index()

customer_segmentation.rename({"customer_id":"total_customer"},axis=1, inplace=True)

customer_segmentation.head()


# In[130]:


temp_sorted = customer_segmentation.sort_values(by="total_customer",ascending=False)

#assigning the data
customer_segmentation = temp_sorted


# In[131]:


colors = ["firebrick","dimgrey","grey","darkgray","darkgrey","silver","lightgrey","gainsboro"]
plt.pie(customer_segmentation['total_customer'],colors = colors, startangle=270,autopct='%1.1f%%',pctdistance = 1.2)

#adding the legend
plt.legend(loc='upper right', bbox_to_anchor=(1.5, 1),labels=customer_segmentation['segment'])

plt.title("RFM Customer Segmentation", y=1.10)
#encusre that pie is drawn as a circle
plt.axis('equal')
plt.show()


# In[132]:


all_df.to_csv("all_data.csv", index=False)


# In[133]:


rfm_segmentation.to_csv("rfm_data.csv", index=False)


# ## Conclusion

# #### Conclusion 1
# 
# Based on the visualization, state with **highest** concentration of customers placing orders is **Sau Pauolo**. Here are the top fives:
# 
# 1. Sao Pauolo
# 2. Rio De Janeiro
# 3. Belo Horioznte
# 4. Brasilia
# 5. Cusitiba

# #### Conclusion 2
# 
# Based on the visualization, the most sold product category is **Bed Bath Table**, with the other top sold product are in this list below:
# 
# 1. Bed Bath Table
# 2. Health Beauty
# 3. Sports Leisure
# 4. Computer Accessories
# 5. Furniture Decor

# #### Conclusion 3
# 
# Based on the visualization,the month with the highest number of orders in 2017 is **November**. On the other hand, between 2017 and 2018 there is a significant pattern of the order placement. But, the majority of month in 2018 doing pretty well compare to 2017. A lot of factors might be affecting, starting the change of customer behaviour or even competitors.
# 
# Based on the 2017 pattern, we might expect a good result from September-December. 

# #### Conclusion 4
# 
# Based on the customer segmentation using the RFM analysis, **loyal customers** are in the first position. It indicates that they visit the website for many time which could tell us we have a good engagement to the customers. But, on the other hand, the almost lost customers are in the second position. Almost lost customers mean thos who have not visit the website for somtetime. At this point, the company could start to do the an improvement on engaging the customers.
