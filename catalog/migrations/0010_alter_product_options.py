from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_edit_published', 'Can edit published'), ('can_edit_desc', 'Can edit description'), ('can_edit_category', 'Can edit category')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]