from django.db import models
from events.models import Event

FEEDBACK_CHOICES = [
    "N/A",
    "STRONGLY AGREE",
    "AGREE",
    "NEUTRAL",
    "DISAGREE",
    "STRONGLY DISAGREE",
]

# Create your models here.
class Feedback(models.Model):
    eventid = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    
for i in range(6):
        Feedback.add_to_class(f"talk_{i}", models.CharField(max_length=128))
        # self.fields[f"talk_{i}"] = models.CharField()
        # self.fields[f"useful_{i}"] = models.CharField(choices=FEEDBACK_CHOICES)
        # self.fields[f"relevant_{i}"] = models.CharField(choices=FEEDBACK_CHOICES)
        # self.fields[f"well_presented_{i}"] = models.CharField(choices=FEEDBACK_CHOICES)
        # self.fields[f"quality{i}"] = models.CharField(choices=FEEDBACK_CHOICES)
