API advanced

Reddit now requires OAuth2 for Data API access.

Set these environment variables before running the scripts:

- `REDDIT_CLIENT_ID`
- `REDDIT_CLIENT_SECRET`
- `REDDIT_USERNAME` (used in `User-Agent`)

Optional:

- `REDDIT_APP_ID` (default: `api_advanced`)
- `REDDIT_APP_VERSION` (default: `1.0.0`)
- `REDDIT_USER_AGENT` (overrides generated value)

Example:

```bash
export REDDIT_CLIENT_ID="your_client_id"
export REDDIT_CLIENT_SECRET="your_client_secret"
export REDDIT_USERNAME="your_reddit_username"
python3 0-main.py python
```
