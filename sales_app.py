import streamlit as st
import pandas as pd

st.title("Sales Summary Dashboard")
st.subheader("Interactive dashboard to view sales by product category")

data = {
    'Product': ['Laptop', 'Wireless Mouse', 'Mechanical Keyboard', 'Office Chair', 'Standing Desk', 'Monitor'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Furniture', 'Furniture', 'Electronics'],
    'Sales': [1200, 45, 130, 250, 400, 300]
}
data_frame = pd.DataFrame(data)

st.sidebar.header("Filter Options")
categories = data_frame['Category'].unique()
selected_category = st.sidebar.selectbox("Select a Category:", categories)

filtered_frame = data_frame[data_framef['Category'] == selected_category]

st.write(f"### Data for {selected_category}")
st.dataframe(filtered_frame)

st.write("### Sales Chart")
chart_data = filtered_frame.set_index('Product')['Sales']
st.line_chart(chart_data)
