# Configuration file for Industrial AI System

BASE_URL="https://Industrial_AI_System.up.railway.app"

PAYMENT_CALLBACK_URL=f"{BASE_URL}/payment/callback"

FLUTTERWAVE_SECRET_KEY ="supersecretkey"
API_TOKEN="MY_SUPER_SECURE_API_TOKEN_123"

#PostgreSQL URL
DATABASE_URL = "postgresql://postgres:password@localhost/industrial_ai"

#Stripe keys(test)
STRIPE_SECRET_KEY = "sk_test_your_secret_key_here"
STRIP_PRICE_BASIC="price_basic_id"
STRIP_PRICE_PRO="price_pro_id"
STRIP_PRICE_ENTERPRISE="price_enterprise_id"