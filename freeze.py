from flask_frozen import Freezer
from flask import url_for
from app import app, Project

# Configuration for static site generation
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

# Disable automatic URL generation for endpoints without arguments
# This prevents it from trying to freeze /admin/ which causes errors
freezer = Freezer(app, with_no_argument_rules=False)

@freezer.register_generator
def url_generator():
    # Start at the home page
    with app.test_request_context():
        yield url_for('index')
    
    # Explicitly yield project details
    with app.app_context():
        projects = Project.query.all()
        for project in projects:
            yield 'project_detail', {'project_id': project.id}

if __name__ == '__main__':
    print("Freezing application to 'static-site' folder...")
    try:
        freezer.freeze()
        print("Done! Static site generated in 'docs/'.")
    except Exception:
        import traceback
        traceback.print_exc()
