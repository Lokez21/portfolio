from app import app, db, User, About, Education, Experience, Project

def seed():
    with app.app_context():
        # Clear existing data
        # Clear existing data and re-create tables to update schema
        db.drop_all()
        db.create_all() # Re-create tables with new schema


        # 0. Admin User
        admin = User(username='admin')
        admin.set_password('admin123')
        db.session.add(admin)

        # 1. About
        about = About(
            name="YourName",
            job_title="Web Designer & Developer",
            email="user@example.com",
            linkedin_url="https://linkedin.com/in/username",
            github_url="https://github.com/username",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            profile_image="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80"
        )
        db.session.add(about)
        
        # 2. Education
        edu1 = Education(
            degree="Master of Computer Science",
            institution="Stanford University",
            year_start=2018,
            year_end=2020,
            description="• Specialized in Artificial Intelligence\n• Thesis on Neural Networks\n• Graduated with Honors (GPA 3.9)"
        )
        edu2 = Education(
            degree="Bachelor of Science in Computer Engineering",
            institution="University of California, Berkeley",
            year_start=2014,
            year_end=2018,
            description="• Dean's List for 6 Semesters\n• President of Coding Club\n• Minor in Business Administration"
        )
        db.session.add_all([edu1, edu2])

        # 3. Experience
        exp1 = Experience(
            role="Senior Frontend Engineer",
            company="Tech Giants Inc.",
            year_start=2022,
            year_end=None,
            description="• Led a team of 5 developers primarily using React and TypeScript.\n• Improved site performance by 40% through code splitting and lazy loading.\n• Collaborated with UX designers to implement a new design system."
        )
        exp2 = Experience(
            role="Software Developer",
            company="StartUp Solutions",
            year_start=2020,
            year_end=2022,
            description="• Developed and maintained full-stack web applications using Python/Django.\n• Implemented RESTful APIs for mobile application consumption.\n• Automated deployment pipelines using Docker and Jenkins."
        )
        db.session.add_all([exp1, exp2])

        # 4. Projects
        proj1 = Project(
            title="E-Commerce Platform",
            blurb="A fully featured e-commerce application built with Next.js and Stripe.",
            description="A fully featured e-commerce application built with Next.js and Stripe.\n\nKey Features:\n• User authentication and profile management\n• Shopping cart and checkout functionality\n• Admin dashboard for product management\n• Secure payment processing with Stripe\n• Responsive design for all devices\n\nThis project demonstrates the ability to build a full-stack application with modern technologies. It includes a robust backend for managing products, orders, and users, and a sleek frontend for a seamless shopping experience.",
            image_url="https://images.unsplash.com/photo-1557821552-17105176677c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
            link="#",
            link_visibility=True
        )
        proj2 = Project(
            title="Task Management App",
            blurb="A productivity tool aimed availability for remote teams.",
            description="A productivity tool aimed at improving availability and collaboration for remote teams.\n\nKey Features:\n• Real-time updates using WebSockets\n• Drag and drop Kanban board\n• Integrated with Slack and Calendar\n• Team analytics and reporting\n• Customizable workflows\n\nBuilt to help teams stay organized and efficient, this app provides a centralized hub for task management. The real-time features ensure that everyone is always on the same page.",
            image_url="https://images.unsplash.com/photo-1540350394557-8d14678e7f91?ixlib=rb-1.2.1&auto=format&fit=crop&w=1332&q=80",
            link="#",
            link_visibility=True
        )
        proj3 = Project(
            title="Health & Fitness Tracker",
            blurb="Mobile-first web application to track workouts and nutrition.",
            description="Mobile-first web application designed to help users track their workouts and nutrition goals.\n\nKey Features:\n• Interactive charts using D3.js\n• Calorie counter with extensive food database\n• Social sharing features\n• Workout routine planner\n• Progress tracking and analytics\n\nThis application focuses on user engagement and data visualization, helping users verify their progress and stay motivated on their fitness journey.",
            image_url="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
            link="#",
            link_visibility=True
        )
        db.session.add_all([proj1, proj2, proj3])

        db.session.commit()
        print("Database populated successfully!")

if __name__ == '__main__':
    seed()
