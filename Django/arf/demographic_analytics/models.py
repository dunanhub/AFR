from django.db import models
from django.conf import settings  # Используем AUTH_USER_MODEL

class UserAction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    action_time = models.DateTimeField(auto_now_add=True, verbose_name="Время действия")
    action_type = models.CharField(max_length=255, verbose_name="Тип действия")  # Например, "вход в систему"
    function_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Используемая функция")

    class Meta:
        verbose_name = "Действие пользователя"
        verbose_name_plural = "Действия пользователей"
        ordering = ['-action_time']

    def __str__(self):
        return f"{self.user} - {self.action_type} - {self.action_time}"