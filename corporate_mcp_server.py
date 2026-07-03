from fastmcp import FastMCP
import json
# Initialize the FastMCP server
mcp = FastMCP("Corporate Compliance Server")
DATABASE = {
    "PII_RULES": [
        {"entity": "EMAIL", "pattern": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "action": "REDACT"},
        {"entity": "SSN", "pattern": r"\d{3}-\d{2}-\d{4}", "action": "REDACT"}
    ],
    "CONFIDENTIAL_PROJECTS": [
        "Project Apollo",
        "Titanium Launch"
    ]
}
@mcp.tool()
def get_compliance_rules() -> str:
    """Returns the internal corporate compliance and redaction rules."""
    return json.dumps(DATABASE)
if __name__ == "__main__":
    mcp.run(transport="sse", port=8001)
