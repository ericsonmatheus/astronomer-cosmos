
-- Use the `ref` function to select from other models

with my_second_dbt_model as (

    select 2 as id
    union all
    select 3 as id

)

select *
from my_second_dbt_model