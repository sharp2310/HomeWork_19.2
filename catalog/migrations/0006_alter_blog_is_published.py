from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Признак публикации'),
        ),
    ]