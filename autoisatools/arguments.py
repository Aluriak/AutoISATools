# -*- coding: utf-8 -*-
"""
Post processing of the arguments.

"""
from docopt       import docopt
from autoisatools import info
import csv
import os

ISA_DIR = 'ISA_metadata/isatab_files'
CONTACT_LAST   = 'lastname',
CONTACT_FIRST  = 'firstname',
CONTACT_MID    = 'midinitials',
CONTACT_MAIL   = 'email',
CONTACT_PHONE  = 'phone',
CONTACT_FAX    = 'fax',
CONTACT_ADRESS = 'adress',
CONTACT_AFF    = 'affiliation'


def titled(flag):
    return flag.lstrip('-').replace('-', '_').upper()


def parse_contacts(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        contacts = tuple(
            dictrow
            for dictrow in reader
        )
    # aggregate all contacts in a field:contacts dict.
    try:
        fields = (k for k in next(iter(contacts)))
        return {
            'CONTACT_'+titled(field): "\t".join(
                '"' + contact[field] + '"'
                for contact in contacts
            )
            for field in fields
        }
    except StopIteration:
        from collections import defaultdict
        return defaultdict(tuple)  # empty tuple. Whatever is asked


def parse(args, docstring):
    # get options
    options = docopt(docstring, version=info.VERSION)
    del options['--help']
    del options['--version']
    # post process those that need it
    assert(' ' not in options['--study-shortname'])
    options['--study-id'] = options['--study-id'].replace(' ', '')
    options['--study-id-lower'] = options['--study-id'].lower()
    # the output dir can be given with(out) the 'ISA_metadata/isatab_files',
    #  and with(out) the final '/'.
    options['--output-dir'] = options['--output-dir'].rstrip('/')
    options['--output-dir'] = options['--output-dir'].rstrip(ISA_DIR)
    options['--output-dir'] = options['--output-dir'].rstrip('/')
    options['--output-dir'] = options['--output-dir'] + '/' + ISA_DIR
    # get the CSV data
    assert(os.path.isfile(options['--contacts-file']))
    options.update(parse_contacts(options['--contacts-file']))
    # return it, formated
    return {titled(k):v for k,v in options.items()}
