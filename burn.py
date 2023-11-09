import requests
import codecs
import json
from settings import REST_HOST, MACAROON_PATH, TLS_PATH


def main():
    url = f"https://{REST_HOST}/v1/taproot-assets/burn"
    macaroon = codecs.encode(open(MACAROON_PATH, "rb").read(), "hex")
    headers = {"Grpc-Metadata-macaroon": macaroon}

    asset_id_hex = "asset-id-here"

    data = {
        "asset_id_str": asset_id_hex,
        "amount_to_burn": <uint64>,
        "confirmation_text": "assets will be destroyed",
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
