from django.db import models
from django.urls import reverse

ACTIVE_ARTIST = (
    ('Y', 'Active Artist'),
    ('N', 'Not Currently Active')
)

FORMAT = (
    ('V', 'Vinyl'),
    ('CD', 'Compact Disc'),
    ('CS', 'Cassette Tape'),
    ('3C', '3-inch Compact Disc'),
    ('D', 'Digital Only')
)

SOLD_OUT = (
    ('Y', 'Sold Out'),
    ('N', 'Currently Available')
)

# Create your models here.
class Artist(models.Model):
    name = models.CharField(
        max_length=60,
        default='Artist Name'
    )
    members = models.CharField(
        max_length=150,
        null=True
    )
    bio = models.TextField(max_length=300)
    isActive = models.CharField(
        max_length=1,
        choices=ACTIVE_ARTIST,
        default=ACTIVE_ARTIST[0][0]
    )
    img = models.ImageField(
        upload_to="main_app/static/images/artists",
        height_field=None,
        width_field=None,
        default='Please Select An Image'
    )

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('artist-detail', kwargs={'pk': self.id})
    

class Release(models.Model):
    title = models.CharField(
        max_length=100,
        default='Record Title'
    )
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    date = models.DateField('Release Date')
    cat_id = models.CharField(
        max_length=10,
        default='Catalogue ID Number'
    )
    format = models.CharField(
        max_length=2,
        choices=FORMAT,
        default=FORMAT[0][0]
    )
    tracks = models.TextField(
        max_length=1000,
        default='Track List Here'
    )
    soldOut = models.CharField(
        max_length=1,
        choices=SOLD_OUT,
        default=SOLD_OUT[0][0]
    )
    img = models.ImageField(
        upload_to="main_app/static/images/releases",
        height_field=None,
        width_field=None,
        default='Please Select An Image'
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} by {self.artist.name}'
    
    def get_absolute_url(self):
        return reverse('record-detail', kwargs={'pk': self.id})
    