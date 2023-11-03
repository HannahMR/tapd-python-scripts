import codecs, json, requests
from settings import REST_HOST, MACAROON_PATH, TLS_PATH


def main():
    url = f"https://{REST_HOST}/v1/taproot-assets/universe/stats"
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
