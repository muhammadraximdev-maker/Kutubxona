from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=200)
    guruh = models.CharField(max_length=50)
    kurs = models.PositiveSmallIntegerField()
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism

class Muallif(models.Model):
    JINS_CHOICES = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol')
    ]
    ism = models.CharField(max_length=200)
    jins = models.CharField(max_length=5, choices=JINS_CHOICES)
    tugilgan_sana = models.DateField()
    kitob_soni = models.PositiveIntegerField(default=0)
    tirik = models.BooleanField(default=True)

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=200)
    janr = models.CharField(max_length=100)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=200)
    ish_vaqti = models.CharField(max_length=50)

    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarish_sana = models.DateField()

    def __str__(self):
        return f"{self.talaba.ism} - {self.kitob.nom}"
