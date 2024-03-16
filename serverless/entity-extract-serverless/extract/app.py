from document_analyzer import analyzeDocument
from event import Event, Body
from datamodel_code_generator import InputFileType, generate
from datamodel_code_generator import DataModelType

sample_event = Event(
    body=Body(
        file="someFile.png",
        schema_string="""
{
                  "student_name": "str",
                  "current_grade": "str",
                  "age": "str",
                  "dob": "str",
                  "emergency_contat": {
                    "name": "str",
                    "relationship": "str"
                  }
}
""",
    )
)

generate()

def lambda_handler(event, context):
    # TODO implement
    return {"statusCode": 200, "body": json.dumps(analyzeDocument().get_text())}
