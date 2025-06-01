# This is config/supabase_client.py
from supabase import create_client, Client



url = "https://bwcrzsxdufasjwvrasxp.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ3Y3J6c3hkdWZhc2p3dnJhc3hwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgxMzIxMTUsImV4cCI6MjA2MzcwODExNX0.WbaNQ_GTnxmc3fLyI-t0hRTA7lGE5g3y-LUSnKWbgmk"
supabase: Client = create_client(url, key)
TABLE_NAME = "superstore_sales"