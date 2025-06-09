from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel


class PromptTemplates(BaseModel):
    task: str

    class DataScientist:
        @classmethod
        def detailed_report(cls, task):
            return f"""
            You're an expert analyst. You make comprehensive reports after visiting many websites.
            Don't hesitate to search for many queries at once in a for loop.
            For each data point that you find, visit the source url to confirm numbers.
            {task}
            """

    class FoodPhotographer(BaseModel):
        @classmethod
        def generate_food_photo(cls, food_details):
            """
            Applications:
                - Restaurant menu visualization
                - Food brand marketing assets
                - Social media content production
                - Product launch materials
                - Digital advertising campaigns

                Technical specifications embedded in prompt:
                - Macro photography simulation
                - Dynamic motion capture
                - Depth of field control
                - Professional lighting presets
                - Commercial photography standards

            :param food_details:
            :return: str
            """

            return f""""
            A cinematic macro shot of [number of food items, e.g., 4–7] 
            [describe the main food item, e.g., Indian samosas, sushi rolls, burgers], 
            with [describe toppings, fillings, or unique features, e.g., grilled unagi, 
            creamy Philadelphia cheese, fresh cilantro, or tangy tomato chutney] — frozen mid-air in dynamic, 
            asymmetric motion. Each [food item] is [describe coating or toppings, e.g., dusted with sesame seeds, 
            brushed with golden ghee, topped with sweet sauce], with [additional descriptive details, e.g., glistening 
            sauce dripping, steam rising, crisp exterior catching the light]. Surrounding the [food items] are 
            [list atmospheric or complementary elements, e.g., scattered sesame seeds, flying bits of herbs, wisps of 
            steam, or scattered microgreens]. Shot with dramatic depth of field — one [food item] in razor-sharp focus,
             the others fading into a soft blur, creating an immersive floating effect. The background is dark with a 
             subtle gradient and cinematic bokeh, emphasizing the texture and motion of the [food items]. 
            Professional food photography lighting, hyper-realistic, intense shadows, luxury ad style. 4:5 format.
            
            """

    def get_detailed_report(self):
        return self.DataScientist.detailed_report(self.task)
