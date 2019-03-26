# Generated by Django 2.0 on 2019-03-25 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('uname', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('date_hired', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('addedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_wishlist', to='myapp.User')),
                ('wishlists', models.ManyToManyField(related_name='wishlists', to='myapp.User')),
            ],
        ),
    ]
