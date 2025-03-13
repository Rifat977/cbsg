from django.db import models

# Home Section
class CompanyProfile(models.Model):
    contracts_international_agencies = models.IntegerField()
    us_government_project = models.IntegerField()
    organizational_capacity_assessment = models.IntegerField()
    research_evaluation_assignments = models.IntegerField()
    years_of_experience = models.IntegerField()
    about_text = models.TextField(max_length=200)
    od_text = models.TextField(max_length=300)
    od_image = models.ImageField(upload_to='company_profile/')
    re_text = models.TextField()
    re_image = models.ImageField(upload_to='company_profile/')
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
    assignment_description = models.TextField(max_length=200)
    assignment_photo = models.ImageField(upload_to='projects/', blank=True, null=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    class Meta:
        verbose_name_plural = '               Recent Projects'

class Testimonial(models.Model):
    statement = models.TextField(max_length=150)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()

    class Meta:
        verbose_name_plural = '              Testimonials'

# About Us Section
class CoreCompetency(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '             Core Competencies'

class About(models.Model):
    about_text = models.TextField(max_length=200)
    our_mission_text = models.TextField(max_length=200)
    vision_text = models.TextField(max_length=200)
    integrity_text = models.TextField(max_length=80)
    commitment_text = models.TextField(max_length=80)
    ethical_text = models.TextField(max_length=80)
    inclusivity_text = models.TextField(max_length=80)
    core_competencies = models.ManyToManyField(CoreCompetency)
    company_profile = models.FileField(upload_to='company_profile_pdfs/')
    logo = models.ImageField(upload_to='logos/')
    company_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '             About Us'

class YearRange(models.Model):
    year_range = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.year_range
    
    class Meta:
        verbose_name_plural = '            Year Ranges'

class HistoryTimeline(models.Model):
    year_range = models.ForeignKey(YearRange, on_delete=models.CASCADE, related_name='timelines')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='history_timeline/')

    def __str__(self):
        return f"{self.year_range} - {self.title}"
    
    class Meta:
        verbose_name_plural = '           History Timelines'

class StrategicPartner(models.Model):
    description = models.TextField()
    logo = models.ImageField(upload_to='partners/')
    company_name = models.CharField(max_length=255)
    company_website_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = '          Strategic Partners'

class SubArea(models.Model):
    TYPE_CHOICES = [
        ('OD', 'Organization Development'),
        ('RE', 'Research & Evaluation')
    ]
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=2, choices=TYPE_CHOICES)
    description = models.TextField(max_length=200)
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

    SERVICE_TYPE_CHOICES = [
        ( 'Organizational Capacity Assesment', 'Organizational Capacity Assesment' ),
        ( 'Change Management', 'Change Management' ),
        ( 'Training & Facilitation', 'Training & Facilitation' ),
        ( 'Project Cycle Management', 'Project Cycle Management' ),
        ( 'ICT/MIS Development', 'ICT/MIS Development' ),
        ( 'Baseline & Program Evaluation', 'Baseline & Program Evaluation' ),
        ( 'Project Program Evaluation', 'Project Program Evaluation' ),
        ( 'Market Survey', 'Market Survey' ),
        ( 'Thematic Research', 'Thematic Research' ),
        ( 'Impact Assesment', 'Impact Assesment' ),
        ( 'Performance Studies', 'Performance Studies' ),
        ( 'Preception Studies', 'Preception Studies' ),
    ]
    
    service_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    sub_service = models.CharField(max_length=255, choices=SERVICE_TYPE_CHOICES)
    practice_area = models.ForeignKey('PracticeArea', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='assignment_photos/')
    description = models.TextField(max_length=300)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = '        Assignments'


class ServiceIntro(models.Model):
    intro_text = models.TextField(max_length=150)
    organization_development = models.TextField(max_length=100)
    organization_development_image = models.ImageField(upload_to='services/', blank=True, null=True)
    research_evaluation = models.TextField(max_length=100)
    research_evaluation_image = models.ImageField(upload_to='services/', blank=True, null=True)
    sub_areas = models.ManyToManyField(SubArea)

    class Meta:
        verbose_name_plural = '       Service Intros'

# Practice Areas Section
class PracticeArea(models.Model):
    name = models.CharField(max_length=255, unique=True)
    introduction = models.TextField(max_length=200)
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
    description = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='team_members/')

    class Meta:
        verbose_name_plural = '     Team Members'

# Our Work & Reach Section
class MilestoneWork(models.Model):
    TYPE_CHOICES = [
        ('', 'Select Type'),
        ('OD', 'Organization Development'),
        ('RE', 'Research & Evaluation')
    ]

    SERVICE_TYPE_CHOICES = [
        ( 'Organizational Capacity Assesment', 'Organizational Capacity Assesment' ),
        ( 'Change Management', 'Change Management' ),
        ( 'Training & Facilitation', 'Training & Facilitation' ),
        ( 'Project Cycle Management', 'Project Cycle Management' ),
        ( 'ICT/MIS Development', 'ICT/MIS Development' ),
        ( 'Baseline & Program Evaluation', 'Baseline & Program Evaluation' ),
        ( 'Project Program Evaluation', 'Project Program Evaluation' ),
        ( 'Market Survey', 'Market Survey' ),
        ( 'Thematic Research', 'Thematic Research' ),
        ( 'Impact Assesment', 'Impact Assesment' ),
        ( 'Performance Studies', 'Performance Studies' ),
        ( 'Preception Studies', 'Preception Studies' ),
    ]
    
    service_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    sub_service = models.CharField(max_length=255, choices=SERVICE_TYPE_CHOICES)
    practice_area = models.ForeignKey('PracticeArea', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='assignment_photos/')
    description = models.TextField(max_length=300)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

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
    work_description = models.TextField(max_length=50)

    class Meta:
        verbose_name_plural = '   Work Locations'

# Request Form
class RequestForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        verbose_name_plural = '  Request Forms'

# Photo Gallery Section
class PhotoGallery(models.Model):
    caption = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photo_gallery/')

    class Meta:
        verbose_name_plural = ' Photo Gallery'

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
