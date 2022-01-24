# Export variables
```
export OAUTH_CLIENT_ID=$(vault kv get --field=client_id kv/external/google/vault/prod/oauth
554532959844-n2oge0hn6og6gsmdgjia1n9ibprp3iri.apps.googleusercontent.com)
export OAUTH_CLIENT_SECRET=$(vault kv get --field=secret kv/external/google/vault/prod/oauth
_NHmcw1GdJyKTq0-kXcrhW2i)
export OAUTH_EMAIL_DOMAIN=testmail.com
```