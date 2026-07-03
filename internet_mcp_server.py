import requests
from bs4 import BeautifulSoup
from fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS

mcp = FastMCP("Internet Fetch Server")

@mcp.tool()
def fetch(url: str) -> str:
    """
    Fetches the content of a webpage and returns the text.
    """
    try:
        if not url.startswith("http"):
            url = "https://" + url

        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            raise McpError(
                ErrorData(
                    code=INTERNAL_ERROR,
                    message=f"Server returned status: {response.status_code}"
                )
            )
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
            
        text = soup.get_text(separator=' ', strip=True)
        return text[:5000] # Limit to prevent context bloat

    except Exception as e:
        raise McpError(ErrorData(code=INTERNAL_ERROR, message=f"Error: {str(e)}")) from e

if __name__ == "__main__":
    mcp.run(transport="sse", port=8002)
