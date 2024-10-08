# Generated by Django 5.1.1 on 2024-09-30 23:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

def create_default_categories(apps, schema_editor):
    Categoria = apps.get_model('juegos', 'Categoria')
    if not Categoria.objects.filter(id=1).exists():
        Categoria.objects.create(id=1, nombre='Supervivencia')
    if not Categoria.objects.filter(id=2).exists():
        Categoria.objects.create(id=2, nombre='Terror')
    if not Categoria.objects.filter(id=3).exists():
        Categoria.objects.create(id=3, nombre='Suspenso')
    if not Categoria.objects.filter(id=4).exists():
        Categoria.objects.create(id=4, nombre='Acción')
    if not Categoria.objects.filter(id=5).exists():
        Categoria.objects.create(id=5, nombre='Mundo abierto')

class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RunPython(create_default_categories),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='juegos.categoria'),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
