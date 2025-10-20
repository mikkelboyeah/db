{{ config(materialized = "view") }}

select *
from {{ ref("ssb_data") }}