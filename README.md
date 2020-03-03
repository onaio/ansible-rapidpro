onaio - RapidPro [![Build Status](https://travis-ci.org/onaio/ansible-rapidpro.svg?branch=master)](https://travis-ci.org/onaio/ansible-rapidpro)
=========

Installs and configures [RapidPro](https://rapidpro.github.io/rapidpro/).

Requirements
------------

RapidPro has the following requirements (that aren't set up using this role):
 - [RapidPro Indexer](https://github.com/onaio/ansible-rapidpro-indexer/) (which requires Elasticsearch)
 - PostgreSQL
 - Redis
 - RabbitMQ (optional; if task queuing should be handled by RabbitMQ and not Redis)

Role Variables
--------------
Check the [defaults/main.yml](./defaults/main.yml) file for the full list of default variables.

```yml
# The RapidPro version to be installed
rapidpro_version: v5.0.9

# The domains RapidPro is deployed behind
rapidpro_domains:
  - example.com
rapidpro_domain: "{{ rapidpro_domains[0] }}"

# Whether Courier should be installed
rapidpro_install_courier: true
# The version of Courier to install
rapidpro_courier_version: "1.2.148"

# Whether Mailroom should be installed
rapidpro_install_mailroom: true
# The version of Mailroom to install
rapidpro_mailroom_version: "0.0.195"
```


### Note on Elasticsearch Port

>If Elasticsearch is behind a reverse proxy and using port 80, you'll have to append the port to the HTTP URL such as http://elasticsearch.example.com:80 otherwise port 9200 will be assumed

Dependencies
------------

Here's the list of role dependencies:
 - [onaio.django](https://galaxy.ansible.com/onaio/django)
 - [onaio.courier](https://galaxy.ansible.com/onaio/courier)
 - [onaio.mailroom](https://galaxy.ansible.com/onaio/mailroom)

Example Playbook
----------------

The following example playbook sets up RapidPro, PostgreSQL, and Redis:

```yml
hosts: all
  roles:
    - role: onaio.postgresql
      vars:
        postgresql_version: 10
        postgresql_users:
          - name: rapidpro
            pass: rapidpro
            encrypted: true
        postgresql_databases:
          - name: rapidpro
            owner: rapidpro
            encoding: "UTF-8"
            hstore: true
            gis: true
        postgresql_database_extensions:
          - db: rapidpro
            extensions:
              - postgis
        postgresql_ext_install_postgis: true
        postgresql_ext_postgis_version: "2.5"

    - role: DavidWittman.redis
      vars:
        redis_version: "2.8.9"

    - role: rapidpro
      vars:
        rapidpro_postgresql_password: rapidpro 
```

License
-------

Apache 2.0

