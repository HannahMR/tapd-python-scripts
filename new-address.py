import requests
import base64
import json
import codecs
from settings import REST_HOST, MACAROON_PATH, TLS_PATH


def main():
    url = f"https://{REST_HOST}/v1/taproot-assets/addrs"
    macaroon = codecs.encode(open(MACAROON_PATH, "rb").read(), "hex")
    headers = {"Grpc-Metadata-macaroon": macaroon}

    data = {
        "asset_id": "id string here",
        "amt": 1000,
        "tapscript_sibling": "",
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
