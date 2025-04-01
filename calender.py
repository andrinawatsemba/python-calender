import calendar
from datetime import datetime

def enhanced_calendar(year=None, month=None):
    """Enhanced calendar with current month as default"""
    if year is None or month is None:
        now = datetime.now()
        year, month = now.year, now.month
    
    # Create TextCalendar with Sunday as first day
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    # Display header
    month_name = calendar.month_name[month]
    print(f"\n{month_name} {year}".center(28))
    print("Su Mo Tu We Th Fr Sa")
    
    # Display calendar
    for week in cal.monthdayscalendar(year, month):
        week_str = []
        for day in week:
            if day == 0:
                week_str.append("  ")
            else:
                week_str.append(f"{day:2d}")
        print(" ".join(week_str))
    
    # Add some additional info
    days_in_month = calendar.monthrange(year, month)[1]
    print(f"\nTotal days: {days_in_month}")
    print(f"First day: {calendar.day_name[calendar.weekday(year, month, 1)]}")

# Example usage:
enhanced_calendar()  # Shows current month
enhanced_calendar(2024, 2)  # February 2024