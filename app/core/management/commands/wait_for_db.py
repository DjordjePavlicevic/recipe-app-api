'''
Django command to wait for database to be available.
'''
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
class Command(BaseCommand):
    '''Django command to wait for db'''

    def handle(self, *args, **options):
        pass
