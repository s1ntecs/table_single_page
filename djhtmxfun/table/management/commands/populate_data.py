from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
from table.models import TableData


class Command(BaseCommand):
    help = 'Add to database random data'

    def handle(self, *args, **options):
        fake = Faker()

        # Создаем 100 случайных записей
        for _ in range(100):
            # Генерируем случайные данные
            date = fake.date_between(start_date='-30d', end_date='today')
            name = fake.name()
            quantity = randint(1, 100)
            distance = randint(1, 1000)

            # Создаем новую запись в базе данных
            TableData.objects.create(
                date=date,
                name=name,
                quantity=quantity,
                distance=distance
            )

        self.stdout.write(self.style.SUCCESS('Data successfully populated'))
