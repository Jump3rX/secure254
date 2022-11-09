# Generated by Django 3.1.7 on 2022-01-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('TanaRiver', 'TanaRiver'), ('Lamu', 'Lamu'), ('TaitaTaveta', 'TaitaTaveta'), ('Garissa', 'Garissa'), ('Wajir', 'Wajir'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Isiolo', 'Isiolo'), ('Meru', 'Meru'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Kirinyaga', 'Kirinyaga'), ('Muranga', 'Muranga'), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('West-Pokot', 'West-Pokot'), ('Samburu', 'Samburu'), ('TransNzoia', 'TransNzoia'), ('UasinGishu', 'UasinGishu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nandi', 'Nandi'), ('Baringo', 'Baringo'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kericho', 'Kericho'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kisumu', 'Kisumu'), ('HomaBay', 'HomaBay'), ('Migori', 'Migori'), ('Kisii', 'Kisii'), ('Nyamira', 'Nyamira'), ('Nairobi', 'Nairobi')], default='Nairobi', max_length=18)),
                ('area', models.CharField(max_length=200)),
                ('incident', models.CharField(choices=[('Theft', 'Theft'), ('Robbery', 'Robbery'), ('CarJack', 'CarJack'), ('Fire', 'Fire'), ('Road Accident', 'Road Accident'), ('Hit and Run', 'Hit and Run'), ('Dangerous Driving', 'Dangerous Driving'), ('Traffic Jam', 'Traffic Jam'), ('Other', 'Other')], max_length=25)),
                ('Describe_other_incident', models.TextField(max_length=150, null=True)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]
