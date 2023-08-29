import requests
import base64
import json
import codecs
from settings import REST_HOST, MACAROON_PATH, TLS_PATH


def main():
    url = f"https://{REST_HOST}/v1/taproot-assets/assets"
    macaroon = codecs.encode(open(MACAROON_PATH, "rb").read(), "hex")
    headers = {"Grpc-Metadata-macaroon": macaroon}

    ASSET_META_DATA = {
        "data": "Some random meta data",
        "type": "No idea",
        "meta_hash": "fakehash",
    }

    ASSET_DATA = {
        "asset_type": "NORMAL",
        "name": "Hannah Coin",
        "amount": 1000,
    }

    data = {
        "asset": ASSET_DATA,
        "enable_emission": True,
    }

    response = requests.post(
        url, headers=headers, data=json.dumps(data), verify=TLS_PATH
    )

    if response.status_code == 200:
        response_data = response.json()
        print("Response from tapd:", response_data["text"])
    else:
        print("Error:", response.text)


if __name__ == "__main__":
    main()
