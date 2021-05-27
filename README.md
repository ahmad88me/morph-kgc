<p align="center">
<img src="https://github.com/oeg-upm/morph-website/blob/master/morph-group/src/assets/logo.png" height="100" alt="morph">
</p>

Morph-KGC is an engine that constructs [RDF](https://www.w3.org/TR/rdf11-concepts/) knowledge graphs from heterogeneous data sources with [R2RML](https://www.w3.org/TR/r2rml/) and [RML](https://rml.io/specs/rml/) mapping languages. Morph-KGC is built on top of [pandas](https://pandas.pydata.org/) and it leverages *mapping partitions* to significantly reduce execution times and memory consumption for large data sources.

**Citing Morph-KGC**: If you used Morph-KGC in your work, please cite the [ISWC 2021 paper]():

```bib
@inproceedings{arenas2021Morph,
  title = {{Morph-KGC: Scalable Knowledge Graph Construction with Mapping Partitions}},
  author = {Arenas-Guerrero, Julián and Chaves-Fraga, David and Corcho, Oscar},
  booktitle = {International Semantic Web Conference},
  pages = {94--102},
  year = {2017},
  organization = {Springer, Cham},
  doi = {},
}
```

## Supported Data Formats

- Input data formats:
  - Relational databases: [MySQL](https://www.mysql.com/), [PostgreSQL](https://www.postgresql.org/).
  - Tabular files: [CSV](https://en.wikipedia.org/wiki/Comma-separated_values), [TSV](https://en.wikipedia.org/wiki/Tab-separated_values), [DSV](https://en.wikipedia.org/wiki/Delimiter-separated_values), [Excel](https://en.wikipedia.org/wiki/Microsoft_Excel), [Parquet](https://parquet.apache.org/documentation/latest/).
- Output RDF serializations: [N-Triples](https://www.w3.org/TR/n-triples/), [N-Quads](https://www.w3.org/TR/n-quads/).

## Getting Started

Morph-KGC is runned using a configuration file. Examples of `config` files can be found [here](https://github.com/oeg-upm/Morph-KGC/tree/main/examples).

## Wiki

## Authors

- Julián Arenas-Guerrero (julian.arenas.guerrero@upm.es)
- David Chaves-Fraga
- Jhon Toledo
- Oscar Corcho

Ontology Engineering Group, Universidad Politécnica de Madrid | 2020 - Present
