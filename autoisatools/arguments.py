# -*- coding: utf-8 -*-
"""
Post processing of the arguments.

"""
from docopt       import docopt
from autoisatools import utils
from autoisatools import info
from collections  import OrderedDict
import shutil
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
    options['--study-lowid'] = options['--study-id'].lower()
    options['--assays-type'] = '"' + '"\t"'.join(options['--assays-type'].split(',')) + '"'
    options['--assays-tech'] = '"' + '"\t"'.join(options['--assays-tech'].split(',')) + '"'
    options['--assays-nodata'] = '"' + '"\t"'.join(
        '' for _ in range(1+options['--assays-type'].count('\t'))
    ) + '"' 
    # create the assay file list
    assay_file_name = 'a_STUDY_LOWID_ASSAY_NAME_ASSAY_TECHNO.txt'
    # print('TEST:', options['--assays-tech'], tuple(
        # (name, techno)
        # for name, techno in zip(options['--assays-type'].split("\t"),
                                # options['--assays-tech'].split("\t"))
    # ))
    assay_files = (
        '"' + assay_file_name.replace('ASSAY_NAME', name).replace('ASSAY_TECHNO', techno) + '"'
        for name, techno in zip(options['--assays-type'].split("\t"),
                                options['--assays-tech'].split("\t"))
    )
    assay_files = (  # remove the double quotes inside, but surround the final name by quotes
        '"' + filename.replace('"', '') + '"'
        for filename in assay_files
    )
    options['--assays-files'] = '\t'.join(assay_files).replace(
        'STUDY_LOWID', options['--study-lowid'])
    # get the assays subdata with space instead of underscore
    options['--assays-tech'] = options['--assays-tech'].replace('_', ' ')
    options['--assays-type'] = options['--assays-type'].replace('_', ' ')
    # take count of exceptions
    options['--assays-tech'] = '\t'.join(
        utils.special_cases_assay_tech(name)
        for name in options['--assays-tech'].split('\t')
    )
    # the output dir can be given with(out) the 'ISA_metadata/isatab_files',
    #  and with(out) the final '/'.
    options['--output-dir'] = options['--output-dir'].rstrip('/')
    options['--output-dir'] = options['--output-dir'].rstrip(ISA_DIR)
    options['--output-dir'] = options['--output-dir'].rstrip('/')
    options['--output-dir'] = options['--output-dir'] + '/' + ISA_DIR
    # get the CSV data
    assert(os.path.isfile(options['--contacts-file']))
    options.update(parse_contacts(options['--contacts-file']))
    # create assay files
    for filename in options['--assays-files'].split("\t"):
        shutil.copy(
            os.path.join(utils.DIR_TEMPLATES, 'a_STUDY_LOWID_ASSAY_NAME.txt'),
            os.path.join(utils.DIR_TEMPLATES, filename.replace('"', '')),
        )

    # return it, formated
    return {titled(k):v for k,v in options.items()}
