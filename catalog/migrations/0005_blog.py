from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=250, null=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('img', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='Превью')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(blank=True, null=True, verbose_name='Признак публикации')),
                ('views_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Счетчик просмотров')),
            ],
            options={
                'verbose_name': 'материал',
                'verbose_name_plural': 'материалы',
            },
        ),
    ]