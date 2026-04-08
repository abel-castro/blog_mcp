# blog-mcp

MCP server for [abelcastro.dev](https://abelcastro.dev). Exposes tools to create draft posts and list published posts directly from Claude.

## Requirements

- [uv](https://docs.astral.sh/uv/)
- An API token created via the Django admin (`/admin` → API Tokens → Add)

## Setup

```bash
cd blog-mcp
uv sync
```

## Configuration

Add to your Claude Code MCP config (`~/.claude/claude_desktop_config.json` or via `claude mcp add`):

```json
{
  "mcpServers": {
    "blog": {
      "command": "uv",
      "args": ["run", "server.py"],
      "cwd": "/absolute/path/to/blog-mcp",
      "env": {
        "BLOG_API_TOKEN": "your-token-here"
      }
    }
  }
}
```

By default the server points to `https://abelcastro.dev/api`. To use a local dev server instead, add:

```json
"BLOG_API_BASE": "http://localhost:8000/api"
```

## Available tools

| Tool | Description |
|------|-------------|
| `create_draft_post(title, content, tags?)` | Creates a draft post. `content` is Markdown. `tags` is an optional list of strings. Returns the created post including its auto-generated slug. |
| `list_posts(query?)` | Lists published posts. Optionally filter by a search term across title, content, and tags. |
