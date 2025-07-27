import pandas as pd
import firebase_admin
from firebase_admin import credentials, db
import re

# ----------------- CONFIGURATION -------------------
EXCEL_FILE = "ai_robotics_qa.xlsx"  # <-- Change if needed
FIREBASE_DB_URL = "https://qa-system-97317-default-rtdb.asia-southeast1.firebasedatabase.app/"  # <-- Your Firebase URL
SERVICE_ACCOUNT_FILE = "qa-system-97317-firebase-adminsdk-fbsvc-ef55f9a971.json"  # <-- Your downloaded credentials file
# ---------------------------------------------------

# 1. Load Excel File
df = pd.read_excel(EXCEL_FILE)
print("🔍 Original columns:", df.columns.tolist())

# 2. Clean column names (remove spaces, lowercase)
df.columns = df.columns.str.strip().str.lower()

# 3. Ensure required columns are present
required_columns = {'question', 'answer'}
if not required_columns.issubset(set(df.columns)):
    raise ValueError(f"❌ Missing required columns. Found: {df.columns.tolist()}")

# 4. Drop empty rows
df.dropna(subset=['question', 'answer'], inplace=True)

# 5. Initialize Firebase
cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_DB_URL
})
ref = db.reference('qa_pairs')

# 6. Function to sanitize Firebase keys
def sanitize_key(key):
    key = str(key)
    key = re.sub(r'[.$#[\]/]', '_', key)  # Replace invalid Firebase key characters
    return key.strip()

# 7. Prepare data dictionary
qa_data = {
    sanitize_key(row['question']): row['answer']
    for _, row in df.iterrows()
}

# 8. Upload to Firebase
ref.set(qa_data)
print("✅ Data uploaded successfully to Firebase.")
