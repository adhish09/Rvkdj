import hashlib
import payu
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DonationSerializer
import time


def create_hash(data):
    # concatenate all the data values into a single string
    data_string = ''.join(str(value) for value in data.values())
    # append the merchant salt to the data string
    data_string += 'YOUR_MERCHANT_SALT'
    # encode the resulting string using SHA512 hashing
    hash_string = hashlib.sha512(data_string.encode()).hexdigest()
    return hash_string


class DonationView(APIView):
    def post(self, request, format=None):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            payu.merchant_id = 'YOUR_MERCHANT_ID'
            payu.salt = 'YOUR_MERCHANT_SALT'
            payu.sandbox_mode = True # set to False for production

            # create payment
            payment_data = {
                'txnid': str(serializer.validated_data['amount']) + str(time.time()),
                'amount': str(serializer.validated_data['amount']),
                'productinfo': serializer.validated_data['description'],
                'firstname': 'Test',
                'email': 'test@example.com',
                'phone': '1234567890',
                'surl': 'http://localhost:8000/donation-success/',
                'furl': 'http://localhost:8000/donation-failure/',
            }
            hash_string = create_hash(payment_data)
            payment_data['hash'] = hash_string
            payment = payu.Payments(**payment_data)
            response = payment.create()

            # check response status and return redirect URL
            if response.status == 'SUCCESS':
                return Response({'redirect_url': response.payment_url})
            else:
                return Response({'error': response.error_message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
