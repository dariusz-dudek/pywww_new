from django.core.management.base import BaseCommand
from posts.utils import create_posts


class Command(BaseCommand):
    help = "Creates fake posts"

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            type=int, default=10, dest='number', help='Amount of posts to generate'
        )

    def handle(self, *args, **options):
        n = options.get('number', 10)
        create_posts(n)
        self.stdout.write(f'{n} posts was created')



