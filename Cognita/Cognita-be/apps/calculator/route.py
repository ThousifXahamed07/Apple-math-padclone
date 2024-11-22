from fastapi import APIRouter, HTTPException
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('/')
async def run(data: ImageData):
    # Decode base64 image data safely
    try:
        if "," in data.image:
            # Handles both cases (with or without the prefix)
            image_data = base64.b64decode(data.image.split(",")[1])
        else:
            image_data = base64.b64decode(data.image)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image data: {e}")
    
    # Convert bytes to a PIL image
    try:
        image_bytes = BytesIO(image_data)
        image = Image.open(image_bytes)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error opening image: {e}")
    
    # Analyze the image using your custom function
    try:
        responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
        if not responses:
            return {"message": "No data found in image", "data": [], "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image analysis failed: {e}")

    print('response in route:', responses)

    return {"message": "Image processed", "data": responses, "status": "success"}
