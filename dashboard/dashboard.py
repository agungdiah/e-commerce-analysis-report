# import library

import pandas as pd
import matplotlib as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style="dark")

all_df = pd.read_csv("/e-commerce-analysis-report/dashboard/main_data.csv")

# membuat header
st.header('Olist Store')

st.subheader("Demografi Sellers")
col1, col2 = st.columns(2)
with col1:
    total_seller = all_df.seller_id.nunique()
    st.metric("Total Seller", value=total_seller)

with col2:
# Plotting
    fig, ax = plt.subplots(figsize=(20, 10))
    
    bystate_seller = all_df.groupby(by="seller_state").seller_id.nunique().reset_index()
    bystate_seller.rename(columns={"seller_id": "seller_count"}, inplace=True)

    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        y="seller_count",
        x="seller_state",
        data=bystate_seller.sort_values(by="seller_count", ascending=False).head(),
        palette=colors,
        ax=ax
    )
    
    # Customize the plot
    ax.set_title("Number of Sellers by States", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='y', labelsize=30)
    ax.tick_params(axis='x', labelsize=30)

    # Show the Streamlit app
    st.pyplot(fig)


st.subheader("The Potensial Sellers")
 
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
 
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
bypayment_seller = all_df.groupby(by="seller_id").payment_value.sum().reset_index()
bypayment_seller.rename(columns={
    "payment_value": "Total Pendapatan Seller"
}, inplace=True)

# Plot pertama
sns.barplot(x="Total Pendapatan Seller", y="seller_id", data=bypayment_seller.sort_values(by="Total Pendapatan Seller", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_xlabel(None)
ax[0].set_ylabel(None)
ax[0].set_title("Best Performing Seller by Revenue", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=25)
ax[0].tick_params(axis='x', labelsize=25)



# Plot kedua
sns.barplot(x="Total Pendapatan Seller", y="seller_id", data=bypayment_seller.sort_values(by="Total Pendapatan Seller", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Seller by Revenue", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=25)
ax[1].tick_params(axis='x', labelsize=25)

st.pyplot(fig)






