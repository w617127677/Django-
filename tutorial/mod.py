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
    省份 = models.CharField(max_length=255, blank=True, null=True)
    城市 = models.CharField(max_length=255, blank=True, null=True)
    行政区 = models.CharField(max_length=255, blank=True, null=True)
    标的物类型 = models.CharField(max_length=255, blank=True, null=True)
    标的物名称 = models.CharField(max_length=255, blank=True, null=True)
    拍卖次数 = models.CharField(max_length=255, blank=True, null=True)
    竞价周期 = models.CharField(max_length=255, blank=True, null=True)
    延时周期 = models.CharField(max_length=255, blank=True, null=True)
    保证金 = models.CharField(max_length=255, blank=True, null=True)
    优先购买权人 = models.CharField(max_length=255, blank=True, null=True)
    变卖预缴款 = models.CharField(max_length=255, blank=True, null=True)
    变卖价 = models.CharField(max_length=255, blank=True, null=True)
    变卖周期 = models.CharField(max_length=255, blank=True, null=True)
    监督单位 = models.CharField(max_length=255, blank=True, null=True)
    成交时间 = models.CharField(max_length=255, blank=True, null=True)
    交易类型 = models.CharField(max_length=255, blank=True, null=True)
    报名人数 = models.CharField(max_length=255, blank=True, null=True)
    出价次数 = models.CharField(max_length=255, blank=True, null=True)
    是否限购 = models.CharField(max_length=255, blank=True, null=True)
    抵押物名称 = models.CharField(max_length=255, blank=True, null=True)
    评估价格 = models.CharField(max_length=255, blank=True, null=True)
    信用 = models.CharField(max_length=255, blank=True, null=True)
    当前价格 = models.CharField(max_length=255, blank=True, null=True)
    延时次数 = models.CharField(max_length=255, blank=True, null=True)
    处置单位 = models.CharField(max_length=255, blank=True, null=True)
    结束时间 = models.CharField(max_length=255, blank=True, null=True)
    成交价格 = models.CharField(max_length=255, blank=True, null=True)
    初始价格 = models.CharField(max_length=255, blank=True, null=True)
    itemurl = models.CharField(db_column='itemURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    经度 = models.CharField(max_length=255, blank=True, null=True)
    纬度 = models.CharField(max_length=255, blank=True, null=True)
    市场价格 = models.CharField(max_length=255, blank=True, null=True)
    加价幅度 = models.CharField(max_length=255, blank=True, null=True)
    selloff = models.CharField(db_column='sellOff', max_length=255, blank=True, null=True)  # Field name made lowercase.
    起拍价格 = models.CharField(max_length=255, blank=True, null=True)
    开始时间 = models.CharField(max_length=255, blank=True, null=True)
    支持贷款 = models.CharField(max_length=255, blank=True, null=True)
    围观人数 = models.CharField(max_length=255, blank=True, null=True)
    交易状态 = models.CharField(max_length=255, blank=True, null=True)
    采集时间 = models.CharField(max_length=255, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'too'
