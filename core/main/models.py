from distutils.command.upload import upload
from django.db import models

# Create your models here.

class HomeBackGroud(models.Model):
    name = models.CharField('HomeBackGroud anun',max_length=20,null=True)
    name2 = models.CharField('HomeBackGroud anun2',max_length=20,null=True)
    about = models.TextField('HomeBackGroud about',null=True)
    img = models.ImageField('HomeBackGroud img',upload_to= 'media',null=True)
    text = models.TextField('HomeBackGroud text detali hamar',null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeBackGroud'
        verbose_name_plural = 'HomeBackGrouds'


class ArkacayinTurizm(models.Model):
        name = models.CharField('ArkacayinTurizm anun',max_length=20,null=True)
        text = models.TextField('ArkacayinTurizm text detali hamar',null=True)
        about = models.TextField('ArkacayinTurizm about',null=True)
        img = models.ImageField('ArkacayinTurizm img',upload_to= 'media',null=True)
        img2 = models.ImageField('ArkacayinTurizm  detal img',upload_to= 'media',null=True)


        def __str__(self):
            return self.name
        class Meta:
            verbose_name = 'ArkacayinTurizm'
            verbose_name_plural = 'ArkacayinTurizmner'


class Kayqimasin(models.Model):
    name = models.CharField('Kayqimasin anun',max_length=40)
    about = models.TextField('Kayqimasin about')
    img = models.ImageField('Kayqimasin img',upload_to='media')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kayqimasin'
        verbose_name_plural = 'Kayqimasin'




class aboutuss(models.Model):
    name = models.CharField('aboutus anun',max_length=100)
    about = models.TextField('aboutus about')
    img = models.ImageField('aboutus img',upload_to='media')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'aboutus'
        verbose_name_plural = 'aboutuss'




class apranqnervacharvox(models.Model):
    name = models.CharField('apranqi anun',max_length=40)
    gin = models.IntegerField('aparanqi gin')
    img = models.ImageField('apranqi nkar',upload_to='media')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'apranq'
        verbose_name_plural='apranqner'
    
class hyuranoc(models.Model):
    name = models.CharField('hyuranoci anun',max_length=40)
    about = models.TextField('hyuranoci about')
    img = models.ImageField('hyuranoci img',upload_to='media')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'hyuranoc'
        verbose_name_plural='hyuranocner'
    
class hajortvayr(models.Model):
    name = models.CharField('hajort vayri anun',max_length=40)
    about = models.TextField('hajort vayri about')
    img = models.ImageField('hajort vayri img',upload_to='media')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'hajort vayr'
        verbose_name_plural='hajort vayrer'
    



class blokej(models.Model):
    name = models.CharField('blog anun',max_length=40)
    img = models.ImageField('blog nkar',upload_to='media')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name= 'blog'
        verbose_name_plural ='blogs'




class blokej2(models.Model):
    name = models.CharField('blog2 anun',max_length=100)
    about = models.TextField('blog2 about ')
    img = models.ImageField('blog2 nkar',upload_to ='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'blog2'
        verbose_name_plural ='blog2s'


class Loginimg(models.Model):
    name = models.CharField('login name',max_length=40)
    img = models.ImageField('login img',upload_to='media')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name= 'login'
        verbose_name_plural ='logins'


class staysej(models.Model):
    name = models.CharField('stays eji2 anun',max_length=40)
    img = models.ImageField('stays eji2 nkar',upload_to='media')
    about = models.TextField('stays ejii2 about')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='stays2'
        verbose_name_plural = 'stayss2'

class staysej3(models.Model):
    name =models.CharField('stays3 eji anun',max_length=30)
    price = models.IntegerField()
    img = models.ImageField('stays3 img',upload_to='media')
    orer = models.CharField('oreri qanak',max_length=30)
    oreri_koxqin = models.CharField('oreri koxqin',max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='stays3'
        verbose_name_plural='stayss3'