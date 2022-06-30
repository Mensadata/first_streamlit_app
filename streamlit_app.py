import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner!')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣🥣Omega 3 & Blue Berry Oatmeal')
streamlit.text('🥬Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard Boiled free range egg')
streamlit.header('🍎🍊Build your own fruite smoothie🥭🍓')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
