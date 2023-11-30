# views.py

import paypalrestsdk
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse

paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

# def create_payment(request):
#     print("Executing create payment")
#     payment = paypalrestsdk.Payment({
#         "intent": "sale",
#         "payer": {
#             "payment_method": "paypal",
#         },
#         "redirect_urls": {
#             "return_url": request.build_absolute_uri(reverse('execute_payment')),
#             "cancel_url": request.build_absolute_uri(reverse('payment_failed')),
#         },
#         "transactions": [
#             {
#                 "amount": {
#                     "total": "10.00",  # Total amount in USD
#                     "currency": "USD",
#                 },
#                 "description": "Payment for Product/Service",
#             }
#         ],
#     })
#
#     print("Checking Payment.create()")
#     if payment.create():
#         print(f"payment create successfull redirecting to {payment.links[1].href}")
#         return redirect(payment.links[1].href)  # Redirect to PayPal for payment
#     else:
#         return render(request, 'payments/payment_failed.html')


def create_payment(request):
    print("In manual create payment ")
    import requests
    from requests.auth import HTTPBasicAuth

    # Replace with your actual PayPal client ID and secret
    CLIENT_ID = settings.PAYPAL_CLIENT_ID
    CLIENT_SECRET = settings.PAYPAL_CLIENT_SECRET

    # PayPal API endpoints
    PAYPAL_API_URL = 'https://api.sandbox.paypal.com'  # Use 'https://api.paypal.com' for live environment
    TOKEN_URL = '/v1/oauth2/token'
    PAYMENT_URL = '/v1/payments/payment'

    # Set up authentication headers
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    # Step 1: Get Access Token
    token_data = {
        'grant_type': 'client_credentials'
    }

    token_response = requests.post(f'{PAYPAL_API_URL}{TOKEN_URL}', auth=auth, data=token_data, headers=headers)
    token = token_response.json().get('access_token')

    # Step 2: Create Payment
    payment_data = {
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "transactions": [
            {
                "amount": {
                    "total": "10.00",  # Replace with your actual amount
                    "currency": "USD"
                },
                "description": "Payment for your product"
            }
        ],
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('execute_payment')),  # Replace with your actual return URL
            "cancel_url": request.build_absolute_uri(reverse('payment_failed')) # Replace with your actual cancel URL
        }
    }

    headers['Authorization'] = f'Bearer {token}'

    payment_response = requests.post(f'{PAYPAL_API_URL}{PAYMENT_URL}', json=payment_data, headers=headers)

    if payment_response.status_code == 201:
        payment_url = next(link['href'] for link in payment_response.json()['links'] if link['rel'] == 'approval_url')
        print(f'Payment created successfully. Redirect user to: {payment_url}')
        return redirect(payment_url)
    else:
        print(f'Error creating payment: {payment_response.json()}')
        return redirect("payment_failed")

# views.py

def execute_payment(request):
    print("Executing execute_payment")
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        print("executing payment.execute")
        return render(request, 'payments/payment_success.html')
    else:
        return render(request, 'payments/payment_failed.html')

def payment_checkout(request):
    return render(request, 'payments/checkout.html')

def payment_failed(request):
    return render(request,"payments/payment_failed.html")
def index(request):
    return render(request,"payments/index.html")

