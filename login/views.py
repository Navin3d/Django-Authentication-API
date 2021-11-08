from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
times = 0


@api_view(["POST"])
def signin(request):
        print('Login Request Made!')
        print('Reading Data from JSON')
        json2 = open('user_data.json', )
        data = json.load(json2)
        l1 = data['u_data'][0]
        emails = list(l1.keys())
        passwords = list(l1.values())
        json2.close()
        print('Read data from JSON')
        global times
        times = times + 1
        email = request.data.get('email')
        password = request.data.get('password')
        if email in emails:
            if passwords[emails.index(email)] == password:
                times = 0
                print('Logged in User, returning HTTP response')
                return Response('Logged in as User')
            else:
                print('Email != Password, returning HTTP response')
                return Response('Email != Password,')
        else:
            print('Account does not exist, returning HTTP response')
            return Response('Account does not exist,')