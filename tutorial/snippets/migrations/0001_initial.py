# Generated by Django 2.2.5 on 2021-02-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Too',
            fields=[
                ('iq', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('ali_id', models.CharField(blank=True, db_column='ALI_ID', max_length=255, null=True)),
                ('省份', models.CharField(blank=True, max_length=255, null=True)),
                ('城市', models.CharField(blank=True, max_length=255, null=True)),
                ('行政区', models.CharField(blank=True, max_length=255, null=True)),
                ('标的物类型', models.CharField(blank=True, max_length=255, null=True)),
                ('标的物名称', models.CharField(blank=True, max_length=255, null=True)),
                ('拍卖次数', models.CharField(blank=True, max_length=255, null=True)),
                ('竞价周期', models.CharField(blank=True, max_length=255, null=True)),
                ('延时周期', models.CharField(blank=True, max_length=255, null=True)),
                ('保证金', models.CharField(blank=True, max_length=255, null=True)),
                ('优先购买权人', models.CharField(blank=True, max_length=255, null=True)),
                ('变卖预缴款', models.CharField(blank=True, max_length=255, null=True)),
                ('变卖价', models.CharField(blank=True, max_length=255, null=True)),
                ('变卖周期', models.CharField(blank=True, max_length=255, null=True)),
                ('监督单位', models.CharField(blank=True, max_length=255, null=True)),
                ('成交时间', models.CharField(blank=True, max_length=255, null=True)),
                ('交易类型', models.CharField(blank=True, max_length=255, null=True)),
                ('报名人数', models.CharField(blank=True, max_length=255, null=True)),
                ('出价次数', models.CharField(blank=True, max_length=255, null=True)),
                ('是否限购', models.CharField(blank=True, max_length=255, null=True)),
                ('抵押物名称', models.CharField(blank=True, max_length=255, null=True)),
                ('评估价格', models.CharField(blank=True, max_length=255, null=True)),
                ('信用', models.CharField(blank=True, max_length=255, null=True)),
                ('当前价格', models.CharField(blank=True, max_length=255, null=True)),
                ('延时次数', models.CharField(blank=True, max_length=255, null=True)),
                ('处置单位', models.CharField(blank=True, max_length=255, null=True)),
                ('结束时间', models.CharField(blank=True, max_length=255, null=True)),
                ('成交价格', models.CharField(blank=True, max_length=255, null=True)),
                ('初始价格', models.CharField(blank=True, max_length=255, null=True)),
                ('itemurl', models.CharField(blank=True, db_column='itemURL', max_length=255, null=True)),
                ('经度', models.CharField(blank=True, max_length=255, null=True)),
                ('纬度', models.CharField(blank=True, max_length=255, null=True)),
                ('市场价格', models.CharField(blank=True, max_length=255, null=True)),
                ('加价幅度', models.CharField(blank=True, max_length=255, null=True)),
                ('selloff', models.CharField(blank=True, db_column='sellOff', max_length=255, null=True)),
                ('起拍价格', models.CharField(blank=True, max_length=255, null=True)),
                ('开始时间', models.CharField(blank=True, max_length=255, null=True)),
                ('支持贷款', models.CharField(blank=True, max_length=255, null=True)),
                ('围观人数', models.CharField(blank=True, max_length=255, null=True)),
                ('交易状态', models.CharField(blank=True, max_length=255, null=True)),
                ('采集时间', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'too',
                'managed': False,
            },
        ),
    ]