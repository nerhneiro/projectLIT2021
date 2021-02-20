from django.core.management import BaseCommand
from mainapp.models import Album, Label, Tag, Artist
from authapp.models import SiteUser

class Command(BaseCommand):

    def handle(self, *args, **options):
        Album.objects.all().delete()
        Tag.objects.all().delete()
        Label.objects.all().delete()
        Artist.objects.all().delete()
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
        album1.tags.add(tag2)
        album1.labels.add(label1)
        album1.save()
        album2 = Album(idYandex=2, idDiscogs=2, idDiscogsSecondary=2, name='Album2', artist=artist2)
        album2.save()
        album2.tags.add(tag1)
        album2.labels.add(label1)
        album2.labels.add(label2)
        # print(Tag.objects.all())
        # print(Label.objects.all())
        # print(Artist.objects.all())
        # print(Album.objects.all())
        super_user = SiteUser.objects.create_superuser('nerhneiro', 'nerhneiro@gmail.com', 'janelake', age=15)
        print(tag1.tagged_albums.all())