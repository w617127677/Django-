from rest_framework import serializers
from snippets.models import Ggooo
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ggooo
        fields = ('iq','公司','单位地址','行业性质','规模','性质','公司资产','职位名称','职位详细',
                  )
# 公司 = models.CharField(max_length=255, blank=True, null=True)
#     单位地址 = models.CharField(max_length=255, blank=True, null=True)
#     行业性质 = models.CharField(max_length=255, blank=True, null=True)
#     规模 = models.CharField(max_length=255, blank=True, null=True)
#     性质 = models.CharField(max_length=255, blank=True, null=True)
#     公司资产 = models.CharField(max_length=255, blank=True, null=True)
#     职位名称 = models.CharField(max_length=7000, blank=True, null=True)
#     职位详细