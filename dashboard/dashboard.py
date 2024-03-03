import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

st.header('E-commerce Dashboard :sparkles:')

#read_data
all_data = pd.read_csv("https://raw.githubusercontent.com/calistaas/Ecommerce-Data-Analysis/main/dashboard/all_data.csv")
rfm_data = pd.read_csv("https://raw.githubusercontent.com/calistaas/Ecommerce-Data-Analysis/main/dashboard/rfm_data.csv")

#change to datetime datatype
all_data['order_purchase_timestamp']=pd.to_datetime(all_data['order_purchase_timestamp'])

#making the filter
min_date = all_data['order_purchase_timestamp'].min()
max_date = all_data['order_purchase_timestamp'].max()
#making sidebar
with st.sidebar:
#adding logo
    st.image("https://github.com/dataprofessor/dashboard/blob/43b0c1cf6f7a231abb7a09b502af1daead4015c9/streamlit-logo-secondary-colormark-darktext.png?raw=true")

    start_date, end_date = st.date_input(
        label = "Daily Order Filter", min_value = min_date,
        max_value = max_date,
        value=[min_date, max_date]
    )
main_df = all_data[(all_data["order_purchase_timestamp"] >= str(start_date)) & (all_data["order_purchase_timestamp"] <= str(end_date))]

def cust_state(df):
    customer_geography = df.groupby(by="customer_city").order_id.nunique().reset_index()
    customer_geography.rename({'order_id': 'total_order'}, axis=1, inplace=True)
    temp_sorted = customer_geography.sort_values(by="total_order", ascending=False)
    top_five = temp_sorted.head(5)
    return  top_five

#find the daily order
def daily_orders(df):
    daily_order_df = df.resample(rule='D', on='order_purchase_timestamp').agg({
        "order_id":"nunique",
        "total_price":"sum"
    })
    daily_order_df = daily_order_df.reset_index()
    daily_order_df.rename({"order_purchase_timestamp":"day","order_id":"total_order","total_price":"total_revenue"},axis=1,inplace=True)
    return daily_order_df

def customer_segmentation(df):
    customer_segmentation = df.groupby(by="segment").customer_id.nunique().reset_index()
    customer_segmentation.rename({"customer_id": "total_customer"}, axis=1, inplace=True)
    temp_sorted = customer_segmentation.sort_values(by="total_customer", ascending=False)
    customer_segmentation = temp_sorted
    return customer_segmentation

#daily order data
daily_order_df = daily_orders(main_df)
#customer base on their demography
cust_top_geo = cust_state(main_df)
#customer segmentation
customer_segmentation_res = customer_segmentation(rfm_data)

#columns
col1,col2 = st.columns(2)
with col1:
    total_order = daily_order_df['total_order'].sum()
    st.metric("Total Order", value = total_order)

with col2:
    total_revenue = format_currency(daily_order_df.total_revenue.sum(),"$",locale='es_CO')
    st.metric("Total Revenue", value=total_revenue)


#for daily order
st.subheader("Daily Order")
#create the bar
fig,ax= plt.subplots(figsize=(16,8))
ax.plot(
    daily_order_df['day'],
    daily_order_df['total_order'],
    marker = 'o',
    linewidth=2,
    color = "#72BCD4"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

#for state data
st.subheader('Top 5 States with The Highest Number of Orders')
fig, ax = plt.subplots(figsize=(20,10))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="total_order",
    y="customer_city",
    data=cust_top_geo,
    palette=colors
)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y',labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

#for segmentation data
st.subheader('Customer Segmentation')
fig,ax = plt.subplots(figsize=(20,10))
pie_colors = ["firebrick","dimgrey","grey","darkgray","darkgrey","silver","lightgrey","gainsboro"]
ax.pie(customer_segmentation_res['total_customer'],colors = pie_colors, startangle=270,autopct='%1.1f%%',pctdistance = 1.2)
ax.legend(loc='upper right', bbox_to_anchor=(1.5, 1),labels=customer_segmentation_res['segment'])
st.pyplot(fig)

#making the filter
min_date = all_data['order_purchase_timestamp'].min()
max_date = all_data['order_purchase_timestamp'].max()
