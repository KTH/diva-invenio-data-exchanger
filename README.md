![Tests](https://github.com/KTH/diva-invenio-data-exchanger/actions/workflows/test.yml/badge.svg)

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
expected input structure from Diva: [here](tests/fixtures/input/fixture.csv)


### Format
Formats the code using the black code formatter and isort.
```bash
make format
```

### Test
```bash
make test
```

### Contribution Request:
Find TODO, send PR.



### Invenio API
Most likelly we will use [newman](https://www.npmjs.com/package/newman) it's a free command-line collection runner for Postman, it can generate reports and take care of the API requests part.

## Resources:
### [Invenio docs](https://inveniordm.docs.cern.ch/reference/metadata/)


### [Pandas docs](https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html)



### [Invenio record schema](https://github.com/inveniosoftware/invenio-rdm-records/blob/6d7758714d08be9317bed5d402fc09731f71bf3d/invenio_rdm_records/records/jsonschemas/records/record-v6.0.0.json)