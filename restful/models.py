from django.db import models

class GameUserInfo(models.Model):
    user_id = models.CharField(max_length=30)
    user_password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_id
    

class Ranking(models.Model):
    user_id = models.ForeignKey(GameUserInfo, on_delete=models.CASCADE)
    clear_time = models.DecimalField(max_digits=10, decimal_places=3, null=False, blank=False)

    def __str__(self):
        return str(self.clear_time)



