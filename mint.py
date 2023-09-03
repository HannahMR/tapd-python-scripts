import requests
import json
import codecs
from settings import REST_HOST, MACAROON_PATH, TLS_PATH


def main():
    url = f"https://{REST_HOST}/v1/taproot-assets/assets"
    macaroon = codecs.encode(open(MACAROON_PATH, "rb").read(), "hex")
    headers = {"Grpc-Metadata-macaroon": macaroon}

    ASSET_DATA = {
        "asset_type": "NORMAL",
        "name": "Alice Coin",
        "amount": 200000,
        # "group_key": "Group key here",
    }

    data = {
        "asset": ASSET_DATA,
        # "enable_emission" : True,
    }

    response = requests.post(
        url, headers=headers, data=json.dumps(data), verify=TLS_PATH
    )

    if response.status_code == 200:
        response_data = response.json()
        print("Response from tapd:", response_data)
    else:
        print("Error:", response.text)


if __name__ == "__main__":
    main()
