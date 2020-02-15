Deployment
==========

- produkce: [pyconcz-prod.messa.cz](pyconcz-prod.messa.cz)
- beta: [pyconcz-beta.messa.cz](https://pyconcz-beta.messa.cz)


Server setup
============

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

Next, the websites can be deployment by running the scripts created by the `playbook_server_setup.yml` above:

- `sudo /srv/deploy_pyconcz_2020_beta.sh`
- `sudo /srv/deploy_pyconcz_2020_prod.sh`

The operating system user `pyconcz-github` has SSH allowed_keys set up so the website deploy scripts can be run through **Github Actions**.


Firewall
========

The server is protected by firewall managed by DigitalOcean outside of the VM (Droplet) itself. Only ports 22, 25, 80, 443 are accessible from the Internet.
