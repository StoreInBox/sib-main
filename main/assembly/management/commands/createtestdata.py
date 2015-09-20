# coding: utf-8
from __future__ import unicode_literals

import os
import random

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

from ... import models
from products import models as products_models


class Command(BaseCommand):
    args = 'no args for this command'
    help = 'Creates '

    CHARACTERISTICS = [
        {
            'name': 'weight',
            'units': 'kg',
            'default_value': 0,
        },
        {
            'name': 'width',
            'units': 'm',
            'default_value': 0,
        },
        {
            'name': 'height',
            'units': 'm',
            'default_value': 0,
        },
        {
            'name': 'brand',
            'units': '',
            'default_value': '',
        }
    ]

    CATEGORIES = [
        {
            'name': 'Bulbasaur',
            'children': [
                {
                    'name': 'Ivysaur',
                },
                {
                    'name': 'Venusaur',
                },
            ]
        },
        {
            'name': 'Charmander',
            'children': [
                {
                    'name': 'Charmeleon',
                },
                {
                    'name': 'Charizard',
                },
                {
                    'name': 'Squirtle',
                },
                {
                    'name': 'Wartortle',
                },
                {
                    'name': 'Blastoise',
                },
            ]
        },
    ]

    # def _get_test_image(self):
    #     path = os.path.join(settings.BASE_DIR, 'assembly', 'management', 'commands', 'testimages')
    #     images = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    #     return File(open(os.path.join(path, random.choice(images))))

    def _create_characteristics(self):
        self.stdout.write('Creating characteristics...')
        for characteristic_data in self.CHARACTERISTICS:
            if not products_models.Characteristic.objects.filter(name=characteristic_data['name']).exists():
                characteristic = products_models.Characteristic.objects.create(**characteristic_data)
                self.stdout.write('Characteristic {} created'.format(characteristic))
        self.stdout.write('...Done')

    def _create_categories(self):
        self.stdout.write('Creating sections, categories and subcategories...')
        for parent_category_data in self.CATEGORIES:
            if not products_models.Category.objects.filter(name=parent_category_data['name']).exists():
                children = parent_category_data.pop('children')
                parent_category = products_models.Category.objects.create(**parent_category_data)
                self.stdout.write('Parent category {} created'.format(parent_category))
                for child_data in children:
                    category = products_models.Category.objects.create(parent=parent_category, **child_data)
                    self.stdout.write('Child category {} created'.format(category))
        self.stdout.write('...Done')

    def _create_users(self):
        self.stdout.write('Creating users ...')
        if not get_user_model().objects.filter(username='admin'):
            get_user_model().objects.create_superuser(username='admin', password='admin', email='admin@i.ua')
            self.stdout.write('Superuser admin/admin created')
        else:
            self.stdout.write('User admin already exists')
        self.stdout.write('...Done')

    # def _create_products(self, fast=False):
    #     self.stdout.write('Creating products...')
    #     subcategories = products_models.Subcategory.objects.all()
    #     if fast:
    #         subcategories = subcategories[:2]
    #     for index, subcategory in enumerate(subcategories):
    #         self.stdout.write('Creating products for subcategory {}'.format(subcategory))
    #         for i in range(3 if index == 0 else 3):
    #             product = products_models.Product.objects.create(
    #                 name='product-{}-{}'.format(subcategory.id, i),
    #                 short_description='product-short-description-{}-{}'.format(subcategory.id, i),
    #                 description='product-description-{}-{}'.format(subcategory.id, i),
    #                 subcategory=subcategory,
    #                 materials=subcategories[1],
    #             )
    #             products_models.ProductImage.objects.create(
    #                 product=product,
    #                 image=self._get_test_image(),
    #                 description='Image for product {}'.format(product.name)
    #             )
    #             products_models.ProductImage.objects.create(
    #                 product=product,
    #                 image=self._get_test_image(),
    #                 description='Second image for product {}'.format(product.name)
    #             )
    #             for j in range(3 if not index else 1):
    #                 product_configuration = products_models.ProductConfiguration.objects.create(
    #                     product=product,
    #                     code='pc-{}-{}-{}'.format(index, i, j),
    #                     price_uah=10 * (index + 1) * (i + 1) * (j + 1),
    #                 )
    #                 product_configuration.attrs.brand = random.choice(['B1', 'B2', 'B3', 'B4', 'B5'])
    #                 product_configuration.attrs.width = random.choice(['10', '20', '30', '40', '50'])
    #                 product_configuration.attrs.height = 10
    #                 product_configuration.attrs.weight = random.choice(['100', '200', '300', '400', '500'])
    #         self.stdout.write('Products created')
    #     self.stdout.write('...Done')

    # def _create_filters(self, fast=False):
    #     self.stdout.write('Creating filters...')
    #     subcategories = products_models.Subcategory.objects.all()
    #     if fast:
    #         subcategories = subcategories[:2]
    #     for subcategory in subcategories:
    #         self.stdout.write('Creating filters for subcategory {}'.format(subcategory))
    #         models.NumericAttributeFilter.objects.create(
    #             characteristic=products_models.Characteristic.objects.get(name='width'),
    #             subcategory=subcategory,
    #             max_value=60,
    #             min_value=0,
    #             name='Width filter'
    #         )
    #     categories = products_models.Category.objects.all()
    #     if fast:
    #         categories = categories[:2]
    #     for category in categories:
    #         self.stdout.write('Creating filters for category {}'.format(category))
    #         models.ChoicesAttributeFilter.objects.create(
    #             characteristic=products_models.Characteristic.objects.get(name='brand'),
    #             category=category,
    #             name='Brand filter',
    #             is_auto_update=True,
    #             choices='B1, B2, B3, B4, B5',
    #         )
    #     self.stdout.write('...Done')

    def handle(self, *args, **options):
        self._create_characteristics()
        self._create_categories()
        self._create_users()
        # self._create_products(fast='fast' in args)
        # self._create_filters(fast='fast' in args)
