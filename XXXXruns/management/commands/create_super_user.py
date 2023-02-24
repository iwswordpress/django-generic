from django.core.management import call_command
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Create random users'
    # call_command("createsuperuser")

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Indicates email')
        parser.add_argument('password', type=str, help='Indicates password')
    def handle(self, *args, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        call_command("createsuperuser", email=email,paswword=password)
      