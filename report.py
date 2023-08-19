from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step
 
from ipyvizzustory import Story  # or
 
# from ipyvizzustory.env.st.story import Story
 



	import pandas as pd

	 

	from ipyvizzu import Data, Config, Style

	from ipyvizzustory import Story, Slide, Step

	 

	 

	# Create data object, read csv to data frame and add data frame to data object

	data = Data()

	df = pd.read_csv(

	    "https://ipyvizzu-story.vizzuhq.com/0.7/examples/trumptwitter/trumptwitter.csv",

	)

	data.add_data_frame(df)

	 

	 

	# Set the style of the charts in the story

	style = Style(

	    {

	        "tooltip": {"fontSize": "22px"},

	        "title": {"paddingTop": "1.2em", "fontSize": "2.5em"},

	        "legend": {"label": {"fontSize": "1.8em"}, "width": "16em"},

	        "logo": {"width": "6em"},

	        "plot": {

	            "marker": {"label": {"fontSize": "1.5em"}},

	            "yAxis": {

	                "label": {

	                    "fontSize": "1.5em",

	                },

	                "title": {"color": "#ffffff00"},

	                "interlacing": {"color": "#ffffff00"},

	            },

	            "xAxis": {

	                "label": {

	                    "fontSize": "1.6em",

	                    "paddingTop": "1em",

	                },

	                "title": {"fontSize": "1.4em", "paddingTop": "2.5em"},

	            },

	        },

	    }

	)

	 

	# Create story object, add data and style settings to it

	story = Story(data=data, style=style)

	 

	# Set the size of the HTML element

	# that appears within the notebook

	story.set_size("100%", "400px")

	 

	# Switch on the tooltip that appears

	# when the user hovers the mouse over a chart element

	story.set_feature("tooltip", True)

	 

	# Each slide here is a page in the final interactive story

	# Add the first slide

	slide1 = Slide(

	    Step(

	        Data.filter(

	            "record.Firsttweet === 'Yes' && record.Dummy === 'No'"

	        ),

	        Config(

	            {

	                "channels": {

	                    "y": {

	                        "set": ["tweets"],

	                    },

	                    "x": {"set": ["Period", "year", "month"]},

	                    "color": "Period",

	                },

	                "title": "Trump started tweeting in May '09",

	            }

	        ),

	    )

	)

	# Add the slide to the story

	story.add_slide(slide1)


	slide2 = Slide(

	    Step(

	        Data.filter(

	            "record.Period === 'New to Twitter' && record.Dummy === 'No'"

	        ),

	        Config(

	            {

	                "title": "In the first two years he wasn't very active",

	            }

	        ),

	    )

	)

	story.add_slide(slide2)

	 

	slide3 = Slide(

	    Step(

	        Data.filter(

	            """

	            (record.Period === 'New to Twitter' || record.Period === 'Businessman')

	            && record.Dummy === 'No'

	            """

	        ),

	        Config(

	            {

	                "title": "Then he got hooked on",

	            }

	        ),

	    )

	)

	story.add_slide(slide3)

	 

	slide4 = Slide(

	    Step(

	        Data.filter(

	            """

	            (record.Period === 'New to Twitter' || 

	            record.Period === 'Businessman' || 

	            record.Period === 'Nominee')

	            && record.Dummy === 'No'

	            """

	        ),

	        Config(

	            {

	                "title": "Interesting trend after becoming a presidential nominee",

	            }

	        ),

	    )

	)

	story.add_slide(slide4)

	 

	slide5 = Slide(

	    Step(

	        Data.filter("record.Dummy === 'No'"),

	        Config(

	            {

	                "title": "And after he became President",

	            }

	        ),

	    )

	)

	story.add_slide(slide5)

	 

	slide6 = Slide()

	slide6.add_step(

	    Step(

	        Config({"geometry": "area", "align": "center"}),

	    )

	)

	slide6.add_step(

	    Step(

	        Config(

	            {

	                "title": "All of Trump's tweets until May 2020",

	            }

	        ),

	    )

	)

	story.add_slide(slide6)

	 

	slide7 = Slide(

	    Step(

	        Config(

	            {

	                "y": "retweetcount",

	                "title": "And the number of times these were retweeted",

	            }

	        ),

	    )

	)

	story.add_slide(slide7)

	 
	 

	slide12 = Slide()

	slide12.add_step(

	    Step(

	        Config(

	            {

	                "align": "center",

	                "title": "",

	            }

	        ),

	    )

	)

	slide8.add_step(

	    Step(

	        Config({"y": "tweets", "color": None, "legend": "lightness"}),

	        Style(

	            {"plot": {"marker": {"colorPalette": "null"}}},

	        ),

	    )

	)

	slide8.add_step(

	    Step(

	        Config(

	            {

	                "y": ["tweets", "Tool"],

	                "color": "Tool",

	                "title": "Tools Trump Used to Tweet",

	                "legend": "color",

	            }

	        ),

	        Style(

	            {

	                "plot": {

	                    "marker": {

	                        "colorPalette": "#597696FF #ED2828FF #26EC87FF #29B9BFFF "

	                    }

	                }

	            },

	        ),

	    )

	)

	story.add_slide(slide8)

	 

	slide9 = Slide(

	    Step(

	        Config({"split": True, "align": "none"}),

	        Style({"plot": {"yAxis": {"label": {"color": "#ffffff00"}}}}),

	    )

	)

	story.add_slide(slide9)

	 

	slide10 = Slide()

	slide10.add_step(

	    Step(

	        Config(

	            {

	                "geometry": "rectangle",

	            }

	        ),

	    )

	)

	slide10.add_step(

	    Step(

	        Config(

	            {

	                "x": ["tweets", "year", "month"],

	                "y": "Tool",

	                "geometry": "rectangle",

	                "split": False,

	                "align": "none",

	            }

	        ),

	        Style(

	            {

	                "plot": {

	                    "xAxis": {"title": {"color": "#ffffff00"}},

	                    "yAxis": {"label": {"color": "#999999ff"}},

	                }

	            },

	        ),

	    )

	)

	slide10.add_step(

	    Step(

	        Config(

	            {

	                "x": "tweets",

	                "label": "tweets",

	            }

	        ),

	    )

	)

	story.add_slide(slide10)
	 

	# Play the created story!

	story.play()

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
