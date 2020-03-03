from django.db import migrations


def forwards_func(apps, schema_editor):
    Rol = apps.get_model('core', 'Rol')
    db_alias = schema_editor.connection.alias
    Rol.objects.using(db_alias).bulk_create([
        Rol(name='admin', description='This rol is superuser'),
        Rol(name='freemium', description='This rol is an user normal')
    ])

def reverse_func(apps, schema_editor):
    Rol = apps.get_model('core', 'Rol')
    db_alias = schema_editor.connection.alias
    Rol.objects.using(db_alias).filter(name='admin').delete()
    Rol.objects.using(db_alias).filter(name='freemium').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(code=forwards_func, reverse_code=reverse_func)
    ]
