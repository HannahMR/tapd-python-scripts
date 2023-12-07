import requests
import codecs
import binascii
from urllib.parse import quote
from settings import REST_HOST, MACAROON_PATH, TLS_PATH

# This script retrieves the metadata for an asset and runs a hex to text
# converson on the response data.


# Function to convert hex to text
def hex_to_text(hex_string):
    try:
        decoded_bytes = binascii.unhexlify(hex_string)
        text = decoded_bytes.decode("utf-8")
        return text
    except Exception as e:
        print("Error converting hex to text:", e)
        return None


def main():
    asset_id = "asset-id"
    encoded_asset_id = quote(asset_id)

    url = (
        f"https://{REST_HOST}/v1/taproot-assets/assets/meta/asset-id/{encoded_asset_id}"
    )
    macaroon = codecs.encode(open(MACAROON_PATH, "rb").read(), "hex")
    headers = {"Grpc-Metadata-macaroon": macaroon}

    response = requests.get(url, headers=headers, verify=TLS_PATH)

    if response.status_code == 200:
        response_data = response.json()
        if "data" in response_data:
            hex_data = response_data["data"]
            text_data = hex_to_text(hex_data)
            if text_data is not None:
                print("Text Data:", text_data)
            else:
                print("Failed to convert hex to text.")
        else:
            print("No 'data' key in the response.")
    else:
        print("Error:", response.text)


if __name__ == "__main__":
    main()
