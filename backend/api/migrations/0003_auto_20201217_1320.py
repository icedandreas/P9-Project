# Generated by Django 3.1.4 on 2020-12-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201215_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtcCodesTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id', models.CharField(blank=True, max_length=20, null=True)),
                ('atc_codes', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'atc_codes_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CategoriesTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id', models.CharField(blank=True, max_length=20, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('mesh_id', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categories_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DosagesTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id', models.CharField(blank=True, max_length=20, null=True)),
                ('form', models.TextField(blank=True, null=True)),
                ('route', models.TextField(blank=True, null=True)),
                ('strength', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dosages_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DrugInteractionsTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id_1', models.CharField(blank=True, max_length=20, null=True)),
                ('drug_id_2', models.CharField(blank=True, max_length=20, null=True)),
                ('sd_name', models.TextField(blank=True, null=True)),
                ('sd_desc', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'drug_interactions_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupsTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('primary_id', models.CharField(blank=True, max_length=20, null=True)),
                ('groups', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'groups_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainTable',
            fields=[
                ('primary_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cas_number', models.CharField(blank=True, max_length=20, null=True)),
                ('unii', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('indication', models.TextField(blank=True, null=True)),
                ('pharmacodynamics', models.TextField(blank=True, null=True)),
                ('mechanism', models.TextField(blank=True, null=True)),
                ('toxicity', models.TextField(blank=True, null=True)),
                ('metabolism', models.TextField(blank=True, null=True)),
                ('absorbtion', models.TextField(blank=True, null=True)),
                ('halflife', models.TextField(blank=True, null=True)),
                ('protein_binding', models.TextField(blank=True, null=True)),
                ('route_of_elimination', models.TextField(blank=True, null=True)),
                ('volume_of_distribution', models.TextField(blank=True, null=True)),
                ('clearance', models.TextField(blank=True, null=True)),
                ('classification', models.TextField(blank=True, null=True)),
                ('fda_label', models.TextField(blank=True, null=True)),
                ('msds', models.TextField(blank=True, null=True)),
                ('reactions', models.TextField(blank=True, null=True)),
                ('snp_effects', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'main_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MixturesTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id', models.CharField(blank=True, max_length=20, null=True)),
                ('mixture_name', models.TextField(blank=True, null=True)),
                ('ingredient', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mixtures_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PathwaysTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id', models.CharField(blank=True, max_length=20, null=True)),
                ('pathways', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pathways_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductsTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id', models.CharField(blank=True, max_length=20, null=True)),
                ('product_name', models.TextField(blank=True, null=True)),
                ('labeller', models.TextField(blank=True, null=True)),
                ('ndc_id', models.TextField(blank=True, null=True)),
                ('ndc_product_code', models.TextField(blank=True, null=True)),
                ('dpd_id', models.TextField(blank=True, null=True)),
                ('ema_product_code', models.TextField(blank=True, null=True)),
                ('ema_ma_number', models.TextField(blank=True, null=True)),
                ('started_marketing_on', models.DateField(blank=True, null=True)),
                ('ended_marketing_on', models.DateField(blank=True, null=True)),
                ('dosage_form', models.TextField(blank=True, null=True)),
                ('strength', models.TextField(blank=True, null=True)),
                ('route', models.TextField(blank=True, null=True)),
                ('fda_application_number', models.TextField(blank=True, null=True)),
                ('generic', models.BooleanField(blank=True, null=True)),
                ('over_the_counter', models.BooleanField(blank=True, null=True)),
                ('approved', models.BooleanField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('source', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'products_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PropertiesTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id', models.CharField(blank=True, max_length=20, null=True)),
                ('properties', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'properties_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SecondaryIdsTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('primary_id', models.CharField(blank=True, max_length=20, null=True)),
                ('secondary_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'secondary_ids_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SequencesTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id', models.CharField(blank=True, max_length=20, null=True)),
                ('sequence_t', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sequences_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SynonymsTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id', models.CharField(blank=True, max_length=20, null=True)),
                ('synonym_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'synonyms_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TargetsTable',
            fields=[
                ('pkey', models.AutoField(primary_key=True, serialize=False)),
                ('drug_id', models.CharField(blank=True, max_length=20, null=True)),
                ('targets', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'targets_table',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Drug',
        ),
    ]
