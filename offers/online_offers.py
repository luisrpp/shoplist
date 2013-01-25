# -*- coding: utf-8 -*-


class OffersFinder(object):
    """
    The OffersFinder class is responsible for finding product offers
    from different online services.
    """

    def __init__(self, strategy=None):
        self.action = None
        self.offers = None
        if strategy:
            self.action = strategy()

    def find(self, product):
        if(self.action):
            return self.action.find(product)
        else: 
            raise UnboundLocalError('Exception raised, no strategyClass supplied to OffersFinder!')


if __name__ == "__main__":
    from buscape_offers import Buscape
    import sys

    if len(sys.argv) != 2:
        print "Usage %s product_name" % sys.argv[0]
        sys.exit(2)

    bp_offers = OffersFinder(strategy=Buscape)
    offers = bp_offers.find(sys.argv[1])

    for offer in offers:
        print offer
        print "\n\n"
