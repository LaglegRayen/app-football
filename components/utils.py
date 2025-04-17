import re

   
def clean_string(input_string):
    # Define the substrings to remove
    substrings_to_remove = ["CA VS", "CA", "VS"]
    
    # Create a regex pattern to match any of the substrings
    pattern = r'\b(?:' + '|'.join(re.escape(sub) for sub in substrings_to_remove) + r')\b'
    
    # Replace the matched substrings with an empty string
    cleaned_string = re.sub(pattern, '', input_string)
    
    # Remove extra spaces caused by the replacements
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string).strip()
    
    return cleaned_string

import plotly.express as px

