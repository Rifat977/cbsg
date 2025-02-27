from django.db import models

# -------------------------- HOME -------------------------- #

class HomeBanner(models.Model):
    image = models.ImageField(upload_to='banners/')

    class Meta:
        verbose_name = "  Home - Banner"

    def __str__(self):
        return f"Banner {self.id}"

class RecentProject(models.Model):
    assignment_name = models.CharField(max_length=255)
    contract_duration = models.CharField(max_length=255)
    contract_with = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='projects/')
    logo = models.ImageField(upload_to='logos/')

    class Meta:
        verbose_name = "  Home - Recent Project"

    def __str__(self):
        return self.assignment_name

class Testimonial(models.Model):
    statement = models.TextField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

    class Meta:
        verbose_name = "  Home - Testimonial"

    def __str__(self):
        return f"Testimonial from {self.name}"

class WorkLocation(models.Model):
    country = models.CharField(max_length=50)
    work_description = models.TextField(max_length=50)

    class Meta:
        verbose_name = "  Home - Work Location"

    def __str__(self):
        return self.country

# -------------------------- ABOUT US -------------------------- #

class CoreCompetency(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=100)

    class Meta:
        verbose_name = "   About - Core Competency"

    def __str__(self):
        return self.name

class About(models.Model):
    about_text = models.TextField(max_length=200)
    core_competencies = models.ManyToManyField(CoreCompetency)
    company_profile = models.FileField(upload_to='company_profile/')
    logo = models.ImageField(upload_to='logos/')
    company_name = models.CharField(max_length=50)
    partnership_area = models.CharField(max_length=50)

    class Meta:
        verbose_name = "   About - About Us"

    def __str__(self):
        return "About Us"

# -------------------------- OUR SERVICES -------------------------- #

class SubArea(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=100)
    images = models.ImageField(upload_to='subareas/', blank=True, null=True)

    class Meta:
        verbose_name = "    Services - Sub Area"

    def __str__(self):
        return self.name

class Service(models.Model):
    intro_text = models.TextField(max_length=150)
    organization_development = models.TextField(max_length=100)
    research_evaluation = models.TextField(max_length=100)
    sub_areas = models.ManyToManyField(SubArea)

    class Meta:
        verbose_name = "    Services - Our Services"

    def __str__(self):
        return "Our Services"

# -------------------------- PRACTICE AREAS -------------------------- #

class PracticeArea(models.Model):
    name = models.CharField(max_length=255)
    introduction = models.TextField(max_length=100)
    image = models.ImageField(upload_to='practice_areas/', blank=True, null=True)
    logo = models.ImageField(upload_to='practice_areas_logos/', blank=True, null=True)

    class Meta:
        verbose_name = "     Practice Areas"

    def __str__(self):
        return self.name

class MilestoneWork(models.Model):
    practice_area = models.ForeignKey(PracticeArea, on_delete=models.CASCADE)
    description = models.TextField(max_length=50)
    image = models.ImageField(upload_to='milestones/')

    class Meta:
        verbose_name = "     Practice Areas - Milestone Work"

    def __str__(self):
        return f"Milestone in {self.practice_area.name}"

# -------------------------- OUR TEAM -------------------------- #

class TeamMember(models.Model):
    category = models.CharField(
        max_length=50,
        choices=[
            ("Core Team", "Core Team"),
            ("Technical Expert", "Technical Expert"),
            ("International Consultant", "International Consultant"),
        ]
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='team/')

    class Meta:
        verbose_name = "      Our Team"

    def __str__(self):
        return f"{self.name} ({self.category})"

# -------------------------- OUR WORK & REACH -------------------------- #

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='assignments/')
    client_logo = models.ImageField(upload_to='client_logos/')

    class Meta:
        verbose_name = "       Our Work - Assignment"

    def __str__(self):
        return self.name

class WorkReach(models.Model):
    introduction = models.TextField(max_length=100)
    highlight_assignments = models.ManyToManyField(Assignment)
    country = models.CharField(max_length=30)
    assignment_name = models.CharField(max_length=50)
    assignment_photo = models.ImageField(upload_to='work_reach/')

    class Meta:
        verbose_name = "       Our Work - Work Reach"

    def __str__(self):
        return f"Work in {self.country}"

# -------------------------- OUR PRODUCTS -------------------------- #

class Product(models.Model):
    report_name = models.CharField(max_length=50)
    report_summary = models.TextField(max_length=100)
    report_cover = models.ImageField(upload_to='reports/')
    report_file = models.FileField(upload_to='reports/')

    class Meta:
        verbose_name = "        Our Products"

    def __str__(self):
        return self.report_name

# -------------------------- REQUEST FORM -------------------------- #
class RequestForm(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="requests")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "         Request Form"

    def __str__(self):
        return f"Request from {self.name} for {self.product.report_name}"

# -------------------------- PHOTO GALLERY -------------------------- #

class PhotoGallery(models.Model):
    caption = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='gallery/')

    class Meta:
        verbose_name = "          Photo Gallery"

    def __str__(self):
        return self.caption

# -------------------------- CONTACT -------------------------- #

class Contact(models.Model):
    location_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='contact/')

    class Meta:
        verbose_name = "           Contact"

    def __str__(self):
        return self.location_name
