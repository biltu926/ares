import json
import pandas as pd
import csv
import os

def get_bsq():
    ''' Get the bsq file for a given date '''
    bsq = pd.read_csv('c:/data/work/supratim/ares/data/dummy_data_storage/bsq-1.csv')
    return bsq

def get_current_stock():
    ''' Get the current stock for a given date '''
    current_stock = pd.read_csv('c:/data/work/supratim/ares/data/dummy_data_storage/Store_Inventory-1.csv')
    return current_stock

def get_store_master():
    ''''''
    store_master = pd.read_csv('c:/data/work/supratim/ares/data/dummy_data_storage/stores_master_list.csv')
    return store_master

def get_product_master():
    ''''''
    product_master = pd.read_csv('c:/data/work/supratim/ares/data/dummy_data_storage/product_master_list.csv')
    return product_master

def get_warehouse_inventory():
    warehouse_inv = pd.read_csv('c:/data/work/supratim/ares/data/dummy_data_storage/WH_Inventory-1.csv')
    return warehouse_inv

def get_input_for_req():
    ''' Fetch the input from the csv files for REQ calculation '''


def get_req():
    ''' Compute and return REQ'''
    store_master = get_store_master()
    product_master = get_product_master()
    bsq = get_bsq()
    current_stock = get_current_stock()

    # Get the cartesian product of the stores X products
    store_master['key'] = 0
    product_master['key'] = 0
    storeXproduct = store_master.merge(product_master, how='left', on='key')
    storeXproduct.drop('key', 1, inplace=True)
    req_qty_df = pd.DataFrame(columns=['Product_Code', 'Store_Code', 'Req'])
    product_req_map = {}

    r_id = 0
    for row in storeXproduct.itertuples():
        bsq_qty = bsq.loc[(bsq['Product_Code'] == row.Product_Code) & (bsq['Store_Code'] == row.Store_Code)]
        current_qty = current_stock.loc[(current_stock['Product_Code'] == row.Product_Code) & (current_stock['Store_Code'] == row.Store_Code)]

        if not bsq_qty.empty and not current_qty.empty:
            product_req_qty = bsq_qty.iloc[0]['BSQ'] - current_qty.iloc[0]['Closing Inventory']
            req_qty_df.loc[r_id] = [row.Product_Code, row.Store_Code, product_req_qty]
            product_req_map[row.Product_Code] = product_req_map.get(row.Product_Code, 0) + product_req_qty
            r_id += 1

    return req_qty_df, product_req_map


def get_replenish_qty():
    ''' Compute and return replenish quantity '''

    req_qty, product_req_map = get_req()
    warehouse_inventory = get_warehouse_inventory()




get_replenish_qty()