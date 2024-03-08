from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

SMILES = (
  ('1', '😐 Neutral'), #neutral
  ('2', '😃 Happy '), #happy
  ('3', '😍 Excited'), #very excited
)

ARRANGEMENTS = (
  ('R', 'Remote'),
  ('H', 'Hybrid'),
  ('O', 'On-site'),
)

STATUS = (
  ('A', 'Applied'),
  ('Y', 'Yet to Apply'),
  ('I', 'Interviewing'),
  ('N', 'Negotiating'),
  ('O', 'Accepted'),
  ('D', 'Decline'),
  ('R', 'Rejected'),
)

STATES = (
  ('AL', 'Alabama'),
  ('AK', 'Alaska'),
  ('AZ', 'Arizona'),
  ('AR', 'Arkansas'),
  ('CA', 'California'),
  ('CO', 'Colorado'),
  ('CT', 'Connecticut'),
  ('DE', 'Delaware'),
  ('FL', 'Florida'),
  ('GA', 'Georgia'),
  ('HI', 'Hawaii'),
  ('ID', 'Idaho'),
  ('IL', 'Illinois'),
  ('IN', 'Indiana'),
  ('IA', 'Iowa'),
  ('KS', 'Kansas'),
  ('KY', 'Kentucky'),
  ('LA', 'Louisiana'),
  ('ME', 'Maine'),
  ('MD', 'Maryland'),
  ('MA', 'Massachusetts'),
  ('MI', 'Michigan'),
  ('MN', 'Minnesota'),
  ('MS', 'Mississippi'),
  ('MO', 'Missouri'),
  ('MT', 'Montana'),
  ('NE', 'Nebraska'),
  ('NV', 'Nevada'),
  ('NH', 'New Hampshire'),
  ('NJ', 'New Jersey'),
  ('NM', 'New Mexico'),
  ('NY', 'New York'),
  ('NC', 'North Carolina'),
  ('ND', 'North Dakota'),
  ('OH', 'Ohio'),
  ('OK', 'Oklahoma'),
  ('OR', 'Oregon'),
  ('PA', 'Pennsylvania'),
  ('RI', 'Rhode Island'),
  ('SC', 'South Carolina'),
  ('SD', 'South Dakota'),
  ('TN', 'Tennessee'),
  ('TX', 'Texas'),
  ('UT', 'Utah'),
  ('VT', 'Vermont'),
  ('VA', 'Virginia'),
  ('WA', 'Washington'),
  ('WV', 'West Virginia'),
  ('WI', 'Wisconsin'),
  ('WY', 'Wyoming')
)

TYPES = (
  ('R','Referal'),
  ('C','Company Portal'),
  ('L','LinkedIn'),
  ('M','Monster'),
  ('G','Glassdoor'),
  ('L','LinkUp'),
  ('S','SimplyHired'),
  ('Z','ZipRecruiter'),
  ('I','Indeed'),
)

INTERVIEWTYPES = (
  ('P', 'Phone Screen'),
  ('T', 'Technical'),
  ('C', 'Cultural-Fit'),
  ('O', 'On-Site'),
  ('S', 'System-Design'),
  ('C', 'Code-Review'),
)

# Create your models here.
class Application(models.Model):
  app_date = models.DateField('Application Submission Date', null=False, blank=True)
  position = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  enthusiasm = models.CharField(max_length=1, choices=SMILES, default=SMILES[0][0] )
  work_arrangement = models.CharField('Work Arrangement', max_length=1, choices=ARRANGEMENTS, default=ARRANGEMENTS[0][0])
  state = models.CharField(max_length=2, choices=STATES, default=STATES[0][0])
  city = models.CharField(max_length=50)
  techstack = models.TextField('Technology Stack', max_length=100)
  status = models.CharField(max_length=1, choices=STATUS, default=STATUS[0][0])
  minsalary = models.DecimalField('Minimum Salary',max_digits=10, decimal_places=2, null=True, blank=True)
  maxsalary = models.DecimalField('Maximum Salary', max_digits=10, decimal_places=2, null=True, blank=True)
  notes = models.TextField(max_length=1000)
  application_type = models.CharField(max_length=1, choices=TYPES, default=TYPES[0][0])
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.position
  
  def get_absolute_url(self):
    return reverse('app-detail', kwargs={'app_id': self.id})
  
class Interview(models.Model):
  date = models.DateField('Interview Date', null=False, blank=True)
  interviewType = models.CharField('Interview Type',
    max_length=1,
    choices=INTERVIEWTYPES,
    default=INTERVIEWTYPES[0][0]
  )
  notes = models.TextField(max_length=100, default="")
  app = models.ForeignKey(Application, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_interviewType_display()} on {self.date}"
  
  class Meta: 
    ordering = ['-date']


class CoverLetter(models.Model):
  cl_date = models.DateField('Date', null=False, blank=True)
  position = models.CharField('Title', max_length=50, null=False, blank=True)
  letter = models.TextField('Cover Letter', max_length=2500, null=False, blank=True)
  tags = models.CharField('Tags', max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.position
  
  def get_absolute_url(self):
    return reverse('cl-detail', kwargs={'cl_id': self.id})
  
class Document(models.Model):
  url = models.CharField(max_length=250)
  cl = models.ForeignKey(CoverLetter, on_delete=models.CASCADE)

  def __str__(self):
    return f"Document for cl_id: {self.cl_id} @{self.url}"
  
