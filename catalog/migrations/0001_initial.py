# Generated by Django 3.2.4 on 2021-08-02 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('website', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Carpet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.FileField(null=True, upload_to='catalog/DesignColorSize')),
                ('inventory', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('pile_count', models.IntegerField(blank=True)),
                ('pile_length', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_color', models.CharField(max_length=10)),
                ('texture_color', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DesignInColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.FileField(null=True, upload_to='catalog/DesignColor')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.CharField(choices=[('Rectangle', 'Rectangle'), ('Oval', 'Oval'), ('Round', 'Round')], default='Rectangle', max_length=20)),
                ('length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('width', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddConstraint(
            model_name='size',
            constraint=models.UniqueConstraint(fields=('length', 'width', 'shape'), name='unique_size_t'),
        ),
        migrations.AddField(
            model_name='designincolor',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.color'),
        ),
        migrations.AddField(
            model_name='designincolor',
            name='design',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.design'),
        ),
        migrations.AddField(
            model_name='design',
            name='available_colors',
            field=models.ManyToManyField(through='catalog.DesignInColor', to='catalog.Color'),
        ),
        migrations.AddField(
            model_name='design',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.collection'),
        ),
        migrations.AddConstraint(
            model_name='color',
            constraint=models.UniqueConstraint(fields=('primary_color', 'texture_color'), name='unique_color_t'),
        ),
        migrations.AddField(
            model_name='collection',
            name='available_sizes',
            field=models.ManyToManyField(to='catalog.Size'),
        ),
        migrations.AddField(
            model_name='collection',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.brand'),
        ),
        migrations.AddField(
            model_name='carpet',
            name='designColor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.designincolor'),
        ),
        migrations.AddField(
            model_name='carpet',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.size'),
        ),
        migrations.AddConstraint(
            model_name='carpet',
            constraint=models.UniqueConstraint(fields=('designColor', 'size'), name='unique_ein_t'),
        ),
    ]
