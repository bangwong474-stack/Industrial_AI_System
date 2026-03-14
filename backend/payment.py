from fastapi import APIRouter

router=APIRouter()

@router.post("/create-payment")
def create_payment():
    return{"payment_url":"https://payment-link"}

@router.post("/verify-payment")
def verify_payment():
    payment_status="successfully"

    if payment_status=="successfully":
        return{"status":"account activated"}
    
    return{"status":"payment failed"}