import csv
from os.path import exists

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from actors.models import Actor, Director, DirectorGenre, Role
from movies.models import Movie, MovieGenre, MovieDirector


class Command(BaseCommand):
    help = 'Parse csv file with raw data, and populate corresponding database table'
    available_entities = {
        'actor': Actor,
        'director': Director,
        'director_genre': DirectorGenre,
        'role': Role,
        'movie': Movie,
        'movie_genre': MovieGenre,
        'movie_director': MovieDirector
    }

    def add_arguments(self, parser):
        parser.add_argument('--entity', type=str)
        parser.add_argument('--file_path', type=str)
        parser.add_argument('--chunksize', type=int, default=1000)
        parser.add_argument('--max_items', type=int, default=1000)

    def _gen_chunks(self, reader, chunksize=1000, max_items=None):
        chunk = []
        for idx, line in enumerate(reader):
            if max_items and idx == max_items:
                break
            if idx % chunksize == 0 and idx > 0:
                yield chunk
                chunk = []
            chunk.append(line)
        yield chunk

    def handle(self, *args, **options):
        entity = options['entity']
        if entity not in self.available_entities:
            raise CommandError(f'Available entities: {", ".join(self.available_entities)}.')
        model_class = self.available_entities[entity]

        file_path = options['file_path']
        if not exists(file_path):
            raise CommandError(f'Nothing found at {file_path}.')

        if not file_path.endswith('.csv'):
            raise CommandError('CSV file expected.')

        chunksize = options['chunksize']
        max_items = options['max_items']
        reader = csv.DictReader(open(file_path))
        chunks = self._gen_chunks(reader, chunksize=chunksize, max_items=max_items)
        total_items = 0
        for chunk in chunks:
            instances = [model_class(**row) for row in chunk]
            total_items += len(instances)
            with transaction.atomic():
                model_class.objects.bulk_create(instances)

        print(f'{total_items} {entity} items saved to the database')
