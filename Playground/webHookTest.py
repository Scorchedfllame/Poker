from json import dumps

from httplib2 import Http

WEBHOOK_URL = "https://chat.googleapis.com/v1/spaces/AAAApmWJUuQ/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=tkcmGAvlH6f0V1EsVXwD2LTaQqEAJE_h8wDJaMia1-E"

def main():
    """Google Chat incoming webhook quickstart."""
    url = WEBHOOK_URL
    app_message = {
        'text': '_____'}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(app_message),
    )
    print(response)


if __name__ == '__main__':
    main()