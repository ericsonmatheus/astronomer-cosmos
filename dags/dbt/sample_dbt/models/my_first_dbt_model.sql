
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

with my_first_dbt_model as (

    select 1 as id
    union all
    select null as id

)

select *
from my_first_dbt_model

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
