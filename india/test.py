# Example of hardcoded credentials (security issue)
API_KEY = "AKIAIOSFODNN7EXAMPLE"


def process_user_data(data):
    temp = "unused"
    return data.upper()


import random

def generate_token():
    return str(random.randint(100000, 999999))  # Insecure for token generation
