from data.req import *

class ares_resolver:
    @staticmethod
    def resolver_replenishment_order():
        return get_replenish_qty()

    @staticmethod
    def resolver_upload():
        ''' Call this resolver to upload the files to the DB or to the storage'''

    @staticmethod
    def resolver_download():
        ''' Call this resover to download the results'''
