from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404

from .models import Project, SkillGroup, Experience, Education, Certification, SiteProfile
from .forms import ContactForm


def home(request):
    profile = SiteProfile.load()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                send_mail(
                    subject=f"Portfolio contact: {form.cleaned_data['subject']}",
                    message=(
                        f"From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n"
                        f"{form.cleaned_data['message']}"
                    ),
                    from_email=settings.EMAIL_HOST_USER or "noreply@portfolio.local",
                    recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, "Message sent - thanks for reaching out, I'll reply soon.")
            return redirect("home")
    else:
        form = ContactForm()

    context = {
        "profile": profile,
        "projects": Project.objects.all(),
        "featured_projects": Project.objects.filter(featured=True),
        "skill_groups": SkillGroup.objects.prefetch_related("skills"),
        "experiences": Experience.objects.all(),
        "education": Education.objects.all(),
        "certifications": Certification.objects.all(),
        "form": form,
    }
    return render(request, "home.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related = Project.objects.exclude(slug=slug).filter(category=project.category)[:3]
    return render(
        request,
        "project_detail.html",
        {"project": project, "related": related},
    )
