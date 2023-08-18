from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step
 
from ipyvizzustory import Story  # or
 
# from ipyvizzustory.env.st.story import Story
 
# you can also add data with pandas
 
import pandas as pd

data = Data()
df = pd.read_csv(
    "ultra_dataset.csv"
)
data.add_data_frame(df[:500])
 
story = Story(data=data)
 

# Slide 1: Introduction
slide1 = Slide(Step(
    Config({"title": "Exploring Food Delivery Insights"}),
))
story.add_slide(slide1)


# # create Slides and Steps and add them to the Story
 

 
# Slide 2: Restaurant Ratings and Delivery Ratings
slide2 = Slide(
    Step(
        Config(
            {
                "channels": {
                    "y": {
                        "set": ["Restaurant Name"],
                    },
                    "x": {"set": ["Dining Rating", "Delivery Rating"]},
                    "color": "Delivery Rating",
                },
                "title": "Ratings Overview",
            }
        ),
    )
)
# Add the slide to the story
story.add_slide(slide2)

slide3 = Slide(
    Step(
        Config({"x": "Cuisine ", "y": "Prices",
               "title": "Delivery Ratings",},
              ),
        
    )
)
story.add_slide(slide3)
 
slide4 = Slide(
    Step(Config({"color": "Cuisine ", "x": "Dining Votes", "geometry": "circle",
                "title": "Dining Ratings",},
               ),
        )
)
story.add_slide(slide4)




# Group the data by dish name and sum up the quantities ordered
best_selling_dishes = data.groupby('Item Name')['Votes'].sum().reset_index()

# Sort the dishes in descending order based on quantities sold
best_selling_dishes = best_selling_dishes.sort_values(by='Votes', ascending=False)

# Select the top 10 best-selling dishes
top_n = 10
top_dishes = best_selling_dishes.head(top_n)
# Create a slide
slide4 = Slide(
    Step(
        Data.filter(
            f"""
            {' || '.join([f"record['Item Name'] === '{dish}'" for dish in top_dishes['Item Name']])}
            """
        ),
        Config(
            {
                "title": "Top {} Best-Selling Dishes".format(top_n),
                # Configure other visualization settings here
            }
        ),
    )
)

# Add the slide to the story
story.add_slide(slide4)




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
