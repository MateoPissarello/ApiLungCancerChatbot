from fastapi import APIRouter, File, UploadFile
from fastapi import status as response_status
from services.LungCancerModel import LungCancerClassifier
from fastapi import HTTPException
from services.FileHandler import FileHandler
import os
from pprint import pprint
router = APIRouter(prefix="/model", tags=["Model"])
IMAGES_PATH = "images/"


@router.post("/classify", status_code=response_status.HTTP_201_CREATED)
async def classify_image(file: UploadFile = File(...)):
    """
    Classify an image and return the result.
    """
    lung_cancer_classifier = LungCancerClassifier()
    file_handler = FileHandler(bucket_name=os.getenv("IMAGES_BUCKET_NAME"))

    try:
        contents = await file.read()
        filename = f"{IMAGES_PATH}{file.filename}"
        content_type = file.content_type

        # Upload the file to S3
        s3_url = file_handler.upload_file(contents, filename, content_type)

        # Classify the image using the model
        result = lung_cancer_classifier.classify_image(s3_url)
        pprint(result)

        return {
            "message": "Image classified successfully",
            "result": result,
        }

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        raise HTTPException(
            status_code=response_status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the image: {str(e)}",
        )
