from freeze import freezer
from app import app
import traceback

print("Inspecting Freezer URLs...")
try:
    with app.app_context():
        for url in freezer.all_urls():
            print(f"URL: '{url}'")
            if not url.startswith('/'):
                print(f"WARNING: URL '{url}' does not start with /")
except Exception:
    traceback.print_exc()
