from django.db import models
import datetime
from datetime import timedelta,date
# Create your models here.


class tables(models.Model):
    table_name = models.CharField(max_length=30, null=False, blank=True, unique=True)
    
    class Meta:
        ordering = ('table_name',)
        verbose_name_plural = 'Table names'
    def __str__(self):
        return f'{self.table_name}'
    
    @classmethod
    def create(cls, table_name):
        table_instance = cls(table_name=table_name)
        table_instance.save()
        return table_instance


class Items(models.Model):
    #table_name = models.CharField(max_length=30, null=True, blank=True)
    table = models.ForeignKey(tables, null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, null=False, blank=True)
    date = models.DateField()
    codes = models.CharField(max_length=200, null=True, blank = True)
    Bill_no = models.CharField(null=True, blank = True,max_length=200 )
    Items = models.CharField(max_length=200, null=True, blank = True,)
    Item_detail = models.CharField(max_length=200, null=True, blank = True )
    detail = models.CharField(max_length=200, null=True, blank = True )
    quantity = models.CharField(null=True, blank = True, max_length=200 )
    U_PRS_USD = models.FloatField(null=True, blank = True ) 	
    TOTAL_PRS_USD = models.FloatField(null=True, blank = True )
    U_PRS_DHS = models.FloatField(null=True, blank = True )
    S_PRS_dhs = models.FloatField(null=True, blank = True )
    LO_AND_PR = models.FloatField(null=True, blank = True )
    
    @classmethod
    def create(cls, table, item):
        item_instance = cls(table=table, 
                            date=item['date'],
                            codes=item['codes'],
                            Bill_no=item['bill_no'],
                            Items=item['itemes'],
                            Item_detail =item['item_detail'], 
                            detail=item['detail'], 
                            quantity=item['qty'], 
                            U_PRS_USD=item['U_PRS_USD'], 
                            TOTAL_PRS_USD=item['TOTAL_PRS_USD'],
                            U_PRS_DHS=item['U_PRS_DHS'], 
                            S_PRS_dhs=item['S_PRS_dhs'], 
                            LO_AND_PR=item['LO_AND_PR']) 
        item_instance.save()
        return item_instance
    
    def save(self, *args, **kwargs):
        if "Half" in self.Items:
            self.category = "Half"
        elif len(self.Items) > 15:
            self.category = "Complete"
        else:
            self.category = "Ordinary"
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('table','category')
        verbose_name_plural = 'Items table'

    def __str__(self):
        return f'{self.table} + {self.Items}' 