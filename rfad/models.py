from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, verbose_name="Раса")
    hits = models.PositiveIntegerField(verbose_name="ХП")
    mana = models.PositiveIntegerField(verbose_name="МП")
    stamina = models.PositiveIntegerField(verbose_name="СТ")
    hand_damage = models.PositiveIntegerField(verbose_name="Урон с руки")
    race_peculiarities = models.TextField(verbose_name="Особенности расы")
    skills = models.TextField(verbose_name="Бонус к навыкам")
    art = models.ImageField(upload_to='images',
                            verbose_name='Арт', blank=True)

    class Meta:
        verbose_name = "Раса"
        verbose_name_plural = "Расы"

    def __str__(self):
        return self.name
