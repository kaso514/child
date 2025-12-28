from django.shortcuts import render
from django.utils import timezone

def current_datetime(request):
    """显示当前日期和时间的视图"""
    now = timezone.now()
    context = {
        'current_date': now.strftime('%Y年%m月%d日'),
        'current_time': now.strftime('%H:%M:%S'),
        'weekday': now.strftime('%A'),
        'full_datetime': now.strftime('%Y-%m-%d %H:%M:%S'),
    }
    return render(request, 'datetime_app/index.html', context)