import requests
import json
import codecs
from urllib.parse import quote
from settings import REST_HOST, MACAROON_PATH, TLS_PATH


def main():
    asset_id = "f89114c2cddd40a15a318d7d5b0e7b518f6e8771ec895beac0b59c9fdaae5a1f"
    encoded_asset_id = quote(asset_id)

    url = (
        f"https://{REST_HOST}/v1/taproot-assets/assets/meta/asset-id/{encoded_asset_id}"
    )
    macaroon = codecs.encode(open(MACAROON_PATH, "rb").read(), "hex")
    headers = {"Grpc-Metadata-macaroon": macaroon}

    response = requests.get(url, headers=headers, verify=TLS_PATH)

    if response.status_code == 200:
        response_data = response.json()
        print("Response from tapd:", response_data)
    else:
        print("Error:", response.text)


if __name__ == "__main__":
    main()
