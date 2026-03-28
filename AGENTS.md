## Atlassian Rovo MCP

Workspace status:
- `.mcp.json` already points to `https://mcp.atlassian.com/v1/mcp`
- The values below are still placeholders and must be replaced before Jira or Confluence work begins

When connected to `atlassian`:
- MUST use Jira project key = `YOURPROJ`
- MUST use Confluence spaceId = `"YOUR_SPACE_ID"`
- MUST use cloudId = `"https://your-site.atlassian.net"` and do not call resource discovery unless the value is unknown
- MUST use `maxResults: 10` or `limit: 10` for Jira JQL and Confluence CQL search operations
- MUST confirm before destructive or high-impact operations such as bulk page creation, page overwrite, issue deletion, or mass linking

### Confluence tasks

Prefer these workflows when the server exposes Confluence tools:
- Summarize an existing page
- Create a new page in the configured space
- Search pages in the configured space before creating duplicates
- Link Jira issues to the final Confluence page

### Space setup

Replace these placeholders before use:
- `YOURPROJ`
- `YOUR_SPACE_ID`
- `https://your-site.atlassian.net`

Examples:
- Jira project key: `ABC`
- Confluence spaceId: `"123456"`
- cloudId/site URL: `"https://example.atlassian.net"`

### Example prompts

- `Summarize the requirements page in Confluence.`
- `Create a Confluence page titled "Project Documentation" in the configured space.`
- `Search the configured Confluence space for pages about sentiment analysis.`
- `Link Jira issue YOURPROJ-123 to the Confluence page "Project Documentation".`
