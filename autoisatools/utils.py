"""
Definition of some utils functions

"""
DIR_DATA      = 'data'
DIR_TEMPLATES = DIR_DATA + '/templates'


# because all data is not uniformized
def special_cases_assay_tech(name):
    if 'FCA for proteins' in name:
        return name.replace(' ', '_')
    return name



