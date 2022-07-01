import streamlit
import pandas
# to get call API's
import requests

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
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruit_to_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page.
streamlit.dataframe(fruit_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# take the json text from api and load to pandas to normaize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display the normalized data in dataframes
streamlit.dataframe(fruityvice_normalized)
