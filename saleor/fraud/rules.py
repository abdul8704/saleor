"""Individual fraud signals, each scored independently."""

HIGH_VALUE_THRESHOLD = 1000


def is_high_value(order_total):
    return order_total >= HIGH_VALUE_THRESHOLD


def is_mismatched_country(billing_country, shipping_country):
    return billing_country != shipping_country
