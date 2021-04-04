# Generated by Django 3.1.7 on 2021-04-04 17:29

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('upstat', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('downstat', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokedex', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defence', models.IntegerField()),
                ('sp_atk', models.IntegerField()),
                ('sp_def', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('type1', models.CharField(default=None, max_length=10)),
                ('type2', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('gigantamax_factor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, default=None, null=True, upload_to='profile_images')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=30)),
                ('likes', models.IntegerField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='teamname')),
                ('name1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pokedex1', models.IntegerField(blank=True, default=None, null=True)),
                ('gmax1', models.IntegerField(blank=True, default=None, null=True)),
                ('type1_1', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('type2_1', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('ability1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('nature1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('item1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move1_1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move2_1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move3_1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move4_1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype1_1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype2_1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype3_1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype4_1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('level1', models.IntegerField(blank=True, default=None, null=True)),
                ('hp1', models.IntegerField(blank=True, default=None, null=True)),
                ('atk1', models.IntegerField(blank=True, default=None, null=True)),
                ('def1', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atk1', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_def1', models.IntegerField(blank=True, default=None, null=True)),
                ('spd1', models.IntegerField(blank=True, default=None, null=True)),
                ('hpEV1', models.IntegerField(blank=True, default=None, null=True)),
                ('atkEV1', models.IntegerField(blank=True, default=None, null=True)),
                ('defEV1', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkEV1', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defEV1', models.IntegerField(blank=True, default=None, null=True)),
                ('spdEV1', models.IntegerField(blank=True, default=None, null=True)),
                ('hpIV1', models.IntegerField(blank=True, default=None, null=True)),
                ('atkIV1', models.IntegerField(blank=True, default=None, null=True)),
                ('defIV1', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkIV1', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defIV1', models.IntegerField(blank=True, default=None, null=True)),
                ('spdIV1', models.IntegerField(blank=True, default=None, null=True)),
                ('name2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pokedex2', models.IntegerField(blank=True, default=None, null=True)),
                ('gmax2', models.IntegerField(blank=True, default=None, null=True)),
                ('type1_2', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('type2_2', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('ability2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('nature2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('item2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move1_2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move2_2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move3_2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move4_2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype1_2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype2_2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype3_2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype4_2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('level2', models.IntegerField(blank=True, default=None, null=True)),
                ('hp2', models.IntegerField(blank=True, default=None, null=True)),
                ('atk2', models.IntegerField(blank=True, default=None, null=True)),
                ('def2', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atk2', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_def2', models.IntegerField(blank=True, default=None, null=True)),
                ('spd2', models.IntegerField(blank=True, default=None, null=True)),
                ('hpEV2', models.IntegerField(blank=True, default=None, null=True)),
                ('atkEV2', models.IntegerField(blank=True, default=None, null=True)),
                ('defEV2', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkEV2', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defEV2', models.IntegerField(blank=True, default=None, null=True)),
                ('spdEV2', models.IntegerField(blank=True, default=None, null=True)),
                ('hpIV2', models.IntegerField(blank=True, default=None, null=True)),
                ('atkIV2', models.IntegerField(blank=True, default=None, null=True)),
                ('defIV2', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkIV2', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defIV2', models.IntegerField(blank=True, default=None, null=True)),
                ('spdIV2', models.IntegerField(blank=True, default=None, null=True)),
                ('name3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pokedex3', models.IntegerField(blank=True, default=None, null=True)),
                ('gmax3', models.IntegerField(blank=True, default=None, null=True)),
                ('type1_3', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('type2_3', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('ability3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('nature3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('item3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move1_3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move2_3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move3_3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move4_3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype1_3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype2_3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype3_3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype4_3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('level3', models.IntegerField(blank=True, default=None, null=True)),
                ('hp3', models.IntegerField(blank=True, default=None, null=True)),
                ('atk3', models.IntegerField(blank=True, default=None, null=True)),
                ('def3', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atk3', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_def3', models.IntegerField(blank=True, default=None, null=True)),
                ('spd3', models.IntegerField(blank=True, default=None, null=True)),
                ('hpEV3', models.IntegerField(blank=True, default=None, null=True)),
                ('atkEV3', models.IntegerField(blank=True, default=None, null=True)),
                ('defEV3', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkEV3', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defEV3', models.IntegerField(blank=True, default=None, null=True)),
                ('spdEV3', models.IntegerField(blank=True, default=None, null=True)),
                ('hpIV3', models.IntegerField(blank=True, default=None, null=True)),
                ('atkIV3', models.IntegerField(blank=True, default=None, null=True)),
                ('defIV3', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkIV3', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defIV3', models.IntegerField(blank=True, default=None, null=True)),
                ('spdIV3', models.IntegerField(blank=True, default=None, null=True)),
                ('name4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pokedex4', models.IntegerField(blank=True, default=None, null=True)),
                ('gmax4', models.IntegerField(blank=True, default=None, null=True)),
                ('type1_4', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('type2_4', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('ability4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('nature4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('item4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move1_4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move2_4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move3_4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move4_4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype1_4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype2_4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype3_4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype4_4', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('level4', models.IntegerField(blank=True, default=None, null=True)),
                ('hp4', models.IntegerField(blank=True, default=None, null=True)),
                ('atk4', models.IntegerField(blank=True, default=None, null=True)),
                ('def4', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atk4', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_def4', models.IntegerField(blank=True, default=None, null=True)),
                ('spd4', models.IntegerField(blank=True, default=None, null=True)),
                ('hpEV4', models.IntegerField(blank=True, default=None, null=True)),
                ('atkEV4', models.IntegerField(blank=True, default=None, null=True)),
                ('defEV4', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkEV4', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defEV4', models.IntegerField(blank=True, default=None, null=True)),
                ('spdEV4', models.IntegerField(blank=True, default=None, null=True)),
                ('hpIV4', models.IntegerField(blank=True, default=None, null=True)),
                ('atkIV4', models.IntegerField(blank=True, default=None, null=True)),
                ('defIV4', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkIV4', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defIV4', models.IntegerField(blank=True, default=None, null=True)),
                ('spdIV4', models.IntegerField(blank=True, default=None, null=True)),
                ('name5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pokedex5', models.IntegerField(blank=True, default=None, null=True)),
                ('gmax5', models.IntegerField(blank=True, default=None, null=True)),
                ('type1_5', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('type2_5', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('ability5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('nature5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('item5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move1_5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move2_5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move3_5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move4_5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype1_5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype2_5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype3_5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype4_5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('level5', models.IntegerField(blank=True, default=None, null=True)),
                ('hp5', models.IntegerField(blank=True, default=None, null=True)),
                ('atk5', models.IntegerField(blank=True, default=None, null=True)),
                ('def5', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atk5', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_def5', models.IntegerField(blank=True, default=None, null=True)),
                ('spd5', models.IntegerField(blank=True, default=None, null=True)),
                ('hpEV5', models.IntegerField(blank=True, default=None, null=True)),
                ('atkEV5', models.IntegerField(blank=True, default=None, null=True)),
                ('defEV5', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkEV5', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defEV5', models.IntegerField(blank=True, default=None, null=True)),
                ('spdEV5', models.IntegerField(blank=True, default=None, null=True)),
                ('hpIV5', models.IntegerField(blank=True, default=None, null=True)),
                ('atkIV5', models.IntegerField(blank=True, default=None, null=True)),
                ('defIV5', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkIV5', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defIV5', models.IntegerField(blank=True, default=None, null=True)),
                ('spdIV5', models.IntegerField(blank=True, default=None, null=True)),
                ('name6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pokedex6', models.IntegerField(blank=True, default=None, null=True)),
                ('gmax6', models.IntegerField(blank=True, default=None, null=True)),
                ('type1_6', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('type2_6', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('ability6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('nature6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('item6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move1_6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move2_6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move3_6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('move4_6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype1_6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype2_6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype3_6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('movetype4_6', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('level6', models.IntegerField(blank=True, default=None, null=True)),
                ('hp6', models.IntegerField(blank=True, default=None, null=True)),
                ('atk6', models.IntegerField(blank=True, default=None, null=True)),
                ('def6', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atk6', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_def6', models.IntegerField(blank=True, default=None, null=True)),
                ('spd6', models.IntegerField(blank=True, default=None, null=True)),
                ('hpEV6', models.IntegerField(blank=True, default=None, null=True)),
                ('atkEV6', models.IntegerField(blank=True, default=None, null=True)),
                ('defEV6', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkEV6', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defEV6', models.IntegerField(blank=True, default=None, null=True)),
                ('spdEV6', models.IntegerField(blank=True, default=None, null=True)),
                ('hpIV6', models.IntegerField(blank=True, default=None, null=True)),
                ('atkIV6', models.IntegerField(blank=True, default=None, null=True)),
                ('defIV6', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_atkIV6', models.IntegerField(blank=True, default=None, null=True)),
                ('sp_defIV6', models.IntegerField(blank=True, default=None, null=True)),
                ('spdIV6', models.IntegerField(blank=True, default=None, null=True)),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.userprofile')),
            ],
        ),
    ]
