from django.db import models
import requests

# Create your models here.
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    public_ip = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Fetch public IP only if it's not already set or on every save (based on use case)
        self.public_ip = self.fetch_public_ip()
        super().save(*args, **kwargs)

    @staticmethod
    def fetch_public_ip():
        try:
            response = requests.get('https://api.ipify.org/?format=json', timeout=5)
            if response.status_code == 200:
                return response.json().get('ip', 'Unknown')
        except requests.RequestException:
            pass
        return 'Unknown'

    class Meta:
        db_table = "category"