from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
times = 0


@api_view(["POST"])
def signup(request):
        print('Register Request Made!')
        print('Reading Data from JSON')
        if request.path == '/register/signup/':
            report_loc = '../signup/'
        else:
            report_loc = 'signup/'
        json2 = open('user_data.json', )
        data = json.load(json2)
        l1 = data['u_data'][0]
        emails = list(l1.keys())
        passwords = list(l1.values())
        json2.close()
        print('Read data from JSON')
        email = request.data.get('email')
        password = request.data.get('password')
        password1 = request.data.get('password1')
        usernames = []
        if email not in emails:
            if password == password1:
                emails.append(email)
                passwords.append(password)
                d4 = {emails[len(emails) - 1]: passwords[len(emails) - 1]}
                for x in range(len(emails) - 1):
                    d4 = dict(list(d4.items()) + list({emails[x]: passwords[x]}.items()))
                json_object = '{"u_data": [' + json.dumps(d4, indent=4) + ']}'
                a = open('user_data.json', 'w')
                a.write(json_object)
                a.close()
                times = 0
                print('Registered new user, returning HTTP response')
                return Response('You are now registered')
            else:
                print('Passwords do not match, returning HTTP response')
                return Response("Passwords do not match,")
        else:
            print('The Username or Email ID is already taken, returning HTTP response')
            return Response("Sorry. The Username or Email ID is already taken.")