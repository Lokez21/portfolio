from wtforms import validators

opt = validators.Optional()
print(f"Optional validator: {opt}")
if hasattr(opt, 'field_flags'):
    print(f"field_flags type: {type(opt.field_flags)}")
    print(f"field_flags value: {opt.field_flags}")
else:
    print("No field_flags attribute")

# Check if checking items() on it fails
try:
    for k, v in getattr(opt, 'field_flags', {}).items():
        print(k, v)
except Exception as e:
    print(f"Error iterating items: {e}")
