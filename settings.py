# settings.py
# Examples for connecting to tapd nodes running via Polar

# Alice
REST_HOST = "127.0.0.1:8289"
MACAROON_PATH = (
    "/home/hannah/.polar/networks/1/volumes/tapd/alice-tap/data/regtest/admin.macaroon"
)
TLS_PATH = "/home/hannah/.polar/networks/1/volumes/tapd/alice-tap/tls.cert"

# Bob
# REST_HOST = "127.0.0.1:8290"
# MACAROON_PATH = (
#     "/home/hannah/.polar/networks/1/volumes/tapd/bob-tap/data/regtest/admin.macaroon"
# )
# TLS_PATH = "/home/hannah/.polar/networks/1/volumes/tapd/bob-tap/tls.cert"
