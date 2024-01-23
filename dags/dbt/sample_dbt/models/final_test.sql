with 

final_test as (
    select * from {{ ref("my_first_dbt_model") }}
    union
    select * from {{ ref("my_second_dbt_model") }}
)

select * from final_test
