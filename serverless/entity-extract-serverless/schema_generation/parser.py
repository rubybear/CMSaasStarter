from pathlib import Path
from tempfile import TemporaryDirectory
from datamodel_code_generator import InputFileType, generate
from datamodel_code_generator import DataModelType
from pathlib import Path
import os

from pydantic import BaseModel, Field


def generate_pydantic_class_from_json(json_schema: str):
    output_directory = Path(__file__).resolve().parent
    output_filename = "model.py"
    output_path = output_directory / output_filename

    generate(
        json_schema,
        input_file_type=InputFileType.Yaml,
        input_filename="example.json",
        output=output_path,
        # set up the output model types
        output_model_type=DataModelType.PydanticV2BaseModel,
    )


json_schema: str = """{
    "type": "object",
    "properties": {
                  "test": {"type": "str"},
                  "current_grade": {"type": "str"},
                  "age": {"type": "str"},
                  "dob": {"type": "str"},
                  "emergency_contat": {
                    "name": {"type": "str"},
                    "relationship": {"type": "str"}
                  }
                  }
}"""

generate_pydantic_class_from_json(json_schema=json_schema)


class EmergencyContact(BaseModel):
    name: str = Field(description="Name of emergency contact")


class Sample(BaseModel):
    name: str = Field(description="student_name")
    grade: int = Field(description="student grade")
    emergency_contact: EmergencyContact


student = Sample(
    name="ruby", grade=12, emergency_contact=EmergencyContact(name="Morgan")
)

generate_pydantic_class_from_json(
    json_schema="""
student_form:
    name: name of student
    description: student name
    grade:
    emergency_contact:
        name: emergency contact name
"""
)
