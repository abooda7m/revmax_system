# This is config/supabase_client.py
from supabase import create_client, Client



url = "https://****"
key = "Key"
supabase: Client = create_client(url, key)
TABLE_NAME = "superstore_sales"
