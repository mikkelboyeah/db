
{{ config(materialized='table', enabled=false) }}

select *
from {{ ref('my_first_python_model') }}
where id = 1
