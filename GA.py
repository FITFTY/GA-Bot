from google.analytics.data_v1beta.types import DateRange, Metric, Dimension, RunReportRequest
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from datetime import datetime, date
from datetime import timedelta
import secret
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

def getTodayDAU():
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=secret.GA_property,
        # 측정기준
        dimensions=[
        
        ],
        # 측정항목
        metrics=[
            Metric(name="activeUsers")
            ],
        date_ranges=[DateRange(start_date="1daysAgo", end_date="today")],
    )

    response = client.run_report(request)
    dau = 0
    for row in response.rows:
        dau = row.metric_values[0].value
     
    return dau

def getYesterdayDAU():
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=secret.GA_property,
        # 측정기준
        dimensions=[
        
        ],
        # 측정항목
        metrics=[
            Metric(name="activeUsers")
            ],
        date_ranges=[DateRange(start_date="2daysAgo", end_date="1daysAgo")],
    )

    response = client.run_report(request)
    dau = 0
    for row in response.rows:
        dau = row.metric_values[0].value
     
    return dau


def getTodayMAU():
    client = BetaAnalyticsDataClient()

    today = date.today()
    yesterday = today - timedelta(days=1)
    first_day_of_month = date(yesterday.year, yesterday.month, 1).isoformat()
    last_day_of_month = date(yesterday.year, yesterday.month, yesterday.day).isoformat()

    request = RunReportRequest(
        property=secret.GA_property,
        # 측정기준
        dimensions=[
        ],
        # 측정항목
        metrics=[
            Metric(name="activeUsers")
        ],
        date_ranges=[DateRange(start_date=first_day_of_month, end_date=last_day_of_month)],
    )

    response = client.run_report(request)
    mau = 0
    for row in response.rows:
        mau = row.metric_values[0].value
     
    return mau

def getYesterdayMAU():
    client = BetaAnalyticsDataClient()

    today = date.today()
    first_day_of_month = date(today.year, today.month, 1).isoformat()
    last_day_of_month = date(today.year, today.month, today.day).isoformat()

    request = RunReportRequest(
        property=secret.GA_property,
        # 측정기준
        dimensions=[
        ],
        # 측정항목
        metrics=[
            Metric(name="activeUsers")
        ],
        date_ranges=[DateRange(start_date=first_day_of_month, end_date=last_day_of_month)],
    )

    response = client.run_report(request)
    mau = 0
    for row in response.rows:
        mau = row.metric_values[0].value
     
    return mau

