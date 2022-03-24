#!/usr/bin/env bash

set -e

SENTINEL_TUNNEL_OUTPUT=${SENTINEL_TUNNEL_OUTPUT:-/dev/stdout}

if [ "${SENTINEL_TUNNEL_CONF}" == "" ]
then
  if [ "${SENTINEL_ADDRESES}" != "" ]
  then
    PARSED_LIST=$(printf '"%s"\n' "${SENTINEL_ADDRESES//,/\",\"}")
    jq -r --argjson sentinel_addresses "[$PARSED_LIST]" '.Sentinels_addresses_list = $sentinel_addresses' < /etc/tunnel-template.conf > /etc/tunnel.conf
    SENTINEL_TUNNEL_CONF="/etc/tunnel.conf"
  else
    echo "Sentinel addresses not found in SENTINEL_ADDRESES!"
    exit 1
  fi
fi

sentinel_tunnel ${SENTINEL_TUNNEL_CONF} ${SENTINEL_TUNNEL_OUTPUT}
