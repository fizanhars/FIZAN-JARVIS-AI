import requests


def fetch_url(url: str, timeout: int = 10) -> str:
    """Fetch text from a web page."""
    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": "FIZAN-JARVIS-AI/1.0"}
        )
        response.raise_for_status()
        return response.text
    except requests.RequestException as exc:
        return f"Web request failed: {exc}"


if __name__ == "__main__":
    print("JARVIS web module is ready.")
