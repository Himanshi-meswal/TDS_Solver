import os
import tempfile
from fastapi import UploadFile

async def save_upload_file_temporarily(upload_file: UploadFile) -> str:
    """
    Save an uploaded file temporarily and return the path to the saved file.
    """
    try:
        # Extract file extension from the original filename
        _, ext = os.path.splitext(upload_file.filename)
        
        # Create a temporary file with the same extension.
        # delete=False ensures that the file persists after closing.
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            contents = await upload_file.read()
            tmp.write(contents)
            temp_file_path = tmp.name

        return temp_file_path
    except Exception as e:
        raise e