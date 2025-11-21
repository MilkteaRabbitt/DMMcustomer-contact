
import os
import sys
from dotenv import load_dotenv
import logging

# Configure logging to stdout
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

load_dotenv()

logger.info("Starting detailed connection test...")

try:
    import openai
    from langchain_openai import ChatOpenAI
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY is not set in environment variables.")
        sys.exit(1)
    
    logger.info(f"OPENAI_API_KEY found (starts with: {api_key[:5]}...)")
    
    logger.info("Initializing ChatOpenAI...")
    llm = ChatOpenAI(
        model_name="gpt-4o-mini", 
        temperature=0.5,
        request_timeout=60,
        max_retries=2
    )
    
    logger.info("Attempting to invoke LLM (simple greeting)...")
    result = llm.invoke("Hello")
    logger.info("Success! LLM Response:")
    logger.info(result.content)

except Exception as e:
    logger.error("An error occurred during the test:")
    logger.error(e)
    import traceback
    traceback.print_exc()
