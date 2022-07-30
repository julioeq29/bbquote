import requests

def get_quote():
    url = 'https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes'
    response = requests.get(url).json()[0]
    # return f"'{response['quote']}' \n> {response['author']}"
    return response['quote'], response['author']

if __name__ == "__main__":
    print(get_quote())
