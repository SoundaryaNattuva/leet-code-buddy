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

# Create your models here.
class Application(models.Model):
  date = models.DateField('Application Submission Date', null=False, blank=True)
  position = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  enthusiasm = models.CharField(max_length=1, choices=SMILES, default=SMILES[0][0] )
  workArrangement = models.CharField('Work Arrangement', max_length=1, choices=ARRANGEMENTS, default=ARRANGEMENTS[0][0])
  state = models.CharField(max_length=2, choices=STATES, default=STATES[0][0])
  city = models.CharField(max_length=50)
  techstack = models.TextField('Technology Stack', max_length=100)
  status = models.CharField(max_length=1, choices=STATUS, default=STATUS[0][0])
  minsalary = models.DecimalField('Minimum Salary',max_digits=10, decimal_places=2, null=True, blank=True)
  maxsalary = models.DecimalField('Maximum Salary', max_digits=10, decimal_places=2, null=True, blank=True)
  notes = models.TextField(max_length=1000)

  def __str__(self):
    return self.position
  
  def get_absolute_url(self):
    return reverse('app-detail', kwargs={'app_id': self.id})