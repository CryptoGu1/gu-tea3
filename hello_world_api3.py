import requests

def fetch_hello_world():
    response = requests.get('https://api.agify.io/?name=michael')
    print(response.json()['age'])

if __name__ == "__main__":
    fetch_hello_world()
