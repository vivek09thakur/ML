import requests

def get_response(prompt):
    api_url = 'http://127.0.0.1:5000/infer'
    try:
        payload = {'user_input': prompt}
        response = requests.post(api_url, json=payload)
        return response.json()['response']
    except requests.ConnectTimeout:
        print("API took too long to respond! Please check the server side") 
    except requests.ConnectionError:
        print("Cloud not connect to internet! Please check the connection")
    except Exception as e:
        print("Error Occured at => {}".format(e))


if __name__=='__main__':
    while True:
        try:
            user_input = input('<user> : ')
            response = get_response(prompt=user_input)
            if response != None:
                print(f'<model> : {response}')
        except KeyboardInterrupt:
            print("KEYBOARD INTERRUPT")
            break