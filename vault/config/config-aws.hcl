api_addr = "https://vault.umbrellacorp.cloud"

ui = true
plugin_directory = "/opt/vault/plugins/"

listener "tcp" {
  address                  = "0.0.0.0:8200"
  cluster_address          = "0.0.0.0:8201"
  tls_disable_client_certs = true
  tls_cert_file            = "/opt/vault/tls/vault.pem"
  tls_key_file             = "/opt/vault/tls/vault.key"

  telemetry {
    unauthenticated_metrics_access = true
  }
}

telemetry {
  prometheus_retention_time = "30s"
  disable_hostname          = true
  statsd_address            = "127.0.0.1:9125"
}

storage "dynamodb" {
  ha_enabled = "true"
  table = "sec-vault-main"
  region = "eu-west-1"
}

seal "awskms" {
  kms_key_id = "fab50482-0000-0000-0000-fe271ce24c06"
  region = "eu-central-1"
}
