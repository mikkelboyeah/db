{% docs ssb_data %}
# ssb_data

This model imports data from the SSB API using pyjstat. It demonstrates how to fetch, parse, and store external statistical data in your analytics platform using dbt Python models.

- Source: [SSB API](https://data.ssb.no/api/v0/no/table/11342)
- Data is materialized as a table in DuckDB.
- For more details, see the Python model in `ssb_data.py`.

{% enddocs %}

{% docs consume_ssb_data %}
# consume_ssb_data

This model demonstrates how to reference the `ssb_data` model using dbt's `ref` function. It serves as an example of building downstream models that depend on external data sources ingested via Python models.

- Depends on: `ssb_data`
- Materialized as a table in DuckDB.

{% enddocs %} 