"""Persistence for fraud decisions."""

from django.db import models


class FraudDecision(models.Model):
    order_id = models.CharField(max_length=64, db_index=True)
    score = models.FloatField()
    blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
