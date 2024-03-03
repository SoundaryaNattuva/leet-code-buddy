from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

SMILES = (
  ('1', '😐'), #neutral
  ('2', '😃'), #happy
  ('3', '😍'), #very excited
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


# Create your models here.
class Application(models.Model):
  date = models.DateField('Application Submission Date')
  position = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  enthusiasm = models.CharField(max_length=1, choices=SMILES, default=SMILES[0][0] )
  workArrangement = models.CharField(max_length=1, choices=ARRANGEMENTS, default=ARRANGEMENTS[0][0])
  location = models.CharField(max_length=50)
  techstack = models.TextField(max_length=100)
  status = models.CharField(max_length=1, choices=STATUS, default=STATUS[0][0])
  minsalary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  maxsalary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  notes = models.TextField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.position