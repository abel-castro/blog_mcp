import os

import httpx
from mcp.server.fastmcp import FastMCP

API_TOKEN = os.environ["BLOG_API_TOKEN"]
API_BASE = os.environ.get("BLOG_API_BASE", "https://abelcastro.dev/api")

mcp = FastMCP("blog")


@mcp.tool()
def create_draft_post(title: str, content: str, tags: list[str] | None = None) -> dict:
    """Create a draft blog post on abelcastro.dev."""
    response = httpx.post(
        f"{API_BASE}/posts/",
        json={"title": title, "content": content, "tags": tags or []},
        headers={"Authorization": f"Bearer {API_TOKEN}"},
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def list_posts(query: str | None = None) -> dict:
    """List published posts on abelcastro.dev."""
    params = {"query": query} if query else {}
    response = httpx.get(f"{API_BASE}/posts/", params=params)
    response.raise_for_status()
    return response.json()


def main():
    mcp.run()


if __name__ == "__main__":
    main()
