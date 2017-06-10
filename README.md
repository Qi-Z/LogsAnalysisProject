# LogsAnalysisProject
Udacity Nanodegree Logs Analysis Project

## Installation
1. Install VirtualBox
* Download VirtualBox platform package for your operating system [here](https://www.virtualbox.org/wiki/Downloads)
2. Install Vagrant
* Download [here](https://www.vagrantup.com/downloads.html)
3. Download VM configuration
* [VM files](https://d17h27t6h515a5.cloudfront.net/topher/2017/May/59125904_fsnd-virtual-machine/fsnd-virtual-machine.zip) or clone this [repository](https://github.com/udacity/fullstack-nanodegree-vm)

## Get Started
`git clone https://github.com/Qi-Z/LogsAnalysisProject.git`

`cd LogsAnalysisProject`

`cd vagrant`

`vagrant up`

`vagrant ssh`

Download data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Unzip data you will get `newsdata.sql`

load data into database:

`psql -d news -f newsdata.sql`

`python3 main.py`

## Tutorials
[psql](http://postgresguide.com/utilities/psql.html)

[psycopg2](http://initd.org/psycopg/docs/usage.html)
