import requests

url = "https://movie-quote-api.herokuapp.com/v1/quote/"

def get_quote():
    
    response = requests.get(url).json()
    
    return response['show'], response['role'], response['quote']
    
if __name__=="__main__":
    print(get_quote())