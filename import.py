#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, glob, re, random, glob

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"

import django
django.setup()

from cities.models import Country, City, Region, PostalCode

from company.models import Company, CompanyClass, CompanyClassTranslation
from company.models import CompanyPhoto, CompanySize, CompanySizeTranslation
from company.models import CompanyWheels, CompanyWheelsTranslation, Warehouse
import random

def clean_all():
    CompanyWheels.objects.all().delete()
    CompanyPhoto.objects.all().delete()
    CompanyClass.objects.all().delete()
    CompanySize.objects.all().delete()
    Company.objects.all().delete()

def import_dics():
    company_companyclass_1 = CompanyClass()
    company_companyclass_1.order = 2
    company_companyclass_1.save()

    company_companyclass_2 = CompanyClass()
    company_companyclass_2.order = 1
    company_companyclass_2.save()

    company_companyclass_3 = CompanyClass()
    company_companyclass_3.order = 3
    company_companyclass_3.save()

    # Processing model: company.models.CompanySize


    company_companysize_1 = CompanySize()
    company_companysize_1.order = 1
    company_companysize_1.save()

    company_companysize_2 = CompanySize()
    company_companysize_2.order = 2
    company_companysize_2.save()

    company_companysize_3 = CompanySize()
    company_companysize_3.order = 3
    company_companysize_3.save()

    # Processing model: company.models.CompanyWheels


    company_companywheels_1 = CompanyWheels()
    company_companywheels_1.order = 1
    company_companywheels_1.save()

    company_companywheels_2 = CompanyWheels()
    company_companywheels_2.order = 2
    company_companywheels_2.save()

    company_companywheels_3 = CompanyWheels()
    company_companywheels_3.order = 3
    company_companywheels_3.save()

    company_companywheels_4 = CompanyWheels()
    company_companywheels_4.order = 4
    company_companywheels_4.save()


    # Processing model: company.models.CompanyClassTranslation


    company_companyclass_translation_1 = CompanyClassTranslation()
    company_companyclass_translation_1.language_code = u'en'
    company_companyclass_translation_1.title = u'Premium'
    company_companyclass_translation_1.short_title = u'Premium'
    company_companyclass_translation_1.master = company_companyclass_1
    company_companyclass_translation_1.save()

    company_companyclass_translation_2 = CompanyClassTranslation()
    company_companyclass_translation_2.language_code = u'es'
    company_companyclass_translation_2.title = u'Prima'
    company_companyclass_translation_2.short_title = u'Prima'
    company_companyclass_translation_2.master = company_companyclass_1
    company_companyclass_translation_2.save()

    company_companyclass_translation_3 = CompanyClassTranslation()
    company_companyclass_translation_3.language_code = u'en'
    company_companyclass_translation_3.title = u'B\xe1sico'
    company_companyclass_translation_3.short_title = u'B\xe1sico'
    company_companyclass_translation_3.master = company_companyclass_2
    company_companyclass_translation_3.save()

    company_companyclass_translation_4 = CompanyClassTranslation()
    company_companyclass_translation_4.language_code = u'en'
    company_companyclass_translation_4.title = u'Luxury'
    company_companyclass_translation_4.short_title = u'Luxury'
    company_companyclass_translation_4.master = company_companyclass_3
    company_companyclass_translation_4.save()

    company_companyclass_translation_5 = CompanyClassTranslation()
    company_companyclass_translation_5.language_code = u'es'
    company_companyclass_translation_5.title = u'Lujo'
    company_companyclass_translation_5.short_title = u'Lujo'
    company_companyclass_translation_5.master = company_companyclass_3
    company_companyclass_translation_5.save()

    # Processing model: company.models.CompanySizeTranslation


    company_companysize_translation_1 = CompanySizeTranslation()
    company_companysize_translation_1.language_code = u'en'
    company_companysize_translation_1.title = u'Carry On'
    company_companysize_translation_1.short_title = u'Carry On'
    company_companysize_translation_1.master = company_companysize_1
    company_companysize_translation_1.save()

    company_companysize_translation_2 = CompanySizeTranslation()
    company_companysize_translation_2.language_code = u'es'
    company_companysize_translation_2.title = u'Continua'
    company_companysize_translation_2.short_title = u'Continua'
    company_companysize_translation_2.master = company_companysize_1
    company_companysize_translation_2.save()

    company_companysize_translation_3 = CompanySizeTranslation()
    company_companysize_translation_3.language_code = u'en'
    company_companysize_translation_3.title = u'Medium Size'
    company_companysize_translation_3.short_title = u'Medium Size'
    company_companysize_translation_3.master = company_companysize_2
    company_companysize_translation_3.save()

    company_companysize_translation_4 = CompanySizeTranslation()
    company_companysize_translation_4.language_code = u'es'
    company_companysize_translation_4.title = u'Talla mediana'
    company_companysize_translation_4.short_title = u'Talla mediana'
    company_companysize_translation_4.master = company_companysize_2
    company_companysize_translation_4.save()

    company_companysize_translation_5 = CompanySizeTranslation()
    company_companysize_translation_5.language_code = u'es'
    company_companysize_translation_5.title = u'Talla grande'
    company_companysize_translation_5.short_title = u'Talla grande'
    company_companysize_translation_5.master = company_companysize_3
    company_companysize_translation_5.save()

    company_companysize_translation_6 = CompanySizeTranslation()
    company_companysize_translation_6.language_code = u'en'
    company_companysize_translation_6.title = u'Large Size'
    company_companysize_translation_6.short_title = u'Large Size'
    company_companysize_translation_6.master = company_companysize_3
    company_companysize_translation_6.save()

    # Processing model: company.models.CompanyWheelsTranslation


    company_companywheels_translation_1 = CompanyWheelsTranslation()
    company_companywheels_translation_1.language_code = u'en'
    company_companywheels_translation_1.title = u'2 Wheels'
    company_companywheels_translation_1.short_title = u'2'
    company_companywheels_translation_1.master = company_companywheels_1
    company_companywheels_translation_1.save()

    company_companywheels_translation_2 = CompanyWheelsTranslation()
    company_companywheels_translation_2.language_code = u'es'
    company_companywheels_translation_2.title = u'2 Ruedas'
    company_companywheels_translation_2.short_title = u'2'
    company_companywheels_translation_2.master = company_companywheels_1
    company_companywheels_translation_2.save()

    company_companywheels_translation_3 = CompanyWheelsTranslation()
    company_companywheels_translation_3.language_code = u'en'
    company_companywheels_translation_3.title = u'4 Wheels'
    company_companywheels_translation_3.short_title = u'4'
    company_companywheels_translation_3.master = company_companywheels_2
    company_companywheels_translation_3.save()

    company_companywheels_translation_4 = CompanyWheelsTranslation()
    company_companywheels_translation_4.language_code = u'es'
    company_companywheels_translation_4.title = u'4 Ruedas'
    company_companywheels_translation_4.short_title = u'4'
    company_companywheels_translation_4.master = company_companywheels_2
    company_companywheels_translation_4.save()

    company_companywheels_translation_5 = CompanyWheelsTranslation()
    company_companywheels_translation_5.language_code = u'en'
    company_companywheels_translation_5.title = u'6 Wheels'
    company_companywheels_translation_5.short_title = u'6'
    company_companywheels_translation_5.master = company_companywheels_3
    company_companywheels_translation_5.save()

    company_companywheels_translation_6 = CompanyWheelsTranslation()
    company_companywheels_translation_6.language_code = u'es'
    company_companywheels_translation_6.title = u'6 Ruedas'
    company_companywheels_translation_6.short_title = u'6'
    company_companywheels_translation_6.master = company_companywheels_3
    company_companywheels_translation_6.save()

    company_companywheels_translation_7 = CompanyWheelsTranslation()
    company_companywheels_translation_7.language_code = u'en'
    company_companywheels_translation_7.title = u'No Wheels'
    company_companywheels_translation_7.short_title = u'No Wheels'
    company_companywheels_translation_7.master = company_companywheels_4
    company_companywheels_translation_7.save()

    company_companywheels_translation_8 = CompanyWheelsTranslation()
    company_companywheels_translation_8.language_code = u'es'
    company_companywheels_translation_8.title = u'sin Ruedas'
    company_companywheels_translation_8.short_title = u'sin Ruedas'
    company_companywheels_translation_8.master = company_companywheels_4
    company_companywheels_translation_8.save()

