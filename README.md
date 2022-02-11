# NitrotypePy

This package accesses nitrotype's official api along with its unofficial user api. Currently still in development.

## Installation

```sh-session
pip3 install git+https://github.com/RangerEmerald/NitrotypePy
```

or

```sh-session
pip3 install git+https://github.com/RangerEmerald/NitrotypePy@branch-name
```

or 

```sh-session
pip3 install NitrotypePy
```

## About

The endpoints this package uses are `https://www.nitrotype.com/racer/` along with `https://www.nitrotype.com/api/v2/`. The first link is used only to access racer information, while the second one is nitrotype's offical api.

## Usage

Access user information:

```python
from NitrotypePy import user

print(user('corndog')) # Or use any other username. Make sure it is their username, not their display name
```

Get team information:

```python
from NitrotypePy import teams

print(teams('NT')) # Or any other team tag
```

Get top 100 teams:

```python
from NitrotypePy import top

print(top())
```

Get the latest news:

```python
from NitrotypePy import news

print(news()) # Use this to get all the latest news

print(news(234)) # Use this to get the news by its id
```

Access any object from the bootstrap:

```python
from NitrotypePy import bootstrap

print(bootstrap("CASH_SENDING")) # Or any other portion of the bootstrap
```

Access raw api:

```python
from NitrotypePy import api

print(api("")) # Or any other endpoint. For now, this is only a "get" request
```
