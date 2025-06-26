import requests
from models import ACLEDResponse
from config import ACLEDConfig

class ACLEDExtractor:
    def __init__(self, config: ACLEDConfig):
        self.config = config
        self.base_url = "https://api.acleddata.com/acled/read"

    def extract_data(self, country: str = "India", start: str = "2023-01-01", end: str = "2023-12-31", limit: int = 500) -> ACLEDResponse:
        print("🔄 Extracting data from ACLED API...")
        params = {
            'email': self.config.email,
            'key': self.config.api_key,
            'country': country,
            'event_date': start,
            'event_date_to': end,
            'limit': limit,
            'format': 'json'
        }

        print(f"Making request with email: {self.config.email[:3]}***@{self.config.email.split('@')[1] if '@' in self.config.email else 'unknown'}")
        print(f"API Key length: {len(self.config.api_key)} characters")

        try:
            response = requests.get(self.base_url, params=params)
            print(f"API Response Status: {response.status_code}")
            json_response = response.json()
            print(f"API Response Keys: {list(json_response.keys())}")
            return ACLEDResponse.from_api_response(json_response)
        except requests.RequestException as e:
            print(f"❌ Error making API request: {e}")
            return ACLEDResponse(success=False, error=str(e))
        except ValueError as e:
            print(f"❌ Error parsing JSON response: {e}")
            print(f"Raw response (first 500 chars): {response.text[:500]}...")
            return ACLEDResponse(success=False, error=str(e))
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return ACLEDResponse(success=False, error=str(e))

    def test_api_connection(self) -> ACLEDResponse:
        print("🧪 Testing API connection...")
        params = {
            'email': self.config.email,
            'key': self.config.api_key,
            'limit': 1,
            'format': 'json'
        }

        try:
            response = requests.get(self.base_url, params=params)
            print(f"Test Response Status: {response.status_code}")
            json_response = response.json()
            response_obj = ACLEDResponse.from_api_response(json_response)
            if response_obj.success:
                print("✅ API connection successful!")
                print(f"Available data count: {response_obj.count or 'Unknown'}")
            else:
                print("❌ API connection failed:")
                print(f"Error: {response_obj.error}")
            return response_obj
        except Exception as e:
            print(f"❌ Test failed: {e}")
            return ACLEDResponse(success=False, error=str(e))