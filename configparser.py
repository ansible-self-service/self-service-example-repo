#!/usr/bin/python3
# Datum: 21.05.2021
# Author: dirk.loser@deepl.com
# Funktion: yaml file parsen und validieren
#
import sys,yaml
from cerberus.validator import Validator



class Parser():
    def __init__(self):
        pass


    def parser_schema(self):
        """Return Schema"""
        schema = '''
        categories:
            type: list
        Misc:
            type: list
        
        items:
            type: dict
        description:
            type: string
        categories:
            type: list
        image_url:
            type: string
        playbook:
            type: string
        params:
            type: list
        ansible_become_password:
            type: list
        type:
            type: string
        mandatory:
            type: boolean
        requirements:
            type: string
        '''
        return schema

    def open_config(self,self_service_cfg):
        "Reads self-service.cfg and Validates"
        schema = yaml.safe_load(self.parser_schema())
        with open('{}'.format(self_service_cfg)) as fobj:
            document = yaml.safe_load(fobj)
            vali = Validator(schema)
            if vali.validate(document) == True:
                print(document['categories'])
            else:
                print(vali.errors)



if __name__ == '__main__':
    o = Parser()
    o.open_config(sys.argv[1])
