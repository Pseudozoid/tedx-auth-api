from django.db import migrations

def create_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    UserProfile = apps.get_model('accounts', 'UserProfile')

    if not User.objects.filter(username='admin').exists():
        user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        UserProfile.objects.create(user=user, role='admin')

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),  # adjust if your previous migration has a different name
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]