def import_data():
    # Initial Imports

    # Processing model: company.models.Company

    for i in range(100):
        company = Company()
        company.set_current_language('en')
        company.title = u'SwissGear Large Trolley Bag'
        company.full_price = round(100+random.random()*200, 2)
        company.day_price = round(3+random.random()*7, 2)
        company.cnt = int(5+random.random()*20)
        company.company_wheels =  random.choice(CompanyWheels.objects.all())
        company.company_size =  random.choice(CompanySize.objects.all())
        company.company_class =  random.choice(CompanyClass.objects.all())
        company.details = u'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed'
        company.features = u'Lorem ipsum dolor sit amet, consectetur \r\nadipisicing elit, sed do eiusmod tempor incididunt \r\nut labore et dolore magna aliqua. Duis aute\r\nirure dolor in reprehenderit in voluptate velit esse'
        company.save()

        for i in range(random.randrange(1,3)):
            photo = CompanyPhoto()
            photo.company = company
            photo.photo = 'company/4R5l6xqban.png'
            photo.save()

def import_warehouses():
    c_usa = Country.objects.get(name='United States')
    c_mx = Country.objects.get(name='Mexico')

    for i in range(20):
        c = random.choice([c_usa, c_mx])
        r = random.choice(c.region_set.all())
        t = random.choice(r.city_set.all())
        while Warehouse.objects.filter(city=t).exists():
            t = random.choice(r.city_set.all())

        w = Warehouse()
        w.country = c
        w.region = r
        w.city = t
        w.save()


def assign_warehouses():
    for bag in Company.objects.all():
        bag.warehouse = random.choice(Warehouse.objects.all())
        bag.save()


#clean_all()
#import_dics()
#import_data()
import_warehouses()
assign_warehouses()
