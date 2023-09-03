import requests
import json
import codecs
from settings import REST_HOST, MACAROON_PATH, TLS_PATH


# Function to convert image to hex
def image_to_hex(image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    hex_representation = image_bytes.hex()
    return hex_representation


def main():
    url = f"https://{REST_HOST}/v1/taproot-assets/assets"
    macaroon = codecs.encode(open(MACAROON_PATH, "rb").read(), "hex")
    headers = {"Grpc-Metadata-macaroon": macaroon}

    # Convert image to hex
    image_hex = image_to_hex("/home/hannah/Temp/Tapd-Python/key.png")

    ASSET_META_DATA = {
        "data": image_hex,
        "type": 1,
    }

    ASSET_DATA = {
        "asset_type": "COLLECTIBLE",
        "name": "Bob's Key",
        "asset_meta": ASSET_META_DATA,
        "amount": 1,
    }

    data = {
        "asset": ASSET_DATA,
        "enable_emission": False,
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
