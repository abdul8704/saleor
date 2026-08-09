"""Combines the fraud rules into a single risk score."""

from .rules import is_high_value, is_mismatched_country


class FraudScorer:
    """Scores an order for fraud risk between 0.0 and 1.0."""

    def __init__(self, threshold=0.7):
        self.threshold = threshold

    def score(self, order):
        score = 0.0
        if is_high_value(order.total_gross_amount):
            score += 0.5
        if is_mismatched_country(order.billing_country, order.shipping_country):
            score += 0.4
        return min(score, 1.0)

    def should_block(self, order):
        return self.score(order) >= self.threshold
