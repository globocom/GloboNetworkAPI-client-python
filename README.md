# GloboNetworkAPI python client

This project is the python implementation of a [GloboNetworkAPI](https://github.com/globocom/GloboNetworkAPI) client library.

### Installation

Install the project by running:
```bash
$> pip install GloboNetworkAPI
```

### Contributing

We are not stringent with contributions. Just fork, modify, write tests and send us a Pull Request :)

For development purpose, setup your environment by installing project and development dependencies:
```bash
$> make setup
```

### Testing
Tests are divided into Integration, Functional and Unit tests. They are located inside tests directory.
To run tests, first install tests dependencies by running:
```bash
$> make test_setup
```
It will download and run GloboNetworkAPI using vagrant.
After that, just run the tests using:
```bash
$> make test
```

### Releasing new version

Before releasing new version, don't forget to update the version you want. After this, run:

```bash
$> make publish
```

You can not upload the same version twice.
