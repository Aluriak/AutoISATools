PYTHON=python3
PKG=autoisatools
OUTPUT_DIR=/udd/lbourneu/ISA_metadata/isatab_files
STUDYSHORT_NAME=ALittleTitleYouWillRecognize
STUDY_DIR=$(OUTPUT_DIR)/$(STUDYSHORT_NAME)

STUDYNAME=--study-name="A very very long title"
STUDYSHORT=--study-shortname="$(STUDYSHORT_NAME)"
STUDY_ID=--study-id="AnUniqueIDWithoutSpace"
DESCRIPTION=--description="A very long description of the study"
OUTPUT=--output-dir=$(OUTPUT_DIR)
CONTACT=--contacts-file=/udd/lbourneu/Documents/autoISAtools/data/contacts.csv
PYDIO=--pydio-url="http://emme.genouest.org/pydio/ws-dyliss/Escherichia%20coli/GraphCompression"
ASSAYS_TYPE=--assays-type="Classification_with_Formal_Concepts,Visualization_and_Representation"
ASSAYS_TECH=--assays-tech="FCA_for_proteins,Metabolic_network_representation"
ASSAYS=$(ASSAYS_TYPE) $(ASSAYS_TECH)
TOOL=--tool="Python + Clingo"
TOOL_VERSION=--tool-version="Python 3.5 + Clingo 4.5.0"
TOOL_DESCRIPTION=--tool-description="its amazing"

OPTIONS=$(STUDYNAME) $(STUDYSHORT) $(STUDY_ID) $(DESCRIPTION) $(OUTPUT) $(CONTACT) $(PYDIO) $(TOOL) $(TOOL_VERSION) $(TOOL_DESCRIPTION) $(ASSAYS)


all: del
	$(PYTHON) -m $(PKG) $(OPTIONS)

del:
	- rm -r $(STUDY_DIR)
