from datetime import datetime, timedelta
import random

from django.core.management.base import BaseCommand
from json_serve.models import ActivityPeriod


class Command(BaseCommand):
    help = "Save random activity data of users"

    def add_arguments(self, parser):
        parser.add_argument(
            '--entries',
            type=int, 
            help="to specify the number of records to be generated",
            const=10,
            nargs='?')
        parser.add_argument(
            '--delete-existing',
            action='store_true',
            dest='delete_existing',
            default=False,
            help='Delete existing activity records.',
        )
    def get_timezone(self):
        return random.choice(['Africa/Lubumbashi', 'Asia/Manila', 'America/Ensenada', 'Europe/Jersey', 
                            'America/Panama', 'Europe/Moscow', 'America/Winnipeg', 'Africa/Mbabane',
                            'US/Mountain', 'Asia/Kolkata'])

    def get_name(self):
        return random.choice(['Jonas Kahnwald', 'Hannah Kahnwald', 'Martha Nielsen',
                            'Elisabeth Doppler'])

    def get_dates(self):
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2014, 2017)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        start = datetime(year, month, day, hour, minute)
        dhour = random.randint(0, 3)
        dmin = random.randint(0, 59)
        end = start + timedelta(hours=dhour, minutes=dmin)
        return start, end

    def handle(self, *args, **options):
        records = []
        for _ in range(options['entries'] or 10):
            entry, end = self.get_dates()
            kwargs = {
                'real_name': self.get_name(),
                'start_time': entry,
                'end_time': end,
                'tz': self.get_timezone()
            }
            record = ActivityPeriod(**kwargs)
            records.append(record)
        if options["delete_existing"]:
            ActivityPeriod.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing records deleted.'))
        ActivityPeriod.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS('%s Entries created and saved successfully.' % (options['entries'] or 10)))

        
