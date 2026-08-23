from django.contrib import admin
from .models import (
    SiteProfile,
    SkillGroup,
    Skill,
    Project,
    Experience,
    Education,
    Certification,
    ContactMessage,
)


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "projects_completed", "certifications_count")

    def has_add_permission(self, request):
        return not SiteProfile.objects.exists()


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillGroup)
class SkillGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "track", "order")
    inlines = [SkillInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "track", "category", "featured", "order", "created_at")
    list_filter = ("track", "category", "featured")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "technologies")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "organization", "track", "start_date", "end_date", "order")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_year", "end_year", "order")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "date", "order")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read",)
    readonly_fields = ("name", "email", "subject", "message", "created_at")
