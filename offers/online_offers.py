# -*- coding: utf-8 -*-
from decimal import *


class OffersFinder(object):
    """
    The OffersFinder class is responsible for finding product offers
    from different online services.
    """

    def __init__(self, strategy=None):
        self.action = None
        if strategy:
            self.action = strategy()

    def find(self, product):
        if(self.action):
            offers = self.action.find(product)

            result = { 'summary': {'max_price': Decimal(0.00),
                                    'min_price': Decimal(0.00),
                                    'avg_price': Decimal(0.00),
                                    'count': len(offers)}, 
                        'offers': offers}

            prices = [ Decimal(offer['price']) for offer in offers ]
            if prices:
                result['summary']['min_price'] = min(prices)
                result['summary']['max_price'] = max(prices)
                result['summary']['avg_price'] = sum(prices)/len(prices)

            return result
        else: 
            raise UnboundLocalError('Exception raised, no strategyClass supplied to OffersFinder!')



class OfferFinderFactory(object):
    """
    Factory class to create different Offer Finder strategy instances.
    """

    @staticmethod
    def get_instance(strategy="BUSCAPE"):
        if strategy.upper() == "BUSCAPE":
            from buscape_offers import Buscape
            return OffersFinder(Buscape)
        
        raise ValueError('No offer finder strategy with name "%s" found!' % strategy )



if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print "Usage %s product_name" % sys.argv[0]
        sys.exit(2)

    bp_offers = OfferFinderFactory.get_instance(strategy="BUSCAPE")
    offers = bp_offers.find(sys.argv[1])['offers']

    for offer in offers:
        print offer
        print "\n\n"
