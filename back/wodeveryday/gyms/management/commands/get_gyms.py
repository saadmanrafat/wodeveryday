from django.core.management.base import BaseCommand, CommandError
from gyms.models import Gym, City, Country
import requests


class Command(BaseCommand):
    help = 'Get 1 page of gyms and save to database'

    BASE_URL = 'https://www.crossfit.com/cf/find-a-box.php?page={page}&country=&state=&city=&type=Commercial'

    def handle(self, *args, **options):
        page = 1
        endpoint = self.BASE_URL.format(page=page)
        response = requests.get(endpoint)
        data = response.json()
        affiliates = data['affiliates']
        affiliate = affiliates[2]

        country, _ = Country.objects.get_or_create(name=affiliate.get('country', ''))
        city, _ = City.objects.get_or_create(
            name=affiliate.get('city', ''),
            country=country
            )
        lat, lon = affiliate.get('latlon', '').split(',')

        gym, created = Gym.objects.get_or_create(
            name=affiliate['name'],
            city=city,
            website=affiliate['website'],
            photo=affiliate['photo'],
            status=affiliate['status'],
            photo_version=affiliate['photo_version'],
            ready_to_link=affiliate['ready_to_link'],
            ordernum=affiliate['ordernum'],
            bad_standing=affiliate['bad_standing'],
            zip=affiliate['zip'],
            country_short_code=affiliate['country_short_code'],
            address=affiliate['address'],
            lat=lat,
            lon=lon,
            aid=affiliate['aid'],
            org_type=affiliate['org_type'],
            effective_date=affiliate['effective_date'],
            active=affiliate['active'],
            show_on_map=affiliate['show_on_map'],
            kids=affiliate['kids'],
            name_search=affiliate.get('name_search', ''),
            state_code=affiliate.get('state_code', ''),
            full_state=affiliate.get('full_state', ''),
             )

