from django.db import models

# Create your models here.
class Band(models.Model):

    '''A model of a Rock Band'''
    name = models.CharField(max_length=200)
    can_rock = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'band'
        verbose_name_plural = 'bands'

    def __str__(self):
        return self.name

    # count members by bands
    def get_members_count(self):
        return self.band.count()

    # retorna a url no formato /bands/1
    def get_band_detail_url(self):
        return self.id


class Member(models.Model):

    '''A model of a Rock band member'''
    INST = (
        ('g', 'Guitar'),
        ('b', 'Bass'),
        ('d', 'Drums'),
        ('v', 'Vocal'),
        ('p', 'Piano')
    )

    name = models.CharField("Member's name", max_length=200)
    instrument = models.CharField(choices=INST, max_length=1)
    band = models.ForeignKey("Band", related_name='band')

    class Meta:
        ordering = ['name']
        verbose_name = 'member'
        verbose_name_plural = 'members'

    def __str__(self):
        return self.name
