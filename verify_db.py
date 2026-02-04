from app import app, db, Project

with app.app_context():
    projects = Project.query.all()
    for p in projects:
        print(f"Project: {p.title}")
        print(f"Blurb: {p.blurb[:50]}...")
        print(f"Desc: {p.description[:50]}...")
        print("-" * 20)
