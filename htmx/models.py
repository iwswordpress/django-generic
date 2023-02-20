from django.db import models
import uuid


class Team(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    team_name = models.CharField(max_length=50)
    def __str__(self):
        return self.team_name
