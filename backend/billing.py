import requests
import json

from backend.config import FLUTTERWAVE_SECRET_KEY,PAYMENT_CALLBACK_URL

BASE_URL="https://api.flutterwave.com/v3"
headers={"Authorization":f"Bearer{FLUTTERWAVE_SECRET_KEY}","Content-type":"application/json"}

def create_payment(amount,currency,customer_number,tx_ref,plan_name):
    """amount:number(TZS)
    currency:"TZS"
    customer_number:mobie number of factory
    tx_ref:unique transaction reference
    plan_name:"Basic","Pro","Enterprise"""     

    data={"tx_ref":tx_ref,"amount":amount,"currency":currency,"payment_type":"Mobilemoney",
          "redirect_url":PAYMENT_CALLBACK_URL,"customer":{"email":f"{customer_number}@nomail.com",
            "phonenumber":customer_number,"name":f"Factory{tx_ref}"},"customizations":
            {"title":f"{plan_name}Subscription","description":f"payment for plan{plan_name}"""}}
                                                                                
    response=requests.post(f"{BASE_URL}/charges?type=mobilemoneytz",headers=headers,json=data)
    if response.status_code==200:
        return response.json()["data"]["link"]
    else:
        return f"Error creating payment:{response.text}"
    
def create_checkout_session(amount,mobile_number):
    print("Creating checkout session...")
    return{"status":"success","amount":amount,"mobile":mobile_number}

def verify_payment(tx_ref):
    response=requests.get(f"{BASE_URL}/transactions/verify_by_reference?tx_ref={tx_ref}",headers=headers)
            
    if response.status_code==200:
        data=response.json()["data"]
        status=data["status"]
        amount=data["amount"]
        currency=data["currency"]
        return{"status":status,"amount":amount,"currency":currency}
    else:
        return{"status":"error","message":response.text}

result=verify_payment('tx_ref')
print("Payment verification:",result)