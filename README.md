# Blight of Yggdrasil

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running](#running)
- [Architectural Design](#architectural-design)

## Overview

Norse-themed text adventure game.


## Prerequisites

- [Poetry](https://python-poetry.org/docs)
- (Optional) [Docker Desktop](https://www.docker.com/products/docker-desktop) or an alternative like [OrbStack](https://orbstack.dev/)

## Setup

```bash
poetry install
```

## Running

Server:

```bash
poetry run blight server
```

Client:

```bash
poetry run blight client
```

## Architectural Design

There is a service in the docker compose file called "structurizr" that allows the developer to view the architectural design of the project.

Structurizr `.dsl` files are located in `.design/`; visit https://structurizr.com for more information on the DSL.

To view the designs in structurizr-lite, run the following command:

```bash
docker compose run design
```

Once started, open a browser and navigate to http://localhost:8080

