def model(dbt, session): 
    my_sql_model_df = dbt.ref("my_first_dbt_model")

    return my_sql_model_df