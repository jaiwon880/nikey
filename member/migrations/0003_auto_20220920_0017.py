# Generated by Django 3.1.5 on 2022-09-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20220725_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clipboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cb_memo', models.CharField(max_length=200)),
                ('cb_field', models.SmallIntegerField(db_column='cb_')),
                ('th_user', models.SmallIntegerField()),
                ('g_allow', models.IntegerField()),
            ],
            options={
                'db_table': 'clipboard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emoticon',
            fields=[
                ('e_default', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'emoticon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmoticonRelationWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_r_word', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'emoticon_relation_word',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KeyboardSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kb_korea_form', models.IntegerField()),
                ('kb_full_stop', models.IntegerField()),
                ('kb_capital_letter', models.IntegerField()),
                ('kb_double_consonant', models.IntegerField()),
                ('kb_suggested_words', models.IntegerField()),
                ('kb_typo_correction', models.IntegerField()),
            ],
            options={
                'db_table': 'keyboard_setting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'member_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MyDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('md_bookmark', models.CharField(blank=True, max_length=255, null=True)),
                ('md_save_date', models.DateField()),
            ],
            options={
                'db_table': 'my_dictionary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NeologismDictionary',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('nd_word', models.CharField(max_length=40)),
                ('nd_detail', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'neologism_dictionary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NeologismDictionaryAssociatedWord',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('nd_a_word', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'neologism_dictionary_associated_word',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NeologismDictionaryBookmark',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('nd_bookmark', models.IntegerField()),
            ],
            options={
                'db_table': 'neologism_dictionary_bookmark',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NeologismDictionaryExample',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('nd_ex', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'neologism_dictionary_example',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NeologismDictionarySearch',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('nd_s_word', models.CharField(blank=True, max_length=40, null=True)),
                ('nd_s_date', models.DateField()),
                ('nd_word_frequency_data', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'neologism_dictionary_search',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecommendLearningData',
            fields=[
                ('rl_text', models.CharField(max_length=255)),
                ('rl_emoticon', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'recommend_learning_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ThemeSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('th_dark', models.IntegerField()),
                ('th_default', models.SmallIntegerField()),
                ('th_user', models.SmallIntegerField()),
                ('g_allow', models.IntegerField()),
            ],
            options={
                'db_table': 'theme_setting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ToolSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_cb_icon', models.IntegerField()),
                ('t_kb_setting', models.IntegerField()),
                ('t_spell_check', models.IntegerField()),
                ('t_nd', models.IntegerField()),
                ('t_allow', models.IntegerField()),
            ],
            options={
                'db_table': 'tool_setting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='YourTable',
            fields=[
                ('uid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('isnosql', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'your_table',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
    ]
