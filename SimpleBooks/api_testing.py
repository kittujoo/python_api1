import json
import random
from urllib.parse import urljoin
import jsonpath
import requests


BASE_URL = "https://simple-books-api.glitch.me"
class SimpleBooks:

    def authentication(self):
        with open("authentication.json", "r") as json_file:
            json_body = json_file.read()
            body = json.loads(json_body)
            base_url = BASE_URL
            resource = "/api-clients/"
            response = requests.post(urljoin(base_url,resource),json=body)
            # print(response.text)
            token = json.loads(response.text)
            # print(token['accessToken'])
            # access_token = jsonpath.jsonpath(token,'accessToken')

            # print(response.status_code)

            return token['accessToken']

    def create_book(self, id, name, token):
        import requests
        import json

        url = BASE_URL + "/orders/"

        payload = json.dumps({
            "bookId": id,
            "customerName": name
        })
        headers = {
            'Authorization': 'Bearer %s' % token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # print(response.text)
        # print(response.status_code)

        return (json.loads(response.text))['orderId']

    def get_all_books(self):
        url = BASE_URL + "/books"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def get_a_book(self, book_number):
        url = BASE_URL + "/books/%s" %book_number

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def update_order(self, order_id, token):
        url = BASE_URL + "/orders/"+order_id

        payload = json.dumps({
            "customerName": "Krushna"
        })
        headers = {
            'Authorization': 'Bearer %s' % token,
            'Content-Type': 'application/json'
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)

        print(response.text)

    def delete_order(self, order_id, token):
        url = BASE_URL + "/orders/"+order_id

        payload = {}
        headers = {
            'Authorization': 'Bearer %s' % token
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)

def read_json_file():
    with open("authentication.json", "r") as json_file:
        json_body = json_file.read()
        body = json.loads(json_body)
        print(body['clientEmail'])
        body['clientEmail'] = "Krushna"
        print(body)


if __name__ == "__main__":
    books = SimpleBooks()
    new_token = "1bce72ae2cc75ebaef284f6fc987d4a01391617b8dff6e0e9ff21984a9d90c77"
    # new_token = books.authentication()
    print("Your token generated successfully : ", new_token)
    order_id = books.create_book(1,'Comic', new_token)
    print("You have created order successfully, Your order_id is : ",order_id)
    books.get_all_books()
    books.get_a_book(1)
    books.update_order(order_id, new_token)
    books.delete_order(order_id, new_token)
    books.get_all_books()
