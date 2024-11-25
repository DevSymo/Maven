import requests
import time
from typing import Dict, Any

def QueryTicker(query: str, lang: str = "en-AU", region: str = "AU", max_retries: int = 5, timeout: int = 30) -> Dict[str, Any]:
    """
    Query Yahoo Finance for a given search term, handling 429 responses by retrying with a timeout.

    Args:
        query (str): The search query term.
        lang (str): The language code (default: "en-AU").
        region (str): The region code (default: "AU").
        max_retries (int): Maximum number of retry attempts (default: 5).
        timeout (int): Timeout duration for requests in seconds (default: 30).

    Returns:
        dict: JSON response from Yahoo Finance if successful.

    Raises:
        Exception: If the maximum number of retries is exceeded or other errors occur.
    """
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {"q": query, "lang": lang, "region": region}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=timeout)
            
            # Check for success
            if response.status_code == 200:
                if (response.json())["count"] < 1:
                    raise Exception(f"No results found for ticker query.")
                else:
                    return response.json()
            
            # Handle 429 Too Many Requests
            if response.status_code == 429:
                print(f"429 Too Many Requests - Retry {attempt}/{max_retries}")
                retry_after = int(response.headers.get("Retry-After", 2))  # Default retry delay if not specified
                time.sleep(retry_after)
                continue

            # Handle other non-200 responses
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"Error on attempt {attempt}/{max_retries}: {e}")
            time.sleep(2 ** attempt)  # Exponential backoff for other errors

    raise Exception(f"Failed to fetch data after {max_retries} retries.")

def is_not_null_or_whitespace(value):
    return value is not None and value.strip() != ""
