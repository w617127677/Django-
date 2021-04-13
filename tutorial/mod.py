# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Too(models.Model):
    iq = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    ali_id = models.CharField(db_column='ALI_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ʡ�� = models.CharField(max_length=255, blank=True, null=True)
    ���� = models.CharField(max_length=255, blank=True, null=True)
    ������ = models.CharField(max_length=255, blank=True, null=True)
    ��������� = models.CharField(max_length=255, blank=True, null=True)
    ��������� = models.CharField(max_length=255, blank=True, null=True)
    �������� = models.CharField(max_length=255, blank=True, null=True)
    �������� = models.CharField(max_length=255, blank=True, null=True)
    ��ʱ���� = models.CharField(max_length=255, blank=True, null=True)
    ��֤�� = models.CharField(max_length=255, blank=True, null=True)
    ���ȹ���Ȩ�� = models.CharField(max_length=255, blank=True, null=True)
    ����Ԥ�ɿ� = models.CharField(max_length=255, blank=True, null=True)
    ������ = models.CharField(max_length=255, blank=True, null=True)
    �������� = models.CharField(max_length=255, blank=True, null=True)
    �ල��λ = models.CharField(max_length=255, blank=True, null=True)
    �ɽ�ʱ�� = models.CharField(max_length=255, blank=True, null=True)
    �������� = models.CharField(max_length=255, blank=True, null=True)
    �������� = models.CharField(max_length=255, blank=True, null=True)
    ���۴��� = models.CharField(max_length=255, blank=True, null=True)
    �Ƿ��޹� = models.CharField(max_length=255, blank=True, null=True)
    ��Ѻ������ = models.CharField(max_length=255, blank=True, null=True)
    �����۸� = models.CharField(max_length=255, blank=True, null=True)
    ���� = models.CharField(max_length=255, blank=True, null=True)
    ��ǰ�۸� = models.CharField(max_length=255, blank=True, null=True)
    ��ʱ���� = models.CharField(max_length=255, blank=True, null=True)
    ���õ�λ = models.CharField(max_length=255, blank=True, null=True)
    ����ʱ�� = models.CharField(max_length=255, blank=True, null=True)
    �ɽ��۸� = models.CharField(max_length=255, blank=True, null=True)
    ��ʼ�۸� = models.CharField(max_length=255, blank=True, null=True)
    itemurl = models.CharField(db_column='itemURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ���� = models.CharField(max_length=255, blank=True, null=True)
    γ�� = models.CharField(max_length=255, blank=True, null=True)
    �г��۸� = models.CharField(max_length=255, blank=True, null=True)
    �Ӽ۷��� = models.CharField(max_length=255, blank=True, null=True)
    selloff = models.CharField(db_column='sellOff', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ���ļ۸� = models.CharField(max_length=255, blank=True, null=True)
    ��ʼʱ�� = models.CharField(max_length=255, blank=True, null=True)
    ֧�ִ��� = models.CharField(max_length=255, blank=True, null=True)
    Χ������ = models.CharField(max_length=255, blank=True, null=True)
    ����״̬ = models.CharField(max_length=255, blank=True, null=True)
    �ɼ�ʱ�� = models.CharField(max_length=255, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'too'
