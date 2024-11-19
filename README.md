![FSI-Logo.png]
# fsi
File System Indexer is an attempt to develop a set of tools for answering the question: Why is my disk full?

The intital goal is to document the adhoc methodology I've been use and begin to morph it into a simple, re-usable workflow.

At this point its more about having an outline for what to do with helpers along the way.

The ultimate goal at this point is to have a standardized data model with easy to use analytics for typical use cases.

# Use Cases
{include fancy images}

## Workflow
* Collect file system metadata
    * Mac
    * Linux
    * Windows
    * HDFS
    * S3
    * Tools
        * NCDU
        * TDU
        * RClone
        * stat
        ```
         stat -f "%d,%i,%p,%l,%Su,%Sg,%r,%z,%a,%m,%c,%B,%k,%b,%#Xf,%N,%Y,%R" files.db
        ```
        * Other?
* Convert to parquet
    * Flatten if needed
    * Target model - need to review union of features from various tools
* Duckdb - describe rationale for focusing on duckdb
    * CLI
    * Notebook
    * Streamlit.IO
* Ideas
    * Process a subset with lambda like use: delete/extract as tar/etc
    * Compare file systems for difference, similarity

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

