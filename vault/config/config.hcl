ui = true
disable_mlock = false

storage "etcd" {
  address  = "http://backend-etcd-01:2379,http://backend-etcd-02:2379,http://backend-etcd-03:2379"
  etcd_api = "v3"
}

listener "tcp" {
  address     = "0.0.0.0:8200"
  tls_disable = 1
}
