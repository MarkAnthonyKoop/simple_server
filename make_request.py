import httpx

def make_request(url):
    try:
        response = httpx.get(url)
        response.raise_for_status()
        print(f"Success: {response.status_code}")
        return response.text
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        print(f"Status code: {e.response.status_code}")
        print(f"Error response: {e.response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'http://example.com' with the URL you want to test
#url_to_test = "https://www.middlematter.com/"
#url_to_test = "https://newtest.middlematter.com/"
#url_to_test = "https://www.thisgotmissed.com/"
url_to_test = "https://davidtest.middlematter.com/"
url_to_test = "https://www.newtest.middlematter.com/"

make_request(url_to_test)

