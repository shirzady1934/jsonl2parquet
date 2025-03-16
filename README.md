# JSONL to Parquet Converter with PySpark

This project contains a function to read large multipart JSONL files and convert them to Parquet format using PySpark.

## Overview

- **Input Format:** JSONL (JSON Lines)
- **Output Format:** Parquet
- **Technology Used:** PySpark

The function `convert_jsonl_to_parquet()` reads JSONL files from a specified directory, converts them into a DataFrame, and then saves them in Parquet format for optimized storage and faster querying. It also handles large files efficiently with configurable memory settings.

## Features

- Reads large JSONL files, including multipart (using wildcards for file paths).
- Converts data to Parquet format for efficient storage.
- Configurable memory for both Spark executor and driver to handle large datasets.
- Provides a schema overview and sample rows of the data.

## Prerequisites

Before running the script, ensure you have the following installed:

- Apache Spark (with PySpark)
- Python 3.x
- Java 8 or higher (required by Spark)
  
You can install PySpark using pip:

```bash
pip install pyspark
```

You can run the code using python:

```bash
python main.py
```

