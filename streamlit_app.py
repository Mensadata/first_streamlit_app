import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner!')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣🥣Omega 3 & Blue Berry Oatmeal')
streamlit.text('🥬Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard Boiled free range egg')
streamlit.header('🍎🍊Build your own fruite smoothie🥭🍓')

#read the csv data into pandas dataframe
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
