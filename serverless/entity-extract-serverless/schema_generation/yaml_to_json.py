import yaml

valid_yaml = """
student_form:
    name: 
    grade: 
    emergency_contact:
        name: emergency contact name
"""

d = yaml.load(valid_yaml, yaml.CFullLoader)