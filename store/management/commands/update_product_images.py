from django.core.management.base import BaseCommand
from store.models import Product, Category
import os


class Command(BaseCommand):
    help = 'Update products with placeholder images'

    def handle(self, *args, **options):
        self.stdout.write('Updating product images...')

        # Update products with placeholder images
        products = Product.objects.all()
        for i, product in enumerate(products):
            image_path = f'products/product_{i+1}.jpg'
            if os.path.exists(f'media/{image_path}'):
                product.image = image_path
                product.save()
                self.stdout.write(f'Updated image for: {product.name}')

        # Update categories with placeholder images
        categories = Category.objects.all()
        category_images = {
            'Electronics': 'categories/electronics.jpg',
            'Clothing': 'categories/clothing.jpg',
            'Books': 'categories/books.jpg',
            'Home & Garden': 'categories/home_and_garden.jpg',
            'Sports': 'categories/sports.jpg',
            'Toys': 'categories/toys.jpg',
        }
        
        for category in categories:
            if category.name in category_images:
                image_path = category_images[category.name]
                if os.path.exists(f'media/{image_path}'):
                    category.image = image_path
                    category.save()
                    self.stdout.write(f'Updated image for category: {category.name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully updated product and category images!')
        )
