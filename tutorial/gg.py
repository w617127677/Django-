import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [1,2,3,4]
# plt.plot(x,y)
plt.scatter(x,y)
plt.show()# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ggooo(models.Model):
    ��˾ = models.CharField(max_length=255, blank=True, null=True)
    ��λ��ַ = models.CharField(max_length=255, blank=True, null=True)
    ��ҵ���� = models.CharField(max_length=255, blank=True, null=True)
    ��ģ = models.CharField(max_length=255, blank=True, null=True)
    ���� = models.CharField(max_length=255, blank=True, null=True)
    ��˾�ʲ� = models.CharField(max_length=255, blank=True, null=True)
    ְλ���� = models.CharField(max_length=7000, blank=True, null=True)
    ְλ��ϸ = models.CharField(max_length=7000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ggooo'
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
    ��˾ = models.CharField(max_length=255, blank=True, null=True)
    ��λ��ַ = models.CharField(max_length=255, blank=True, null=True)
    ��ҵ���� = models.CharField(max_length=255, blank=True, null=True)
    ��ģ = models.CharField(max_length=255, blank=True, null=True)
    ���� = models.CharField(max_length=255, blank=True, null=True)
    ��˾�ʲ� = models.CharField(max_length=255, blank=True, null=True)
    ְλ���� = models.CharField(max_length=7000, blank=True, null=True)
    ְλ��ϸ = models.CharField(max_length=7000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ggooo'
