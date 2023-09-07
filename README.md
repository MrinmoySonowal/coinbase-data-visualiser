# coinbase-data-visualiser
A website to visualise historic and live Coinbase data.

## Install dependencies

### Add permissions to run the install files

#### For mac (or linux based machines)
```sh
chmod u+x install.sh
chmod u+x run.sh
```

### Install conda (Optional)
To install conda go this [link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), then use the ENV.yml file to get the packages into your conda enviroment. This may not entirely work as I was working on conda 4.10

### Install npm
To install npm please follow this [link](https://nodejs.org/en/download/current)

### Run install.sh and then run.sh (from the bash scripts folder or optionally the .ps1 files from the windows installation folder)
Please do so in order

This should install all the dependencies using pip and then run the server client locally.


## Run backend tests
```sh
cd ./backend/tests
python -m unittest client_test.TestClientServer
```
