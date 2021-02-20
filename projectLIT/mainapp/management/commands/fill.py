from django.core.management import BaseCommand
from mainapp.models import Album, Label, Tag, Artist

class Command(BaseCommand):

    def handle(self, *args, **options):
        tag1 = Tag(name='Excellent')
        tag1.save()
        tag2 = Tag(name='Good')
        tag2.save()
        tag3 = Tag(name='Well')
        tag3.save()
        artist1 = Artist(idDiscogs=100, name='Ira')
        artist1.save()
        artist2 = Artist(idDiscogs=101, name='Irene')
        artist2.save()
        artist3 = Artist(idDiscogs=102, name='Irina')
        artist3.save()
        label1 = Label(name='LabelCom', idDiscogs=1)
        label1.save()
        label2 = Label(name='Music Production', idDiscogs=2)
        label2.save()
        label3 = Label(name='Super label', idDiscogs=3)
        label3.save()
        album1 = Album(idYandex=1, idDiscogs=1, idDiscogsSecondary=1, name='Album1', artist=artist1)
        album1.save()
        album1.tags.add(tag1)
        album1.save()
        print(Tag.objects.all())
        print(Label.objects.all())
        print(Artist.objects.all())
        print(Album.objects.all())