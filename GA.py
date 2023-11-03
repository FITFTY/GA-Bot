from google.analytics.data_v1beta.types import DateRange, Metric, Dimension, RunReportRequest, RunRealtimeReportRequest
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from datetime import datetime, date
from datetime import timedelta
import secret
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

def getTodayDAU():
    client = BetaAnalyticsDataClient()

    request = RunRealtimeReportRequest(
        property=secret.GA_property,
        # 측정기준
        dimensions=[
        
        ],
        # 측정항목
        metrics=[
            Metric(name="activeUsers")
        ]
    )

    response = client.run_realtime_report(request)
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
        date_ranges=[DateRange(start_date="1daysAgo", end_date="1daysAgo")],
    )

    response = client.run_report(request)
    dau = 0
    for row in response.rows:
        dau = row.metric_values[0].value
     
    return dau


def getCurrentMonthMAU():
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
     
    return f"  {yesterday.month}월 누적 MAU: {mau}\n"

def getPrevicousMonthMAU():
    client = BetaAnalyticsDataClient()

    today = date.today()
    first_day_of_previous_month = today.replace(day=1) - timedelta(days=1)
    first_day_of_month = date(first_day_of_previous_month.year, first_day_of_previous_month.month, 1).isoformat()
    last_day_of_month = first_day_of_previous_month.isoformat()
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
     
    return f"  {first_day_of_previous_month.month}월 누적 MAU: {mau}\n"

def get30daysMonthMAU():
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
        date_ranges=[DateRange(start_date="30daysAgo", end_date="1daysAgo")],
    )

    response = client.run_report(request)
    mau = 0
    for row in response.rows:
        mau = row.metric_values[0].value
     
    return f"  최근 30일 MAU: {mau}\n"


def getTodayAverageSessionDuration():
    client = BetaAnalyticsDataClient()
    request = RunReportRequest(
        property=secret.GA_property,
        # 측정기준
        dimensions=[
            Dimension(name="unifiedScreenClass")
        ],
        # 측정항목
        metrics=[
           Metric(name="averageSessionDuration")
        ],
        date_ranges=[DateRange(start_date="today", end_date="today")],
    )

    response = client.run_report(request)
    
    mainVC_time = "  당일 메인화면 평균 체류시간: 0분 0초\n"
    settingVC_time = "  당일 설정화면 평균 체류시간: 0분 0초\n"
    for row in response.rows:
        if row.dimension_values[0].value == "MainView":
            mainVC_time = f"  당일 메인화면 평균 체류시간: {convertMinutes(row.metric_values[0].value)}\n"
        if row.dimension_values[0].value == "SettingViewController":
            settingVC_time = f"  당일 설정화면 평균 체류시간: {convertMinutes(row.metric_values[0].value)}\n"
    return mainVC_time + settingVC_time

def getYesterdayAverageSessionDuration():
    client = BetaAnalyticsDataClient()
    request = RunReportRequest(
        property=secret.GA_property,
        # 측정기준
        dimensions=[
            Dimension(name="unifiedScreenClass")
        ],
        # 측정항목
        metrics=[
           Metric(name="averageSessionDuration")
        ],
        date_ranges=[DateRange(start_date="1daysAgo", end_date="1daysAgo")],
    )

    response = client.run_report(request)
    mainVC_time = "  어제 메인화면 평균 체류시간: 0분 0초\n"
    settingVC_time = "  어제 설정화면 평균 체류시간: 0분 0초\n"
    for row in response.rows:
        if row.dimension_values[0].value == "MainView":
            mainVC_time = f"  어제 메인화면 평균 체류시간: {convertMinutes(row.metric_values[0].value)}\n"
        if row.dimension_values[0].value == "SettingViewController":
            settingVC_time = f"  어제 설정화면 평균 체류시간: {convertMinutes(row.metric_values[0].value)}"
    return mainVC_time + settingVC_time


def convertMinutes(value):
    num = int(float(value))
    return f"{num//60}분 {num%60}초"
   