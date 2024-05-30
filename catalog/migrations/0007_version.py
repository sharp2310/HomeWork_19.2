import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_blog_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_num', models.IntegerField(verbose_name='номер версии')),
                ('version_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='название версии')),
                ('is_active_version', models.BooleanField(default=False, verbose_name='признак текущей версии')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]