<p align="center">
   <img src="https://github.com/grantjwc/fsi/blob/main/FSI-Logo.png" width="400">
</p>>

# File System Indexer
This is an attempt to develop a set of tools for answering the question: Why is my disk full?

The intital goal is to document the adhoc methodology I've been use and begin to morph it into a simple, re-usable workflow.

At this point its more about having an outline for what to do with helpers along the way.

The ultimate goal at this point is to have a standardized data model with easy to use analytics for typical use cases.

# Quickstart
* Collect file system info and write to JSON
    * Download rclone from https://rclone.org/downloads/
    * Collect data:
        ```
        rclone lsjson -MR [source] > [output].json
        ```
        * M - metadata: https://rclone.org/docs/#m-metadata
        * R - recursive
* Convert to JSON to parquet
    * Download duckdb from https://duckdb.org/docs/installation
    * Convert JSON to parquet
        ```
        duckdb
        create view json as from 'data.json';
        summarize json;
        copy json to 'data.parquet';
        ```
* Load up the parquet into a view/table
    ```
    duckdb
    create view files as from 'data.parquet';
    summarize files;
    [do crazy sql...]
    ```

# Experiment with parsing metadata
Once you've got the "files" view (or table), lets try parsing out the metadata structure which is by default in a single field.

## Extract the JSON structure:
```
select json_structure(metadata) from files limit 1;
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                         json_structure(metadata)                                         │
│                                                   json                                                   │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"atime":"VARCHAR","btime":"VARCHAR","gid":"VARCHAR","mode":"VARCHAR","mtime":"VARCHAR","uid":"VARCHAR"} │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
With the information displayed, you can access the nested "fields" with:
```

```
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

Nothing to install yet...

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
