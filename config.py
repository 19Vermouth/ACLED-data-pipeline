import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class ACLEDConfig:
    api_key: str
    email: str

    @classmethod
    def from_env(cls):
        api_key = os.getenv("ACLED_API_KEY")
        email = os.getenv("EMAIL")
        if not api_key or not email:
            raise ValueError("Missing ACLED_API_KEY or EMAIL in environment variables")
        return cls(api_key=api_key, email=email)