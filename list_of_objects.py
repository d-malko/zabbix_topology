#!/usr/bin/env python
import urllib, os, io, pprint
from decimal import Decimal
import simplejson as json
import six.moves.cPickle as pickle

zabbix_switches = []
cubic_switches = []
db_file = 'zabbix_topology.db'

url = "http://work.volia.net/bm3/cache/eth/switchInformation/volia.ternopil"


response = urllib.urlopen(url) #save text from url TODO need to add try catch
data_from_url = json.loads(response.read()) # convert json to dictionary

class List:
    pass


class Switch:
    """Object switch

    """
    def __init__(self, mac="", ip="", model="", switch_2="", switch_3="", switch_SNMP_write="", snmp_write="", vlan="", serial="", monitoring="", hostname="", switch_11="", inventory_state="", street="", building="", porch="", floor="", nettype="", ports = []): #, '55'="", '1'): #, upport, upswitch_mac, upswitch_port):
        self.mac = mac
        self.ip = ip
        self.model = model
        self.snmp_write = snmp_write
        self.vlan = vlan
        self.serial = serial
        self.hostname = hostname
        self.inventory_state = inventory_state
        self.monitoring = monitoring
        self.street = street
        self.building = building
        self.porch = porch
        self.floor = floor
        self.ports = []


        # self.upswitch.port = upswitch.port
        # self.upswitch.mac = upswitch.mac

        #no return

    def __str__(self):
        return "member of Switch"

    def __getattr__(self, name):
        return name

    def compare_switch(self, switch2):
    # def compare_switch(self, list1=[], list2=[], mac="", id=""):
        pass
    def change_ip(self):
        #set ip when no ip
        #del ip set
        #change ip
        pass
    def get_id(self):
        pass
    def change_model(self):
        pass
    def change_serial(self):
        pass
    def change_hostname(self):
        pass
    def change_inventory_state(self):
        pass
    def change_upstream_port(self):
        pass
    def change_upswitch(self):
        pass
    def change_upswitch_downport(self):
        pass
    def change_vlan(self):
        pass
    def change_snmp(self):
        pass

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class Port():
    """Object port

    """
    def __init__(self, port="", num="", upswitch_mac="", upswitch_port=""):
        self.port = port
        self.num = num
        self.upswitch_mac = upswitch_mac
        self.upswitch_port = upswitch_port



def save_to_file(data, file_to_save):
    with open(file_to_save, 'w') as outfile:
        for obj in data:
            outfile.write(json.dumps(obj, default=lambda o: o.__dict__))
            # outfile.write(pickle.dumps(obj.toJSON()))
        outfile.close()

        # pickle.PicklingError TODO need to add try catch and this error
        # with io.open(file_json, 'w', encoding='utf-8') as outfile:

def load_from_file(data, file_to_read):
    with open(file_to_read, 'r') as infile:
        # print(infile.read())
        list_obj = json.loads(infile.read())
        # print(list_obj)
        infile.close()
        # pickle.UnpicklingError TODO need to add try catch and this error
    return list_obj


def dump_keys(d, lvl=0):
    for k, v in d.iteritems():
        print '%s%s  %s' % (lvl * ' ', k, v.__dict__)
        if type(v) == dict:
            dump_keys(v, lvl+1)


def create_list(switch_dict):
    for mac in data_from_url:
        sw = Switch(mac)
        switch_dict.append(sw)
        if isinstance(data_from_url[mac], dict): # if dictionary
                for switch_key, switch_property  in data_from_url[mac].items(): # loop properties
                    if not isinstance(data_from_url[mac][switch_key], dict):
                        if switch_key == '1':
                            sw.ip = data_from_url[mac][switch_key]
                        elif switch_key == '2':
                            sw.model = data_from_url[mac][switch_key]
                        elif switch_key == '5':
                            sw.snmp_write = data_from_url[mac][switch_key]
                        elif switch_key == '7':
                            sw.vlan = data_from_url[mac][switch_key]
                        elif switch_key == '8':
                            sw.serial = data_from_url[mac][switch_key]
                        elif switch_key == '9':
                            sw.monitoring = data_from_url[mac][switch_key]
                        elif switch_key == '10':
                            sw.hostname = data_from_url[mac][switch_key]
                        elif switch_key == '12':
                            sw.inventory_state = data_from_url[mac][switch_key]
                        elif switch_key == '13':
                            sw.street = data_from_url[mac][switch_key]
                        elif switch_key == '14':
                            sw.building = data_from_url[mac][switch_key]
                        elif switch_key == '15':
                            sw.porch = data_from_url[mac][switch_key]
                        elif switch_key == '16':
                            sw.floor = data_from_url[mac][switch_key]
                    elif isinstance(data_from_url[mac][switch_key], dict):
                        for port in data_from_url[mac][switch_key]: # loop if their dictionary in properties
                            pt = Port(port)
                            sw.ports.append(pt)
                            for port_prop in data_from_url[mac][switch_key][port]: # loop if their dictionary in upstream switch properties
                                if port_prop == '1':
                                    pt.num = data_from_url[mac][switch_key][port][port_prop]
                                elif port_prop == '2':
                                    pt.upswitch_mac = data_from_url[mac][switch_key][port][port_prop]
                                elif port_prop == '3':
                                    pt.upswitch_port = data_from_url[mac][switch_key][port][port_prop]

                    else:
                        print("Failure: Not string and not dictionary!!!!!")
        else:
            print( "not switch")

    return(switch_dict)


create_list(cubic_switches)
if os.path.isfile(db_file):
    load_from_file(zabbix_switches, db_file)
else:
    zabbix_switches = cubic_switches
    print(type(zabbix_switches))
    save_to_file(zabbix_switches, db_file) # TODO add hash compare of file
# print(cubic_switches.__getinitargs__)

# dump_keys(zabbix_switches)
for x in cubic_switches:
    if x.mac == '7072CF94FD97':
        print x.__name__
        print x.__class__
        print x.__dict__
        print(x.mac)
        if x.ports:
            for y in x.ports:
                print(y.__dict__)
