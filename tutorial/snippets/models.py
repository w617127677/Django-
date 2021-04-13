# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ggooo(models.Model):
    iq = models.AutoField(primary_key=True)
    公司 = models.CharField(max_length=255, blank=True, null=True)
    单位地址 = models.CharField(max_length=255, blank=True, null=True)
    行业性质 = models.CharField(max_length=255, blank=True, null=True)
    规模 = models.CharField(max_length=255, blank=True, null=True)
    性质 = models.CharField(max_length=255, blank=True, null=True)
    公司资产 = models.CharField(max_length=255, blank=True, null=True)
    职位名称 = models.CharField(max_length=7000, blank=True, null=True)
    职位详细 = models.CharField(max_length=7000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ggooo'