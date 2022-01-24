# Export variables
```
export OAUTH_CLIENT_ID=$(vault kv get --field=client_id kv/external/google/vault/prod/oauth)
export OAUTH_CLIENT_SECRET=$(vault kv get --field=secret kv/external/google/vault/prod/oauth)
export OAUTH_EMAIL_DOMAIN=testmail.com
```