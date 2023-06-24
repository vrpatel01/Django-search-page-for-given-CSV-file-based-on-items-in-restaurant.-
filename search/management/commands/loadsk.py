import ast
import csv
from django.core.management.base import BaseCommand
from search.models import Restaurant

class Command(BaseCommand):
    help = 'Import restaurant data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if it exists

            for row in reader:
                id = row[0]
                name = row[1]
                location = row[2]
                items_data = ast.literal_eval(row[3])  # Convert string to dictionary
                lat_long = row[4]
                full_details = row[5]

                # Extract item names and prices from the dictionary
                items = list(items_data.keys())

                # Create a new Restaurant object and save it to the database
                restaurant = Restaurant(
                    id=id,
                    name=name,
                    location=location,
                    items=items,  # Store items as a list
                    lat_long=lat_long,
                    full_details=full_details
                )
                restaurant.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully imported restaurant: {restaurant.name}'))
