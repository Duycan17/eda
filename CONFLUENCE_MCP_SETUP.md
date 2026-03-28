# Atlassian Jira + Confluence MCP Setup

This workspace now includes the minimal Atlassian Rovo MCP client configuration needed to enable Jira and Confluence workflows from an MCP-capable client.

## What is already configured

- `.mcp.json`: points the client at the Atlassian Rovo MCP endpoint at `https://mcp.atlassian.com/v1/mcp`
- `AGENTS.md`: contains the default Jira project key, Confluence space, and Atlassian site instructions used by the agent

## What is still missing

You still need to provide your real Atlassian values in `AGENTS.md`:

1. Replace:
   - `YOURPROJ`
   - `YOUR_SPACE_ID`
   - `https://your-site.atlassian.net`
2. Reconnect or restart your MCP-capable client so it reloads `.mcp.json`.
3. Complete Atlassian OAuth sign-in, or configure a scoped API token if your environment uses headless auth.
4. Ensure your Atlassian account has access to:
   - the target Jira project
   - the target Confluence space
5. If your organization restricts MCP access, ask an admin to allow Atlassian Rovo MCP and the required Jira/Confluence scopes.

## How to find the missing values

- Jira project key: usually the prefix in issue keys such as `ABC-123`
- Confluence spaceId: available from Confluence space metadata or page/space administration tools
- Atlassian site URL: the base URL you use to open Jira or Confluence, such as `https://example.atlassian.net`

## Recommended `AGENTS.md` result

After replacement, the relevant section should look like this:

```md
When connected to `atlassian`:
- MUST use Jira project key = `ABC`
- MUST use Confluence spaceId = `"123456"`
- MUST use cloudId = `"https://example.atlassian.net"` and do not call resource discovery unless the value is unknown
- MUST use `maxResults: 10` or `limit: 10` for Jira JQL and Confluence CQL search operations
```

## How to verify Jira and Confluence are working

After reconnecting, try prompts like:

- `Find the latest issues in the configured Jira project.`
- `What Confluence spaces do I have access to?`
- `Search the configured Confluence space for project documentation.`
- `Create a Confluence page titled "Final Project Overview" in the configured space.`

If you still only see Jira tools, the usual causes are:

- the client has not reloaded the updated MCP config
- the Atlassian account used for auth does not have Confluence access
- the site admin has not enabled or authorized the required Rovo MCP access
- the current client integration exposes only a Jira subset even though the upstream Atlassian server supports Confluence

## Notes

- Atlassian documents the remote MCP endpoint as `https://mcp.atlassian.com/v1/mcp`.
- Atlassian's README also recommends setting `cloudId`, Jira project, and Confluence space defaults in `AGENTS.md` to reduce discovery calls.
- Actual tool availability depends on the client platform, Atlassian permissions, and admin policy.
