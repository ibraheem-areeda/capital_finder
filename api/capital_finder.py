from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    """
    A custom request handler that handles GET requests and retrieves information about capitals and countries.
    """

    def do_GET(self):
        """
        Handles the GET request and sends the appropriate response based on the provided query parameters.
        """

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        app_url = self.path
        url_parts = parse.urlsplit(app_url)
        query_list = parse.parse_qsl(url_parts.query)
        query_dict = dict(query_list)

        capital_query_val = query_dict.get('capital')
        country_query_val = query_dict.get('country')

        if "capital" in query_dict:
            response = requests.get(f'https://restcountries.com/v3.1/capital/{capital_query_val}')
            select_res = str(response.json()[0]["name"]["common"])
            formated_res = f"{capital_query_val} is the capital of {select_res}."
            self.wfile.write(formated_res.encode())

        elif "country" in query_dict:
            response = requests.get(f'https://restcountries.com/v3.1/name/{country_query_val}')
            select_res = str(response.json()[0]["capital"][0])
            formated_res = f"The capital of {country_query_val} is {select_res}."
            self.wfile.write(formated_res.encode())

        else:
            self.wfile.write("Please enter a valid query".encode())

        return







       
       
       
       
       
       
       
       
