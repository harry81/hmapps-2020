# -*- coding: utf-8 -*-

from django.test import TestCase
from .utils import (get_content_with_key,
                    get_s3_keys,
                    convert_data_to_json,
                    update_deals,
                    create_deals, delete_deals)
from earth.models import Deal


class ArticlesTestCase(TestCase):
    fixtures = ['deals']

    def setUp(self):
        pass


class DealsTeatCase(TestCase):

    def test_bulk_create(self):
        path = u'2016/04/47190_구미시.xml'

        content = get_content_with_key()
        data_json = convert_data_to_json(content)
        condition = {"origin": path}
        delete_deals(condition)
        create_deals(data_json, origin=path)

        for deal in Deal.objects.filter(origin=path):
            print deal.update_location()

    def test_get_s3_keys(self):
        list_of_keys = get_s3_keys(u'2016/04')

    def test_update_deals(self):
        update_deals(year=2016, month=2)

    def test_update_deals_without_month(self):
        update_deals(year=2016)
