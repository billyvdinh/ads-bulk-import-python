# ads-bulk-import-python

**To use the utility, please make sure your python version is 3.x.**

## 1. How to use

```commandline
    python main.py {command} {csv_path} [--entity_type {entity_type} ---entity_id {entity_id}]
```

Arguments:
- command: one of **upload**, **print**, required
- csv path: unix path of CSV file to be loaded, required
- entity_type: one of **campaign**, **ad_group**, **ad**, optional
- entity_id: id of entity to be printed, optional

Examples:

Upload Ads from `csv/Book1.csv`, result will be created in `csv/Result.csv` 
```commandline
    python main.py upload csv/Book1.csv
```

Print all campaigns, ad groups, ads from `csv/Book1.csv`
```commandline
    python main.py print csv/Book1.csv
```

Print specific campaign, ad group, ad from `csv/Book1.csv` with entity type and entity id
```commandline
    python main.py print csv/Book1.csv --entity_type ad_group --entity_id 5
```

## 2. How to run tests

```commandline
    python -m unittest discover -s tests
```
