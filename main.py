from config.settings import (
    OUTPUT_FILE,
    OUTPUT_SHOP_FILENAME,
    OUTPUT_BUS_STOP_FILENAME,

)
from controller.bus_stop_manager import BusStopManager
from controller.shop_manager import ShopManager

def get_osm_shops():
    shop = ShopManager()
    shop.get_shop("all")
    shop.filter_raw_json(shop.manager.response_json)
    shop.validity_check(shop.shops)
    shop.export_data(OUTPUT_FILE,OUTPUT_SHOP_FILENAME,shop.valid_shops)

def get_osm_bus_stop():
    bus_stop = BusStopManager()
    bus_stop.get_bus_stop("bus_stop")
    bus_stop.filter_raw_json(bus_stop.manager.response_json)
    bus_stop.validity_check(bus_stop.bus_stops)
    bus_stop.export_data(
        OUTPUT_FILE,
        OUTPUT_BUS_STOP_FILENAME,
        bus_stop.valid_bus_stops
    )


if __name__ == "__main__":
    # get_osm_shops()
    get_osm_bus_stop()