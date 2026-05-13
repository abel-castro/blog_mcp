# blog-mcp

MCP server for [abelcastro.dev](https://core.abelcastro.dev). Exposes tools to create draft posts and list published posts directly from Claude.

## Requirements

- [uv](https://docs.astral.sh/uv/)
- An API token created via the Django admin (`/admin` → API Tokens → Add)

## Setup

```bash
cd blog-mcp
uv sync
```

## Configuration

Create a `.env` file in the project root:

```bash
BLOG_API_TOKEN="your-token-here"
```

Optionally, to use a local dev server instead of `https://core.abelcastro.dev/api`:

```bash
BLOG_API_BASE="http://localhost:8000/api"
```

### Claude Code (terminal/IDE)

Add to `.mcp.json` in the project root:

```json
{
  "mcpServers": {
    "blog": {
      "command": "uv",
      "args": ["run", "server.py"],
      "cwd": "/absolute/path/to/blog-mcp"
    }
  }
}
```

### Claude Desktop app

Add the same block to `~/.claude/claude_desktop_config.json` under `mcpServers`.

## Available tools

| Tool                                       | Description                                                                                                                                     |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_draft_post(title, content, tags?)` | Creates a draft post. `content` is Markdown. `tags` is an optional list of strings. Returns the created post including its auto-generated slug. |
| `list_posts(query?)`                       | Lists published posts. Optionally filter by a search term across title, content, and tags.                                                      |
