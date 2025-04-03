import re

def format_date(date):
    return date.strftime("%Y-%m-%d")

def validate_evaluation_data(data):
    required_fields = ['id_joueur', 'evaluation_date', 'moyenne_tactique', 'moyenne_comportementale', 'moyenne_technique']
    for field in required_fields:
        if field not in data or data[field] is None:
            return False, f"Missing required field: {field}"
    return True, ""

def calculate_average_evaluations(evaluations):
    if not evaluations:
        return {}
    
    averages = {}
    for key in evaluations[0].keys():
        if key.startswith('moyenne_'):
            averages[key] = sum(eval[key] for eval in evaluations) / len(evaluations)
    
    return averages

def format_evaluation_details(evaluation):
    return {
        "Date": format_date(evaluation['evaluation_date']),
        "Tactique": evaluation['moyenne_tactique'],
        "Comportementale": evaluation['moyenne_comportementale'],
        "Technique": evaluation['moyenne_technique'],
        "Commentaires": evaluation.get('commentaires', 'N/A')
    }
 
def joueur_non_existant():
       """Joueur n'existe pas"""
       pass
   
   


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

