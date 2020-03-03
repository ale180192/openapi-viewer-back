import os, re
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'delete all migration files that place into migrations folder of each app, andd truncate'


    def add_arguments(self, parser):
        pass

    def _get_abs_path_module(self, app):
        folders = app.split('.')
        path_full = ''
        for folder in folders:
            path_full = os.path.join(path_full, folder)
        return os.path.join(settings.BASE_DIR, path_full)

    def exist_app_into_project(self, app):
        return os.path.exists(self._get_abs_path_module(app))

    def delete_migrations_files(self, app):
        dirname = self._get_abs_path_module(app)
        for f in os.listdir(dirname):
            if not re.search(r'__init__', f):
                os.remove(os.path.join(dirname, f))


    def handler(self, *args, **options):
        for app in settings.INSTALLED_APPS:
            exist_app = self.exist_app_into_project(app)
            if exist_app:
                self.delete_migrations_files(app)
                