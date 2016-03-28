from __future__ import unicode_literals
from django.db import models


class StockIndex(models.Model):
    symbol = models.CharField(max_length=16,unique=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.symbol

    def get_market_cap(self):
        market_cap = 0.0 
        for equity in equity_set:
            market_cap += equity.price * equity.number
        return market_cap


class Equity(models.Model):
    stockindex = models.ForeignKey(StockIndex, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=16,unique=True)
    price = models.FloatField(default=0.0)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.symbol
