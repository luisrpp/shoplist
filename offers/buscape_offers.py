# -*- coding: utf-8 -*-
from buscape import Buscape as BP
import json
import os

BUSCAPE_APP_ID = os.environ.get('BUSCAPE_APP_ID')


class Buscape(object):

    def find(self, product):
        try:
            apiki_buscape = BP(applicationID=BUSCAPE_APP_ID)
            apiki_buscape.set_sandbox()

            bp_offers = apiki_buscape.find_offer_list(keyword=product.replace(' ',','), format='json')
            bp_offers = bp_offers.get('data')
            bp_offers = json.loads(bp_offers)

            offers = []
            for bp_offer in bp_offers['offer']:
                offer = {}
                offer['product'] = bp_offer['offer']['offername']
                offer['seller'] = bp_offer['offer']['seller']['sellername']
                offer['currency'] = bp_offer['offer']['price']['currency']['abbreviation']
                offer['price'] = bp_offer['offer']['price']['value']
                
                if 'thumbnail' in bp_offer['offer']:
                    offer['thumbnail'] = bp_offer['offer']['thumbnail']['url']

                for link in bp_offer['offer']['links']:
                    offer['url'] = link['link']['url']
                    break

                offers.append(offer)

            return offers

        except Exception:
            return []
