import pandas as pd
import streamlit as st
# from streamlit_vizzu import Config, Data, VizzuChart
from streamlit.components.v1 import html
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget

# # Load the Zomato dataset
# df = pd.read_csv("zomato_dataset.csv")

# # Create a VizzuChart object
# chart = Chart()

# # Add the dataset to the chart
# data = Data()
# data.add_data_frame(df)
# chart.animate(data)

# # Configure the chart
# chart.animate(Config({"x": "Cuisine", "y": "Votes", "title": "Cuisine Popularity"}))

# # Add the swap checkbox
# if st.checkbox("Swap"):
#     chart.animate(Config({"y": "Cuisine", "x": "Votes", "title": "Votes Distribution"}))

# # # Show the chart in the app
# # chart.show()
# # display Chart
 
# html(chart, width=650, height=370)

# import streamlit, pandas and ipyvizzu
#####################################################################################
# from streamlit.components.v1 import html
# import pandas as pd
# from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
 
 
# def create_chart():
#     # initialize Chart
 
#     chart = Chart(
#         width="640px", height="360px", display=DisplayTarget.MANUAL
#     )
 
#     # create and add data to Chart
 
#     data = Data()
#     data_frame = pd.read_csv(
#         "https://ipyvizzu.vizzuhq.com/0.15/showcases/titanic/titanic.csv"
#     )
#     data.add_data_frame(data_frame)
 
#     chart.animate(data)
 
#     # add config to Chart
 
#     chart.animate(
#         Config(
#             {
#                 "x": "Count",
#                 "y": "Sex",
#                 "label": "Count",
#                 "title": "Passengers of the Titanic",
#             }
#         )
#     )
#     chart.animate(
#         Config(
#             {
#                 "x": ["Count", "Survived"],
#                 "label": ["Count", "Survived"],
#                 "color": "Survived",
#             }
#         )
#     )
#     chart.animate(Config({"x": "Count", "y": ["Sex", "Survived"]}))
 
#     # add style to Chart
 
#     chart.animate(Style({"title": {"fontSize": 35}}))
 
#     # return generated html code
 
#     return chart._repr_html_()
 
 
# # generate Chart's html code
 
# CHART = create_chart()
#########################################################

from ipyvizzu import Data, Config

from ipyvizzustory import Story, Slide, Step

	 

	 

# Create data object

data = Data()

data.add_series("Foo", ["Alice", "Bob", "Ted"])

data.add_series("Bar", [15, 32, 12])

data.add_series("Baz", [5, 3, 2])

	 

	 

# Create story object, add data to it

story = Story(data=data)

	 

	 

# Each slide here is a page in the final interactive story

# Add the first slide

slide1 = Slide(

	Step(

	Config({"x": "Foo", "y": "Bar"}),

	    )

	)

	# Add the slide to the story

story.add_slide(slide1)

	 

# Create the second slide

# Configs provided here are changes to the visualization

# created in the previous Step

slide2 = Slide(

	    Step(

	        Config({"color": "Foo", "x": "Baz", "geometry": "circle"}),

	    )

	)

story.add_slide(slide2)

	 

	 
# Play the created story!

story.play()

# # display Chart
 
# html(CHART, width=650, height=370)
