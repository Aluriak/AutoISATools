PYTHON=python3
PKG=autoisatools
OUTPUT_DIR=/udd/lbourneu/ISA_metadata/isatab_files
STUDYSHORT_NAME=GraphCompressionTiso
STUDY_DIR=$(OUTPUT_DIR)/$(STUDYSHORT_NAME)

STUDYNAME=--study-name="Tiso Various Networks Graph Compression"
STUDYSHORT=--study-shortname="$(STUDYSHORT_NAME)"
STUDY_ID=--study-id="PWGTISONGC"
STUDY_DESCRIPTION=--study-description="Lucas Bourneuf's internship (2015). Formal Concepts and ASP programming. Final program is a Python script named PowerGrASP."
OUTPUT=--output-dir=$(OUTPUT_DIR)
CONTACT=--contacts-file=/udd/lbourneu/Documents/autoISAtools/data/contacts.csv
PYDIO=--pydio-url="http://emme.genouest.org/pydio/ws-dyliss/Tisochrysis_lutea_in_silico/GraphCompression/TisoVariousGraphCompression"
ASSAYS_TYPE=--assays-type="Classification_with_Formal_Concepts,Visualization_and_Representation"
ASSAYS_TECH=--assays-tech="FCA_for_proteins,Metabolic_network_representation"
ASSAYS=$(ASSAYS_TYPE) $(ASSAYS_TECH)
TOOL_NAME=--tool-name="Python + Clingo,Cytoscape"
TOOL_VERSION=--tool-version="Python 2.7 + Clingo 4.5.0,2.x"
TOOL_DESCRIPTION=--tool-description="Python-gringo is a pip packaging that allows python to embed clingo,Cytoscape + plugin BIOTEC CyOog"
TOOL=$(TOOL_NAME) $(TOOL_DESCRIPTION) $(TOOL_VERSION)

OPTIONS=$(STUDYNAME) $(STUDYSHORT) $(STUDY_ID) $(STUDY_DESCRIPTION) $(OUTPUT) $(CONTACT) $(PYDIO) $(TOOL) $(ASSAYS)


all: del
	$(PYTHON) -m $(PKG) $(OPTIONS)

del:
	- rm -r $(STUDY_DIR)
