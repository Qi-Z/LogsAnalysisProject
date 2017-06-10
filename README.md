# LogsAnalysisProject
Udacity Nanodegree Logs Analysis Project

3 questions to answer:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

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

## Design
Source code in `main.py`

Basically, it uses `psycopg2` module to perform query on Postgresql database

Output in `output.txt`

## Style
Use pep8 tool to check style
`pep8 main.py`

## Tutorials
[psql](http://postgresguide.com/utilities/psql.html)

[psycopg2](http://initd.org/psycopg/docs/usage.html)
