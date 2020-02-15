Deployment
==========

- produkce: [pyconcz-prod.messa.cz](pyconcz-prod.messa.cz)
- beta: [pyconcz-beta.messa.cz](https://pyconcz-beta.messa.cz)


Server
======

Currently running on a [DigitalOcean](https://m.do.co/c/389daec654bc) VM.

Server setup:

```shell
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install --no-install-recommends ansible git
$ sudo ansible-pull \
    --url https://github.com/messa/cz.pycon.org-2020-dev.git \
    --checkout master \
    --verbose \
    deployment/playbook_server_setup.yml
```
