"""Function to Generate invitations"""
import os

def generate_invitations(template:str, attendees:list):
    """Create an invitstion based on the template an filling in the information with the list"""
    
    try:
        if template is None:
            raise ValueError("Template cannot be empty")
        if type(template) is not str:
            raise TypeError("Template must be a string")
        if type(attendees) is not list:
            raise TypeError("Attendees must be a list")
        for attendee in attendees:
            if type(attendee) is not dict:
                raise TypeError("Attendees must be a list of dictionaries")
            fixed_attendee = {key: (value if value is not None else "N/A") for key, value in attendee.items()}
            x = attendees.index(attendee) + 1
            with open(f"output_{x}.txt", "w") as file:
                file.write(template.format(**fixed_attendee))
    except TypeError as e:
        print(f"Error: {str(e)}")