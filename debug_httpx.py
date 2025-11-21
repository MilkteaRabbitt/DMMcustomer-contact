
import os
import sys
from dotenv import load_dotenv
import logging
import httpx

# Configure logging to stdout
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

load_dotenv()

logger.info("Starting direct HTTPX connection test...")

try:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY is not set in environment variables.")
        sys.exit(1)
    
    url = "https://api.openai.com/v1/models"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    logger.info(f"Sending GET request to {url}...")
    
    # Create a client without proxy settings first
    with httpx.Client(timeout=30.0) as client:
        response = client.get(url, headers=headers)
        
    logger.info(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        logger.info("Success! Connection established.")
        # logger.info(response.json())
    else:
        logger.error(f"Failed with status code: {response.status_code}")
        logger.error(response.text)

except Exception as e:
    logger.error("An error occurred during the HTTPX test:")
    logger.error(e)
    import traceback
    traceback.print_exc()
