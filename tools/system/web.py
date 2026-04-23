import requests
from bs4 import BeautifulSoup

def search_web(query):
    """
    Simple DuckDuckGo search (via HTML scraping or a better API in production).
    For now, this is a placeholder or uses a simple request.
    """
    # Note: DuckDuckGo scraping might be blocked. In production, use an API.
    # We'll use a simplified version for this project.
    return f"Searching for: {query}... (Simulated result for now)"

def scrape_url(url):
    """
    Scrapes the text content of a URL.
    """
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        return soup.get_text(separator=' ', strip=True)
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

def summarize_url(url):
    """
    Scrapes a URL and returns content for the agent to summarize.
    """
    content = scrape_url(url)
    if "Error" in content:
        return content
    return f"CONTENT_TO_SUMMARIZE: {content[:2000]}" # Limit size for LLM context

def download_file(url, save_path):
    """
    Downloads a file from a URL.
    """
    save_path = os.path.expanduser(save_path)
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return f"Success: Downloaded to {save_path}"
    except Exception as e:
        return f"Error downloading {url}: {str(e)}"
