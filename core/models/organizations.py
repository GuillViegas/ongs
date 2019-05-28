from django.db import models
from django.contrib.postgres.fields import ArrayField

from lib.enum_choices import EnumChoices


class Address(models.Model):
    class Meta:
        verbose_name = 'Address: Address'
        verbose_name_plural = 'Address: Addresses'

    cep = models.CharField(max_length=9)
    location = models.CharField(max_length=150)
    number = models.CharField(max_length=10, null=True, blank=True)
    complement = models.CharField(max_length=256, null=True, blank=True)
    neighborhood = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

    def __str__(self):
        return 'Address #{}: {}, {} - {}'.format(self.id, self.city, self.state, self.location)


class Organization(models.Model):
    class ActionArea(EnumChoices):
        A_HEALTH = 0
        A_EDUCATION = 1
        A_SPORT = 2
        A_CULTURE = 3
        A_TECHNOLOGY = 5
        A_SUSTAINABILITY = 6
        A_COMMUNITY = 7
        A_ENVIROMENT = 8
        A_WOMEN = 9
        A_SENIORS = 10
        A_OTHERS = 11

        def __str__(self):
            ACTION_AREAS = [
                (self.A_HEALTH, 'Saúde'),
                (self.A_EDUCATION, 'Educação'),
                (self.A_SPORT, 'Esportes'),
                (self.A_CULTURE, 'Cultura'),
                (self.A_TECHNOLOGY, 'Tecnologia'),
                (self.A_SUSTAINABILITY, 'Sustentabilidade'),
                (self.A_COMMUNITY, 'Comunidade'),
                (self.A_ENVIROMENT, 'Meio Ambiente'),
                (self.A_WOMEN, 'Mulheres'),
                (self.A_SENIORS, 'Idosos'),
                (self.A_OTHERS, 'Outros'),
            ]

            return dict(ACTION_AREAS)[self]

    name = models.CharField(max_length=120, null=True, blank=True)
    site = models.CharField(max_length=100, null=True, blank=True)
    presentation = models.CharField(max_length=500, null=True, blank=True)
    phones = ArrayField(
        models.CharField(max_length=30, null=True, blank=True),
        size=3,
    )
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, related_name='organization', on_delete=models.CASCADE)
    action_area = models.IntegerField(choices=ActionArea.choices())
    logo_path = models.CharField(max_length=255)


class OrganizationMedia(models.Model):
    class MediaType(EnumChoices):
        MT_BLOG_SITE = 0
        MT_INSTAGRAM = 1
        MT_FACEBOOK = 2
        MT_TWITTER = 3
        MT_YOUTUBE = 4
        MT_OUTRO = 5

        def __str__(self):
                MEDIA_TYPE = [
                    (self.MT_BLOG_SITE, 'Blog/Site'),
                    (self.MT_INSTAGRAM, 'Instagram'),
                    (self.MT_FACEBOOK, 'Facebook'),
                    (self.MT_TWITTER, 'Twitter'),
                    (self.MT_YOUTUBE, 'Youtube'),
                    (self.MT_OUTRO, 'Outro'),
                ]

                return dict(MEDIA_TYPE)[self]

    organization = models.ForeignKey(Organization, related_name='medias', on_delete=models.CASCADE)
    media_type = models.IntegerField(choices=MediaType.choices())
    type_name = models.CharField(max_length=64, null=True, help_text='Used for type "other"', blank=True)
    address = models.CharField(max_length=512)