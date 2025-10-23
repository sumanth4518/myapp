from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Category, Product, ProductImage
import random


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create categories
        categories_data = [
            {'name': 'Electronics', 'description': 'Electronic devices and gadgets'},
            {'name': 'Clothing', 'description': 'Fashion and apparel'},
            {'name': 'Books', 'description': 'Books and literature'},
            {'name': 'Home & Garden', 'description': 'Home improvement and gardening'},
            {'name': 'Sports', 'description': 'Sports and fitness equipment'},
            {'name': 'Toys', 'description': 'Toys and games for children'},
        ]

        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create subcategories
        subcategories_data = [
            {'name': 'Smartphones', 'parent': 'Electronics'},
            {'name': 'Laptops', 'parent': 'Electronics'},
            {'name': 'Headphones', 'parent': 'Electronics'},
            {'name': 'Men\'s Clothing', 'parent': 'Clothing'},
            {'name': 'Women\'s Clothing', 'parent': 'Clothing'},
            {'name': 'Fiction', 'parent': 'Books'},
            {'name': 'Non-Fiction', 'parent': 'Books'},
            {'name': 'Furniture', 'parent': 'Home & Garden'},
            {'name': 'Kitchen', 'parent': 'Home & Garden'},
        ]

        for subcat_data in subcategories_data:
            parent = Category.objects.get(name=subcat_data['parent'])
            subcategory, created = Category.objects.get_or_create(
                name=subcat_data['name'],
                defaults={'parent': parent, 'description': f'{subcat_data["name"]} products'}
            )
            if created:
                self.stdout.write(f'Created subcategory: {subcategory.name}')

        # Create products
        products_data = [
            # Electronics
            {'name': 'iPhone 15 Pro', 'description': 'Latest iPhone with advanced camera system and A17 Pro chip', 'price': 999.99, 'category': 'Smartphones', 'stock': 50},
            {'name': 'Samsung Galaxy S24', 'description': 'Premium Android smartphone with AI features', 'price': 899.99, 'category': 'Smartphones', 'stock': 30},
            {'name': 'MacBook Pro 16"', 'description': 'Powerful laptop for professionals with M3 Pro chip', 'price': 2499.99, 'category': 'Laptops', 'stock': 20},
            {'name': 'Dell XPS 13', 'description': 'Ultrabook with stunning display and long battery life', 'price': 1299.99, 'category': 'Laptops', 'stock': 25},
            {'name': 'Sony WH-1000XM5', 'description': 'Premium noise-canceling headphones', 'price': 399.99, 'category': 'Headphones', 'stock': 40},
            {'name': 'AirPods Pro', 'description': 'Wireless earbuds with active noise cancellation', 'price': 249.99, 'category': 'Headphones', 'stock': 60},
            
            # Clothing
            {'name': 'Classic T-Shirt', 'description': 'Comfortable cotton t-shirt in various colors', 'price': 19.99, 'category': 'Men\'s Clothing', 'stock': 100},
            {'name': 'Denim Jeans', 'description': 'Classic blue denim jeans with modern fit', 'price': 59.99, 'category': 'Men\'s Clothing', 'stock': 75},
            {'name': 'Summer Dress', 'description': 'Elegant summer dress perfect for any occasion', 'price': 79.99, 'category': 'Women\'s Clothing', 'stock': 50},
            {'name': 'Running Shoes', 'description': 'Comfortable athletic shoes for running and walking', 'price': 89.99, 'category': 'Men\'s Clothing', 'stock': 80},
            
            # Books
            {'name': 'The Great Gatsby', 'description': 'Classic American novel by F. Scott Fitzgerald', 'price': 12.99, 'category': 'Fiction', 'stock': 200},
            {'name': 'To Kill a Mockingbird', 'description': 'Harper Lee\'s masterpiece about justice and morality', 'price': 14.99, 'category': 'Fiction', 'stock': 150},
            {'name': 'Sapiens', 'description': 'A brief history of humankind by Yuval Noah Harari', 'price': 18.99, 'category': 'Non-Fiction', 'stock': 100},
            {'name': 'Atomic Habits', 'description': 'An easy way to build good habits and break bad ones', 'price': 16.99, 'category': 'Non-Fiction', 'stock': 120},
            
            # Home & Garden
            {'name': 'Office Chair', 'description': 'Ergonomic office chair with lumbar support', 'price': 199.99, 'category': 'Furniture', 'stock': 30},
            {'name': 'Coffee Table', 'description': 'Modern wooden coffee table for living room', 'price': 299.99, 'category': 'Furniture', 'stock': 20},
            {'name': 'Kitchen Knife Set', 'description': 'Professional chef knife set with block', 'price': 79.99, 'category': 'Kitchen', 'stock': 40},
            {'name': 'Blender', 'description': 'High-speed blender for smoothies and food prep', 'price': 89.99, 'category': 'Kitchen', 'stock': 35},
            
            # Sports
            {'name': 'Yoga Mat', 'description': 'Non-slip yoga mat for home workouts', 'price': 29.99, 'category': 'Sports', 'stock': 60},
            {'name': 'Dumbbells Set', 'description': 'Adjustable dumbbells for strength training', 'price': 149.99, 'category': 'Sports', 'stock': 25},
            {'name': 'Basketball', 'description': 'Official size basketball for indoor and outdoor play', 'price': 24.99, 'category': 'Sports', 'stock': 45},
            
            # Toys
            {'name': 'LEGO Classic Set', 'description': 'Creative building blocks for all ages', 'price': 39.99, 'category': 'Toys', 'stock': 80},
            {'name': 'Board Game Collection', 'description': 'Family-friendly board games set', 'price': 49.99, 'category': 'Toys', 'stock': 30},
            {'name': 'Remote Control Car', 'description': 'Fast RC car with LED lights', 'price': 69.99, 'category': 'Toys', 'stock': 40},
        ]

        for product_data in products_data:
            category = Category.objects.get(name=product_data['category'])
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'category': category,
                    'stock': product_data['stock']
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@sumanthcommerce.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write('Created admin superuser (username: admin, password: admin123)')

        # Create test users
        test_users = [
            {'username': 'customer1', 'email': 'customer1@example.com', 'password': 'password123', 'first_name': 'John', 'last_name': 'Doe'},
            {'username': 'customer2', 'email': 'customer2@example.com', 'password': 'password123', 'first_name': 'Jane', 'last_name': 'Smith'},
        ]

        for user_data in test_users:
            if not User.objects.filter(username=user_data['username']).exists():
                User.objects.create_user(**user_data)
                self.stdout.write(f'Created test user: {user_data["username"]}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
        self.stdout.write('You can now login with:')
        self.stdout.write('- Admin: username=admin, password=admin123')
        self.stdout.write('- Customer: username=customer1, password=password123')
