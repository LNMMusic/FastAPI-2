# LIBRARIES
from dotenv import load_dotenv
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, 'sample.env'))
sys.path.append(BASE_DIR)

# Fetcher
def Env(variable:str) -> str:
    try:
        return os.environ[variable]
    except KeyError:
        return ""