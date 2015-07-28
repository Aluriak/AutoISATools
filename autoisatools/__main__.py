# -*- coding: utf-8 -*-
"""
usage:
    __main__.py [options]

options:
    --help, -h
    --version, -v
    --study-shortname=STR           Name of the study, only alphanumeric
    --study-name=STR                Detailed name of the study
    --study-id=STR                  Unique ID (no space, alphanumeric)
    --description=STR               Detailed description
    --output-dir=FILE               Path to ISA_metadata/isatab_files
    --contacts-file=FILE            CSV contacts file (see README for format)
    --pydio-url=STR                 URL of the data in Pydio
    --tool=STR                      Used tools
    --tool-version=STR              Versions used
    --tool-description=STR          Comments, addendum,…
    --assays-type=STR[,STR]         Assays type (one per assay)
    --assays-tech=STR[,STR]         Assays techno (one per assay)


"""


from autoisatools import arguments
from autoisatools import utils
import sys
import os

def postprocess(payload, string):
    """Operate a postprocessing on given string

    Ex: the string "the project is named STUDYNAME" is replaced by
        "the project is named A very very long title"
        if the project name is "A very very long title".

    """
    # print('IN :', string)
    for field, value in payload.items():
        string = string.replace(field, value)
    # print('OUT:', string)
    # print(payload)
    return string



def create_isa_data(payload):
    """Create the isa package according to all given options

    Payload is the data parsed by arguments package

    """
    # Create the main repertory and copy the template inside
    maindir = os.path.join(payload['OUTPUT_DIR'], payload['STUDY_SHORTNAME'])
    os.mkdir(maindir)
    for filename in os.listdir(utils.DIR_TEMPLATES):
        if 'ASSAY_NAME' in filename: continue  # avoid keeping the model of assays files
        pre_filename  = os.path.join(utils.DIR_TEMPLATES, filename)
        post_filename = os.path.join(maindir, postprocess(payload, filename))
        # exit()
        with open(pre_filename) as fi, open(post_filename, 'w') as fo:
            [fo.write(postprocess(payload, line)) for line in fi]
    # remove intermediate template files
    for filename in os.listdir(utils.DIR_TEMPLATES):
        if filename.startswith('a_'):
            if filename != 'a_STUDY_LOWID_ASSAY_NAME.txt':
                os.remove(os.path.join(utils.DIR_TEMPLATES, filename))





if __name__ == '__main__':
    create_isa_data(arguments.parse(sys.argv, __doc__))



