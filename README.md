# DIVA Invenio data exchanger
The DIVA Invenio Data Exchanger is a Python-based tool designed to facilitate data exchange between the DIVA and Invenio systems.
The tool provides a seamless way to move data between these two systems, making it easy to convert Diva data into Invenio platform and vice versa.
## prerequisites:
Make sure your virtual environment is set up.

## How to convert
Makefile provides you a convenient interface with the following commands:

### make
List the available commands:
```bash
make
```
### install
Installs the Python dependencies specified in the requirements.txt file
```bash
make install
```

### run
Runs the main.py Python script with the input and output arguments provided as command line arguments.
```bash
make run input=data/input/pub.csv output=data/output/pub.json
```

### Format
Formats the code using the black code formatter.
```bash
make format
```

### Contribution Request:
Find TODO, send PR.



### builder class where it build the request body
https://inveniordm.docs.cern.ch/reference/metadata/

### Pandas docs:
https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html


### Invenio record schema
https://github.com/inveniosoftware/invenio-rdm-records/blob/6d7758714d08be9317bed5d402fc09731f71bf3d/invenio_rdm_records/records/jsonschemas/records/record-v6.0.0.json