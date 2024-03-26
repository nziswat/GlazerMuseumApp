#This middleware is used to loosely ensure that each vote is unique to each voter.
#Some caveats: this isn't secure at all and operates under the assumption no one will bother to mess with the cookies on their own device.
import uuid
from django.utils.deprecation import MiddlewareMixin

class VerifyUser(MiddlewareMixin): 
    def process_request(self, request):
        if not request.COOKIES.get('user_id'):
            # Generate a unique ID
            unique_id = uuid.uuid4()  
            request.unique_id = unique_id
        else:
            request.unique_id = request.COOKIES['user_id']

    def process_response(self, request, response):
        if not request.COOKIES.get('user_id'):
            response.set_cookie('user_id', request.unique_id, max_age=86400)  # the cookie here expires in just one day, letting the user come back the next day and vote again, uniquely.
        return response