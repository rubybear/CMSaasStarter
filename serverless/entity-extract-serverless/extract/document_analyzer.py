import json
from textractor import Textractor
from textractor.data.constants import TextractFeatures
from textractor.data.text_linearization_config import TextLinearizationConfig
from textractor.entities.document import Document


def analyzeDocument() -> Document:
    image = "s3://textractdevdata/sampleform.png"
    extractor = Textractor(region_name="us-east-1")

    config = TextLinearizationConfig(
        selection_element_selected="[X]",
        selection_element_not_selected="[ ]",
        signature_token="[SIGNATURE]",
    )

    document: Document = extractor.analyze_document(
        file_source=image,
        features=[
            TextractFeatures.LAYOUT,
            TextractFeatures.SIGNATURES,
            TextractFeatures.FORMS,
            TextractFeatures.TABLES,
        ],
        save_image=True,
    )

    return document