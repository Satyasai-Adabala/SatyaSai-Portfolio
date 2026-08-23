"""
Run with: python manage.py shell < populate.py
(or: python manage.py runscript populate — if you install django-extensions)

This seeds the database with Sai's real data pulled from his SE and Data
Analyst resumes. Safe to re-run — it clears and re-creates content rows.
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

from django.core.files import File
from core.models import (
    SiteProfile, SkillGroup, Skill, Project, Experience, Education, Certification
)

print("Seeding portfolio data...")

# --------------------------------------------------------------------- #
# SITE PROFILE
# --------------------------------------------------------------------- #
profile = SiteProfile.load()
profile.full_name = "Adabala Satya Sai"
profile.location = "Razole, Andhra Pradesh, India"
profile.email = "saiadabala53@gmail.com"
profile.phone = "+91 8008968188"
profile.github_url = "https://github.com/Satyasai-Adabala"
profile.linkedin_url = "https://linkedin.com/in/satya-sai-adabala-333687286"
profile.tagline_se = "Python & Django Developer who ships working software, not tutorial clones."
profile.tagline_da = "Data Analyst who turns messy datasets into decisions people can act on."
profile.summary = (
    "Aspiring Software Engineer and Data Analyst with a B.Tech in Electronics & "
    "Communication Engineering (CGPA 8.5). I've built and deployed a full-stack "
    "Django e-commerce platform, run four end-to-end data analysis and machine "
    "learning projects, and completed two internships — one in Python web "
    "development, one in data science."
)
profile.projects_completed = 5
profile.technologies_count = 20
profile.internships_count = 2
profile.certifications_count = 4

resume_se_path = "media/resumes/Adabala_Satya_Sai_SE_Resume.pdf"
resume_da_path = "media/resumes/Adabala_Satya_Sai_Data_Analyst_Resume.pdf"
if os.path.exists(resume_se_path) and not profile.resume_se:
    with open(resume_se_path, "rb") as f:
        profile.resume_se.save("Adabala_Satya_Sai_SE_Resume.pdf", File(f), save=False)
if os.path.exists(resume_da_path) and not profile.resume_da:
    with open(resume_da_path, "rb") as f:
        profile.resume_da.save("Adabala_Satya_Sai_Data_Analyst_Resume.pdf", File(f), save=False)
profile.save()

# --------------------------------------------------------------------- #
# SKILLS
# --------------------------------------------------------------------- #
SkillGroup.objects.all().delete()

programming = SkillGroup.objects.create(name="Programming & Scripting", track="both", order=1)
for name, pct in [("Python", 90), ("SQL", 82), ("C", 65)]:
    Skill.objects.create(group=programming, name=name, proficiency=pct)

backend = SkillGroup.objects.create(name="Backend & Web", track="se", order=2)
for name, pct in [("Django", 85), ("Django ORM", 82), ("HTML / CSS", 78), ("REST-style App Design", 70)]:
    Skill.objects.create(group=backend, name=name, proficiency=pct)

data_analytics = SkillGroup.objects.create(name="Data & Analytics", track="da", order=3)
for name, pct in [("Pandas / NumPy", 88), ("Power BI (DAX, Power Query)", 82), ("Matplotlib / Seaborn", 80), ("Excel (Pivot Tables, VLOOKUP)", 75)]:
    Skill.objects.create(group=data_analytics, name=name, proficiency=pct)

ml = SkillGroup.objects.create(name="Machine Learning", track="da", order=4)
for name, pct in [("Scikit-learn", 78), ("Logistic Regression / Decision Trees", 78), ("Model Evaluation", 75)]:
    Skill.objects.create(group=ml, name=name, proficiency=pct)

databases = SkillGroup.objects.create(name="Databases", track="both", order=5)
for name, pct in [("MySQL", 80), ("PostgreSQL", 68), ("SQLite", 85)]:
    Skill.objects.create(group=databases, name=name, proficiency=pct)

tools = SkillGroup.objects.create(name="Tools & Platforms", track="both", order=6)
for name, pct in [("Git & GitHub", 85), ("VS Code", 90), ("Jupyter / Colab", 82), ("MySQL Workbench", 70)]:
    Skill.objects.create(group=tools, name=name, proficiency=pct)

# --------------------------------------------------------------------- #
# PROJECTS
# --------------------------------------------------------------------- #
Project.objects.all().delete()

Project.objects.create(
    title="AgriGro — Farm-to-Cart E-Commerce Platform",
    track="se",
    category="django",
    short_description="Full-stack Django e-commerce app with auth, catalog, cart, and search — deployed live on Render.",
    description=(
        "A complete farm-to-cart marketplace built from scratch using Django's MVT "
        "architecture. Covers the full flow a real e-commerce app needs: user "
        "registration and login, product browsing with category filters and search, "
        "a cart with quantity management, and an admin panel to manage the catalog."
    ),
    problem_statement="Most fresher portfolios show static clones. I wanted one real, deployed, working application with an actual database behind it.",
    features="User authentication and registration\nProduct catalog with category filtering\nQ-object based search\nCart with quantity management\nAdmin panel for catalog management\nCustom-styled, framework-free frontend",
    challenges="Hit a Pillow install issue, a 405 error on logout under Django 4.1+'s POST requirement for logout, and a UNIQUE constraint error during registration.",
    solutions="Fixed Pillow via correct system dependencies, switched the logout link to a POST-based form, and added proper validation to prevent duplicate accounts.",
    technologies="Python, Django, Django ORM, SQLite, HTML, CSS, JavaScript, Git, Render",
    github_url="https://github.com/Satyasai-Adabala/Agri_Gro-Django-Ecommerce",
    live_url="https://agri-gro-django-ecommerce.onrender.com",
    metric_label="Status",
    metric_value="Live on Render",
    featured=True,
    order=1,
    created_at="2025-06-01",
)

Project.objects.create(
    title="Employee Attrition Prediction — Machine Learning",
    track="both",
    category="ml",
    short_description="Compared 3 classification models on IBM HR data to predict employee attrition — 89.1% accuracy.",
    description=(
        "Built a complete ML pipeline on the IBM HR Analytics dataset (1,470 records, "
        "35 features): data cleaning, EDA, label encoding, feature selection, and "
        "standard scaling, followed by training and evaluating three classifiers."
    ),
    problem_statement="HR teams need to know which employees are at risk of leaving before it happens, not after.",
    features="End-to-end preprocessing pipeline\nLogistic Regression, Decision Tree, Random Forest models\nModel evaluation via confusion matrix, precision, recall, F1-score\nFeature importance analysis",
    challenges="Categorical features needed careful encoding, and class imbalance risked biasing accuracy toward the majority class.",
    solutions="Used label encoding plus standard scaling, and evaluated with precision/recall/F1 rather than accuracy alone.",
    technologies="Python, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn",
    github_url="https://github.com/Satyasai-Adabala/Employee-Attrition-Prediction-ML",
    metric_label="Best Accuracy",
    metric_value="89.1% (Logistic Regression)",
    featured=True,
    order=2,
    created_at="2025-07-01",
)

Project.objects.create(
    title="Retail Sales — Exploratory Data Analysis",
    track="da",
    category="data",
    short_description="End-to-end EDA on 12,575 retail transactions to find category, channel, and timing patterns.",
    description=(
        "Cleaned and validated a retail transaction dataset, then analyzed sales "
        "across categories, payment methods, and channels to surface patterns a "
        "business could act on."
    ),
    problem_statement="Raw transaction logs don't tell a retailer what to do differently next quarter.",
    features="Data cleaning and type validation\nCategory, payment method, and channel analysis\nIQR-based outlier detection\nCorrelation analysis for targeted recommendations",
    challenges="Distinguishing genuine high-value outliers from data entry errors in the transaction amounts.",
    solutions="Applied IQR-based outlier detection combined with category-specific context before deciding to keep or flag a record.",
    technologies="Python, Pandas, NumPy, Matplotlib, Seaborn",
    github_url="https://github.com/Satyasai-Adabala/retail-sales-eda",
    metric_label="Records analyzed",
    metric_value="12,575",
    order=3,
    created_at="2025-05-01",
)

Project.objects.create(
    title="Healthcare Appointment — Exploratory Data Analysis",
    track="da",
    category="data",
    short_description="Analyzed appointment records to explain why 51.5% of visits were cancelled or no-shows.",
    description=(
        "Engineered time-based features (month, day of week, hour) from healthcare "
        "appointment records to uncover scheduling patterns behind cancellations "
        "and no-shows."
    ),
    problem_statement="Clinics lose revenue and time to no-shows without knowing which slots or visit types are highest risk.",
    features="Time-based feature engineering\nDoctor-wise and hour-wise comparative analysis\nCross-tabulations and heatmaps\nScheduling recommendations",
    challenges="Therapy visits showed a disproportionately high no-show rate (35.71%), which needed isolating from the overall average to be useful.",
    solutions="Built doctor-wise and hour-wise breakdowns instead of a single aggregate no-show rate, making the pattern actionable.",
    technologies="Python, Pandas, NumPy, Matplotlib, Seaborn",
    github_url="https://github.com/Satyasai-Adabala/healthcare-appointment-eda",
    metric_label="No-show rate",
    metric_value="51.5% of records",
    order=4,
    created_at="2025-04-01",
)

Project.objects.create(
    title="E-Commerce Sales Dashboard — Power BI",
    track="da",
    category="bi",
    short_description="Interactive Power BI dashboard tracking sales, profit, and shipments across products and salespersons.",
    description=(
        "Built KPI cards, treemaps, matrix tables, and monthly trend visuals using "
        "DAX measures and Power Query transformations, comparing current-year vs "
        "previous-year performance."
    ),
    problem_statement="Sales leadership needed one view to compare performance across products, salespeople, and geography — not five spreadsheets.",
    features="KPI cards for sales, profit, profit %, shipment count\nTreemaps and matrix tables\nCurrent-year vs previous-year comparison\nCountry-wise sales distribution",
    challenges="Combining multiple data sources cleanly without duplicating rows during Power Query transformations.",
    solutions="Standardized the data model with proper relationships before writing DAX measures, avoiding double-counted totals.",
    technologies="Power BI, DAX, Power Query, Excel",
    github_url="https://github.com/Satyasai-Adabala/Ecommers_Power_Bi_Dashboard",
    metric_label="Top performers found",
    metric_value="Top 6 products & salespersons",
    order=5,
    created_at="2025-03-01",
)

# --------------------------------------------------------------------- #
# EXPERIENCE
# --------------------------------------------------------------------- #
Experience.objects.all().delete()

Experience.objects.create(
    role="Data Science Intern",
    organization="Dhaapps",
    track="da",
    start_date="2024",
    end_date="2024",
    responsibilities="Worked with real-world datasets using NumPy and Pandas.\nApplied fundamentals of EDA and machine learning using Python.\nCleaned and analyzed data to surface usable insights.",
    technologies="Python, NumPy, Pandas",
    order=1,
)

Experience.objects.create(
    role="Python Web Development Intern",
    organization="ICT Academy",
    track="se",
    start_date="2024",
    end_date="2024",
    responsibilities="Learned Python web development fundamentals and database integration.\nBuilt mini web applications from the ground up.",
    technologies="Python, Web Development, Databases",
    order=2,
)

# --------------------------------------------------------------------- #
# EDUCATION
# --------------------------------------------------------------------- #
Education.objects.all().delete()

Education.objects.create(
    degree="B.Tech — Electronics & Communication Engineering",
    institution="Bonam Venkata Chalamayya Engineering College, Odalarevu",
    start_year="2021",
    end_year="2025",
    score_label="CGPA",
    score_value="8.5",
    order=1,
)
Education.objects.create(
    degree="Higher Secondary Education (M.P.C)",
    institution="Sri Chaitanya Jr College, Razole",
    start_year="2019",
    end_year="2021",
    score_label="Percentage",
    score_value="87%",
    order=2,
)
Education.objects.create(
    degree="Secondary Education",
    institution="ZP High School, Katrenipadu",
    start_year="2018",
    end_year="2019",
    score_label="CGPA",
    score_value="9.8",
    order=3,
)

# --------------------------------------------------------------------- #
# CERTIFICATIONS
# --------------------------------------------------------------------- #
Certification.objects.all().delete()

certs = [
    ("Programming for Problem Solving using Python", "CodeTantra"),
    ("Python Web Development Internship", "ICT Academy"),
    ("Web Technologies & SQL", "HQL Edu-tech, APSCHE"),
    ("Python Full Stack Development", "IIDT Black Bucks, APSCHE"),
]
for i, (name, org) in enumerate(certs, start=1):
    Certification.objects.create(name=name, organization=org, order=i)

print("Done. Profile, skills, projects, experience, education, and certifications seeded.")
