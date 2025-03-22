from django.db import models

# Home Section
class CompanyProfile(models.Model):
    contracts_international_agencies = models.IntegerField()
    us_government_project = models.IntegerField()
    organizational_capacity_assessment = models.IntegerField()
    research_evaluation_assignments = models.IntegerField()
    years_of_experience = models.IntegerField()
    about_text = models.TextField()
    organization_development_text = models.TextField()
    organization_development_image = models.ImageField(upload_to='company_profile/')
    research_evaluation_text = models.TextField()
    research_evaluation_image = models.ImageField(upload_to='company_profile/')
    practice_caption = models.TextField()

    class Meta:
        verbose_name_plural = '                 Company Profile'

class HomeBanner(models.Model):
    image = models.ImageField(upload_to='home_banner/')
    caption = models.TextField()

    class Meta:
        verbose_name_plural = '                Home Banners'

class RecentProject(models.Model):
    assignment_name = models.CharField(max_length=255)
    assignment_start = models.DateField()
    assignment_end = models.DateField()
    assignment_with = models.CharField(max_length=255)
    assignment_description = models.TextField()
    assignment_photo = models.ImageField(upload_to='projects/', blank=True, null=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    class Meta:
        verbose_name_plural = '               Recent Projects'

class Testimonial(models.Model):
    statement = models.TextField()
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="testimonial_photo", null=True, blank=True)
    organization = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()

    class Meta:
        verbose_name_plural = '              Testimonials'

# About Us Section
class CoreCompetency(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '             Core Competencies'

class About(models.Model):
    about_text = models.TextField()
    our_mission = models.TextField()
    vision_text = models.TextField()
    integrity_text = models.TextField()
    commitment_text = models.TextField()
    ethical_text = models.TextField()
    inclusivity_text = models.TextField()
    core_value_text = models.TextField()
    company_profile = models.FileField(upload_to='company_profile_pdfs/')
    logo = models.ImageField(upload_to='logos/')
    company_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '             About Us'

class YearRange(models.Model):
    year_range = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.year_range
    
    class Meta:
        verbose_name_plural = '            Year Ranges'

class HistoryTimeline(models.Model):
    year_range = models.ForeignKey(YearRange, on_delete=models.CASCADE, related_name='timelines')
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='history_timeline/')

    def __str__(self):
        return f"{self.year_range} - {self.title}"
    
    class Meta:
        verbose_name_plural = '           History Timelines'

class StrategicPartner(models.Model):
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='partners/')
    company_name = models.CharField(max_length=255)
    company_website_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = '          Strategic Partners'

class SubServiceArea(models.Model):
    TYPE_CHOICES = [
        ('OD', 'Organization Development'),
        ('RE', 'Research & Evaluation')
    ]
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=2, choices=TYPE_CHOICES)
    description = models.TextField()
    images = models.ImageField(upload_to='subarea_images/', blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.category
    
    class Meta:
        verbose_name_plural = '         Sub Areas'

class Assignment(models.Model):
    
    TYPE_CHOICES = [
        ('', 'Select Type'),
        ('OD', 'Organization Development'),
        ('RE', 'Research & Evaluation')
    ]

    # SERVICE_TYPE_CHOICES = [
    #     ( 'Organizational Capacity Assesment', 'Organizational Capacity Assesment' ),
    #     ( 'Change Management', 'Change Management' ),
    #     ( 'Training & Facilitation', 'Training & Facilitation' ),
    #     ( 'Project Cycle Management', 'Project Cycle Management' ),
    #     ( 'ICT/MIS Development', 'ICT/MIS Development' ),
    #     ( 'Baseline & Program Evaluation', 'Baseline & Program Evaluation' ),
    #     ( 'Project Program Evaluation', 'Project Program Evaluation' ),
    #     ( 'Market Survey', 'Market Survey' ),
    #     ( 'Thematic Research', 'Thematic Research' ),
    #     ( 'Impact Assesment', 'Impact Assesment' ),
    #     ( 'Performance Studies', 'Performance Studies' ),
    #     ( 'Preception Studies', 'Preception Studies' ),
    # ]
    
    service_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    # sub_service = models.CharField(max_length=255, choices=SERVICE_TYPE_CHOICES)
    sub_service_area = models.ForeignKey(SubServiceArea, on_delete=models.CASCADE)
    practice_area = models.ForeignKey('PracticeArea', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    select_client = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='assignment_photos/')
    description = models.TextField()
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = '        Assignments'


class ServiceIntro(models.Model):
    intro_text = models.TextField()
    organization_development = models.TextField()
    organization_development_image = models.ImageField(upload_to='services/', blank=True, null=True)
    research_evaluation = models.TextField()
    research_evaluation_image = models.ImageField(upload_to='services/', blank=True, null=True)
    sub_areas = models.ManyToManyField(SubServiceArea)

    class Meta:
        verbose_name_plural = '       Service Intros'

# Practice Areas Section
class PracticeArea(models.Model):
    name = models.CharField(max_length=255, unique=True)
    introduction = models.TextField()
    image = models.ImageField(upload_to='practice_areas/', blank=True, null=True)
    logo = models.ImageField(upload_to='practice_areas/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '      Practice Areas'

# Our Team Section
class TeamMember(models.Model):
    CATEGORY_CHOICES = [
        ('Core Team', 'Core Team'),
        ('Technical Expert', 'Technical Expert'),
        ('International Consultant', 'International Consultant')
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='team_members/')
    priority = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = '     Team Members'

# Our Work & Reach Section
class MilestoneWork(models.Model):
    TYPE_CHOICES = [
        ('', 'Select Type'),
        ('OD', 'Organization Development'),
        ('RE', 'Research & Evaluation')
    ]

    service_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    # sub_service = models.CharField(max_length=255, choices=SERVICE_TYPE_CHOICES)
    sub_service_area = models.ForeignKey(SubServiceArea, on_delete=models.CASCADE)
    practice_area = models.ForeignKey('PracticeArea', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='assignment_photos/')
    description = models.TextField()
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = '        Milestones'

class WorkLocation(models.Model):
    SUBCONTINENT_CHOICES = [
        ('Africa', 'Africa'), ('Asia', 'Asia'), ('Europe', 'Europe'),
        ('North America', 'North America'), ('South America', 'South America'),
        ('Oceania', 'Oceania'), ('Middle East', 'Middle East'), ('Caribbean', 'Caribbean')
    ]
    subcontinent = models.CharField(max_length=50, choices=SUBCONTINENT_CHOICES)
    country = models.CharField(max_length=100)
    work_description = models.TextField()

    class Meta:
        verbose_name_plural = '   Work Locations'

class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    report_pdf = models.FileField(upload_to='reports/')

    class Meta:
        verbose_name_plural = 'Reports'

class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_photos/')
    content = models.TextField()
    category = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    tags = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Blog Posts'

# Request Form
class RequestForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = models.TextField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='request_forms', null=True, blank=True)

    class Meta:
        verbose_name_plural = '  Request Forms'

# Photo Gallery Section
class PhotoGallery(models.Model):
    caption = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photo_gallery/')

    class Meta:
        verbose_name_plural = 'Photo Gallery'

    def __str__(self):
        return self.caption

# Contact Section
class ContactDetail(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    email = models.EmailField()
    cell = models.CharField(max_length=20)
    website = models.URLField()

    class Meta:
        verbose_name_plural = 'Contact Details'
