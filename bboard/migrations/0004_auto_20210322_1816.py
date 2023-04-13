

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bboard.profile', verbose_name='Профиль'),
        ),
    ]
