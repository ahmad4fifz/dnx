<div align=center>

# dnx

API for dnx using Flask, Flask-RESTX

</div>

## Pre-requisites

This API make use of `dnstwist` as its engine and `MongoDB` as its database, make sure you have it installed. `python3-venv` is recommended to help manage the virtual environment.

It uses [Black](https://github.com/psf/black) for code styling/formatting.

## Installation

```bash
# Clone the project repository.
git clone https://github.com/ahmad4fifz/dnx.git

# Change directory to dnx and initialize the virtual environment.
cd dnx
python3 -m venv venv
source venv/bin/activate

# Install the requirements.
pip install -r src/requirements.txt

# Run the app.
flask run
```

The API can be access on `http://localhost:5000/api/v1/`.

> If `localhost:5000` can't access, try run this: `flask run --host=0.0.0.0`
>
> The API can be access on `http://<host_ip>:5000/api/v1/`.

## Deployment

### `docker-compose`

```bash
  docker-compose up --build -d
```

The API can be access on `http://<host_ip>:8000/api/v1/`.

## API Reference

### View docs

```http
  GET /api/v1/docs/
```

### Query domain instantly

```http
  GET /api/v1/domain/query/
```

| Parameter | Type     | Description                   |
| :-------- | :------- | :---------------------------- |
| `domain`  | `string` | **Required**. Domain with TLD |

## FAQ

### GeoIP error during dnstwist installation

```bash
    ERROR: Command errored out with exit status 1:
     command: /dnx/venv/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-8yexy2fc/geoip_98c22066a35540ee809288d527a059e0/setup.py'"'"'; __file__='"'"'/tmp/pip-install-8yexy2fc/geoip_98c22066a35540ee809288d527a059e0/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /tmp/pip-record-r7vqlyng/install-record.txt --single-version-externally-managed --compile --install-headers /dnx/venv/include/site/python3.9/GeoIP
         cwd: /tmp/pip-install-8yexy2fc/geoip_98c22066a35540ee809288d527a059e0/
    Complete output (15 lines):
    /usr/lib/python3.9/distutils/dist.py:274: UserWarning: Unknown distribution option: 'bugtrack_url'
      warnings.warn(msg)
    Warning: 'classifiers' should be a list, got type 'tuple'
    running install
    running build
    running build_ext
    building 'GeoIP' extension
    creating build
    creating build/temp.linux-x86_64-3.9
    x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I/dnx/venv/include -I/usr/include/python3.9 -c py_GeoIP.c -o build/temp.linux-x86_64-3.9/py_GeoIP.o
    py_GeoIP.c:23:10: fatal error: GeoIP.h: No such file or directory
       23 | #include "GeoIP.h"
          |          ^~~~~~~~~
    compilation terminated.
    error: command '/usr/bin/x86_64-linux-gnu-gcc' failed with exit code 1
    ----------------------------------------
ERROR: Command errored out with exit status 1: /dnx/venv/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-8yexy2fc/geoip_98c22066a35540ee809288d527a059e0/setup.py'"'"'; __file__='"'"'/tmp/pip-install-8yexy2fc/geoip_98c22066a35540ee809288d527a059e0/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /tmp/pip-record-r7vqlyng/install-record.txt --single-version-externally-managed --compile --install-headers /dnx/venv/include/site/python3.9/GeoIP Check the logs for full command output.

```

> Fix: Install `libgeoip-dev` package.

```bash
sudo apt install libgeoip-dev -y
```

## License

[MIT](LICENSE)
