from dataclasses import dataclass
from typing import Optional
import pandas as pd

@dataclass
class ACLEDResponse:
    success: bool
    data: Optional[pd.DataFrame] = None
    error: Optional[str] = None
    count: Optional[int] = None

    @classmethod
    def from_api_response(cls, json_response: dict) -> 'ACLEDResponse':
        if 'success' in json_response and not json_response['success']:
            return cls(
                success=False,
                error=json_response.get('error', 'Unknown error'),
                count=json_response.get('count', None)
            )
        data = json_response.get('data', []) if isinstance(json_response, dict) else json_response
        df = pd.DataFrame(data) if data else pd.DataFrame()
        return cls(
            success=True,
            data=df,
            count=len(df),
            error=None
        )