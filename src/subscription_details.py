from datetime import *
from dateutil.relativedelta import *
from .price_details import price

class subscription:
    def __init__(self, date, category, plan):
        self.date = date
        self.category = category
        self.plan = plan

    def amount(self):
        amount = price[self.category][self.plan]["AMOUNT"]
        return amount

    def renewal_date(self):
        period = price[self.category][self.plan]["NOTIFICATION_PERIOD"]
        date = self.date+relativedelta(months=+period, days=-10)
        return date


class topup:
    def __init__(self, topup_type, topup_period):
        self.topup_type = topup_type
        self.topup_period = topup_period

    def amount(self):
        amount = price["TOPUP"][self.topup_type] * self.topup_period
        #print(type(price["TOPUP"][self.topup_type]), type(self.topup_period))
        return amount