WITH 

-- removes District of Columbia because it's fips code is not included in the fips csv 
merge_with_fips AS (
SELECT tavg.record, tavg.climdiv_state_id, tavg.county_fips, tavg.jan, tavg.feb, tavg.mar, tavg.apr, fips.state, fips.state_fips, fips.climdiv_state
    FROM [master].[dbo].[climdiv_tmpccy_w_hawaii] AS tavg
    JOIN [master].[dbo].[climdiv_fips_mapping] AS fips
    ON tavg.climdiv_state_id = fips.climdiv_state_id
),

tavg_data as (
SELECT state, state_fips, county_fips, jan, feb, mar, apr
    FROM merge_with_fips
    -- ORDER BY state
)

SELECT tavg_data.state, fips.county AS county, fips.county_full AS place_name, fips.state_fips, fips.county_fips, fips.fips, tavg_data.jan, tavg_data.feb, tavg_data.mar, tavg_data.apr
    FROM tavg_data
    JOIN [master].[dbo].[state_county_fips] AS fips
    ON tavg_data.state_fips = fips.state_fips and tavg_data.county_fips = fips.county_fips