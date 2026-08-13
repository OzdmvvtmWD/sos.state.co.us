from django.db import models

class UCCRecord(models.Model):
    document = models.CharField(max_length=255, blank=True, null=True)
    document_link = models.CharField(max_length=255, blank=True, null=True)
    record = models.CharField(max_length=255, blank=True, null=True)
    record_link = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    lapse_date = models.CharField(max_length=255, blank=True, null=True)
    debtor = models.CharField(max_length=255, blank=True, null=True)
    secured_party = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "UCC record"
        verbose_name_plural = "UCC records"

    def __str__(self):
        return f"{self.document} — {self.debtor}"
