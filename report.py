from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step
 
from ipyvizzustory import Story  # or
 
# from ipyvizzustory.env.st.story import Story
 
 
# create data and initialize Story with the created data
 
data = Data()
data.add_series("Foo", ["Alice", "Bob", "Ted"])
data.add_series("Bar", [15, 32, 12])
data.add_series("Baz", [5, 3, 2])
 
# you can also add data with pandas
 
# import pandas as pd
#
# data = Data()
# df = pd.read_csv(
#     "https://ipyvizzu-story.vizzuhq.com/0.7/assets/data/data.csv"
# )
# data.add_data_frame(df)
 
story = Story(data=data)
 
 
# create Slides and Steps and add them to the Story
 
slide1 = Slide(
    Step(
        Config({"x": "Foo", "y": "Bar"}),
    )
)
story.add_slide(slide1)
 
slide2 = Slide(
    Step(Config({"color": "Foo", "x": "Baz", "geometry": "circle"}))
)
story.add_slide(slide2)
 
 
# note: in Streamlit,
# you need to set the width and height in pixels as int
 
story.set_size(width=800, height=480)
 
 
# you can export the Story into a html file
 
story.export_to_html(filename="mystory.html")
 
# or you can get the html Story as a string
 
html = story.to_html()
print(html)
 
 
# you can display the Story with the `play` method
 
story.play()
