"""
django command to wait for hte database to be available
"""
import time

from psycopg2 import OperationalError as psycopg20pError

from django.core.management import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):

    """Django command to wait for database"""
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True

            except (psycopg20pError, OperationalError):
                self.stdout.write("Database unavalilable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database avaliable!'))
