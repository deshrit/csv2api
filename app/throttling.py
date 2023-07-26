from rest_framework.throttling import UserRateThrottle


class CSVRateThrottle(UserRateThrottle):
    scope = "csv"
