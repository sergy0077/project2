from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Populates data into the database'

    def handle(self, *args, **kwargs):
        category1 = Category.objects.create(name='Category 1', description='Description 1')
        category2 = Category.objects.create(name='Category 2', description='Description 2')

        product1 = Product.objects.create(name='Product 1', description='Description 1', category=category1, price=100)
        product2 = Product.objects.create(name='Product 2', description='Description 2', category=category2, price=200)

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))
