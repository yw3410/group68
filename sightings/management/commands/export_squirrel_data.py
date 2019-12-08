from django.core.management.base import BaseCommand,CommandError
from sightings.models import Sighting
import csv
from django.http import HttpResponse

class Command(BaseCommand):
    help='Export CSV file to the database'
    def add_arguments(self,path):
        path.add_argument('csv_file',nargs='+',type=str)

    def handle(self,*arg,**options):
        path=str(options['csv_file'][0])
        with open(path,'w') as csvfile:
            writer = csv.writer(csvfile)
            header=['latitude',
                    'longitude',
                    'squirrel_id',
                    'shift',
                    'date',
                    'age',
                    'fur_color',
                    'location',
                    'specific_location',
                    'running',
                    'chasing',
                    'climbing',
                    'eating',
                    'foraging',
                    'other_activities',
                    'kuks',
                    'quaas',
                    'moans',
                    'tail_flags',
                    'tail_twitches',
                    'approaches',
                    'indifferent',
                    'runs_from',]

            writer.writerow(header)
            squirrel_data=Sighting.objects.all()
            for data in squirrel_data:
                writer.writerow([data.latitude,
                                 data.longitude,
                                 data.squirrel_id,
                                 data.shift,
                                 data.date,
                                 data.age,
                                 data.fur_color,
                                 data.location,
                                 data.specific_location,
                                 data.running,
                                 data.chasing,
                                 data.climbing,
                                 data.eating,
                                 data.foraging,
                                 data.other_activities,
                                 data.kuks,
                                 data.quaas,
                                 data.moans,
                                 data.tail_flags,
                                 data.tail_twitches,
                                 data.approaches,
                                 data.indifferent,
                                 data.runs_from,])
