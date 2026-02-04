from flask_admin.contrib.sqla.validators import Unique
print("Checking Unique validator from Flask-Admin")
# Create a dummy unique validator (needs db session and model, but maybe we can inspect class or mock it)
# Actually Unique validator instance has field_flags?
# Let's inspect the class first
if hasattr(Unique, 'field_flags'):
    print(f"Unique class field_flags: {Unique.field_flags}")

# Try to instantiate
try:
    # It needs session, model, column
    # We can use mock objects
    class Mock: pass
    u = Unique(Mock(), Mock(), Mock())
    if hasattr(u, 'field_flags'):
        print(f"Unique instance field_flags type: {type(u.field_flags)}")
        print(f"Unique instance field_flags value: {u.field_flags}")
except Exception as e:
    print(f"Could not instantiate Unique: {e}")
