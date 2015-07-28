PYTHON=python3
PKG=autoisatools
OUTPUT_DIR=/home/michel/ISA_metadata/isatab_files
STUDYSHORT_NAME=ALittleTitleYouWillRecognize
STUDY_DIR=$(OUTPUT_DIR)/$(STUDYSHORT_NAME)

STUDYNAME=--study-name="A very very long title"
STUDYSHORT=--study-shortname="$(STUDYSHORT_NAME)"
STUDY_ID=--study-id="AnUniqueIDWithoutSpace"
DESCRIPTION=--description="A very long description of the study"
OUTPUT=--output-dir=$(OUTPUT_DIR)
CONTACT=--contacts-file=/home/michel/Documents/autoISAtools/data/contacts.csv
PYDIO=--pydio-url="http://emme.genouest.org/pydio/ws-dyliss/Escherichia%20coli/GraphCompression"

OPTIONS=$(STUDYNAME) $(STUDYSHORT) $(STUDY_ID) $(DESCRIPTION) $(OUTPUT) $(CONTACT) $(PYDIO)


all: del
	$(PYTHON) -m $(PKG) $(OPTIONS)

del:
	- rm -r $(STUDY_DIR)
