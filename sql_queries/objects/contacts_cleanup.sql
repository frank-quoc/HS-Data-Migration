-- Get dinstinct value from contacts prefix
select distinct
	prefix
from 
	frank.contacts;

-- Get distince value from contacts picklist
select distinct
	picklist
from
	frank.contacts;

-- Get distinct values from deals multi_picklist_3

select 
	"name",
	BTRIM(multi_picklist_3, '{}') as pick_list
into table
	frank.picklist_3
from
	frank.deals;

-- Get distinct rows (IGNORE THIS WHEN TRYING TO FIND DISTINCT VALUES)
SELECT "name",
       (SELECT STRING_AGG(DISTINCT p, ',')
        FROM UNNEST(STRING_TO_ARRAY(pick_list, ',')) AS tp
       ) as pick_lists
FROM Data;


select * from frank.picklist_3;
select count(*) from frank.picklist_3;
	
-- split into rows
SELECT  
    regexp_split_to_table(frank.picklist_3.pick_list, E',') AS picklist
into table 
	frank.pl_3
from frank.picklist_3;

select * from frank.pl_3;

-- get distinct values
select distinct 
	picklist
from
	frank.pl_3;
	
-- error handling
drop table frank.picklist_3;
drop table frank.pl_3
