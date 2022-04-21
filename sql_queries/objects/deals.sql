-- Check the number of rows in the deal
select count(*) from frank.deals;
select * from frank.deals;

--Clean deals data
select 
	"name" as dealname, 
	stage as dealstage, 
	probability::float / 100 as hs_deal_stage_probability,
	sentence,
	postcode,
	website,
	external_id,
	replace(BTRIM(multi_picklist_3, '{}'), ',', ';') as multi_picklist_3
into table 
	frank.first_deals
from 
	frank.deals;

select count(*) from frank.first_deals;
select * from frank.first_deals;

-- Update stages to reflect hubspot stages
update frank.first_deals
set 
	dealstage = replace(replace(replace(replace(
					dealstage,'Negotiating', 'qualifiedtobuy'),
					'Closed Lost', 'closedlost'),
					'Open', 'decisionmakerboughtin'),
					'Closed Won', 'closedwon')
where (dealstage like '%Negotiating' or 
		dealstage like '%Closed Lost' or 
		dealstage like '%Open' or 
		dealstage like '%Closed Won');

	
-- Get rid of duplicates in multi_picklist_3
select
	dealname, 
	dealstage, 
	hs_deal_stage_probability,
	sentence,
	website,
	external_id,
    (SELECT STRING_AGG(DISTINCT p, ';')
    FROM UNNEST(STRING_TO_ARRAY(multi_picklist_3, ';')) AS p
    ) as multi_picklist_3
into table
	frank.cleaned_deals
FROM frank.first_deals

select * from frank.first_deals;
select * from frank.cleaned_deals;
select * from frank.migrated_deals;
select count(*) from frank.first_deals;
select count(*) from frank.cleaned_deals;
select count(*) from frank.migrated_deals;


-- Error Handling
drop table frank.first_deals;
drop table frank.cleaned_deals;
drop table frank.migrated_deals;
