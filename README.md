# DIVA Invenio converter



## How to convert
Makefile provides you a convenient interface with the following commands:

### make
List the available commands:
```bash
make
```
### install
 installs the Python dependencies specified in the requirements.txt file
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


