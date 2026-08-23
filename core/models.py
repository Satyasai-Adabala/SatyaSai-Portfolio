from django.db import models
from django.utils.text import slugify


TRACK_CHOICES = [
    ("se", "Software Engineer"),
    ("da", "Data Analyst"),
    ("both", "Both"),
]


class SiteProfile(models.Model):
    """Singleton-ish model holding the numbers and text that change often."""

    full_name = models.CharField(max_length=120, default="Adabala Satya Sai")
    location = models.CharField(max_length=120, default="Razole, Andhra Pradesh, India")
    email = models.EmailField(default="saiadabala53@gmail.com")
    phone = models.CharField(max_length=30, blank=True, default="+91 8008968188")
    github_url = models.URLField(default="https://github.com/Satyasai-Adabala")
    linkedin_url = models.URLField(default="https://linkedin.com/in/satya-sai-adabala-333687286")
    tagline_se = models.CharField(
        max_length=200, default="Python & Django Developer building things that ship."
    )
    tagline_da = models.CharField(
        max_length=200, default="Data Analyst turning raw numbers into decisions."
    )
    summary = models.TextField(
        default=(
            "Fresher engineering graduate who builds real, working software instead of "
            "tutorial clones - a live Django e-commerce platform, four end-to-end data "
            "projects, and a habit of shipping rather than just learning."
        )
    )
    resume_se = models.FileField(upload_to="resumes/", blank=True, null=True)
    resume_da = models.FileField(upload_to="resumes/", blank=True, null=True)

    projects_completed = models.PositiveIntegerField(default=5)
    technologies_count = models.PositiveIntegerField(default=18)
    internships_count = models.PositiveIntegerField(default=2)
    certifications_count = models.PositiveIntegerField(default=4)

    class Meta:
        verbose_name = "Site Profile"
        verbose_name_plural = "Site Profile"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SkillGroup(models.Model):
    name = models.CharField(max_length=80)
    track = models.CharField(max_length=6, choices=TRACK_CHOICES, default="both")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class Skill(models.Model):
    group = models.ForeignKey(SkillGroup, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    proficiency = models.PositiveIntegerField(
        default=70, help_text="0-100, keep it honest."
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("django", "Django / Web"),
        ("python", "Python"),
        ("data", "Data Analysis"),
        ("ml", "Machine Learning"),
        ("bi", "Business Intelligence"),
    ]

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    track = models.CharField(max_length=6, choices=TRACK_CHOICES, default="both")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="django")
    short_description = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    problem_statement = models.TextField(blank=True)
    features = models.TextField(blank=True, help_text="One feature per line.")
    challenges = models.TextField(blank=True)
    solutions = models.TextField(blank=True)
    technologies = models.CharField(
        max_length=300, help_text="Comma-separated, e.g. Python, Django, SQLite"
    )
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    metric_label = models.CharField(
        max_length=60, blank=True, help_text="e.g. 'Accuracy' or 'Records analyzed'"
    )
    metric_value = models.CharField(max_length=60, blank=True, help_text="e.g. '89.1%'")
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateField()

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def tech_list(self):
        return [t.strip() for t in self.technologies.split(",") if t.strip()]

    @property
    def feature_list(self):
        return [f.strip() for f in self.features.splitlines() if f.strip()]


class Experience(models.Model):
    role = models.CharField(max_length=120)
    organization = models.CharField(max_length=120)
    track = models.CharField(max_length=6, choices=TRACK_CHOICES, default="both")
    start_date = models.CharField(max_length=30, help_text="e.g. Jan 2025")
    end_date = models.CharField(max_length=30, default="Present")
    responsibilities = models.TextField(help_text="One point per line.")
    technologies = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.role} @ {self.organization}"

    @property
    def responsibility_list(self):
        return [r.strip() for r in self.responsibilities.splitlines() if r.strip()]

    @property
    def tech_list(self):
        return [t.strip() for t in self.technologies.split(",") if t.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    score_label = models.CharField(max_length=40, help_text="e.g. CGPA or Percentage")
    score_value = models.CharField(max_length=20, help_text="e.g. 8.5 or 87%")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certification(models.Model):
    name = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    date = models.CharField(max_length=30, blank=True)
    credential_url = models.URLField(blank=True)
    certificate_file = models.FileField(upload_to="certificates/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} - {self.name}"
