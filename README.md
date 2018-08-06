# lettuce_rest

---

[![pipeline status](https://gitlab.com/vmeca87/lettuce_rest/badges/master/pipeline.svg)](https://gitlab.com/vmeca87/lettuce_rest/commits/master)

---

BDD-style Rest API testing tool

This repo was inspired on [behave-rest](https://github.com/stanfy/behave-rest) but for a personal need I required to use lettuce so I take all the good ideas from stanfy and implemented the same idea but for lettuce.

## Installation

Run `pip install lettuce_rest` to download package and install required dependencies

But in order to make it works you probability neet o add to your terrain.py 

```python
import lettuce_rest
```


## Running

This is project contains some predefined steps that you can use with lettuce so in order to run test cases with this framework you just need to inovke lettuce in the following way:

```bash
$ lettuce
```

But you can found more information about lettuce here http://lettuce.it/

