from app import app
import traceback

try:
    with app.test_client() as client:
        resp = client.get('/admin/', follow_redirects=True)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 500:
            print("Response output (truncated):")
            print(resp.data[:2000])
except Exception:
    traceback.print_exc()
