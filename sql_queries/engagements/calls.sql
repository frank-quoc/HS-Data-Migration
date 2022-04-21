-- Clean calls table
create table frank.cleaned_calls as (
	select
		frank.calls.active,
		frank.calls."type",
		frank.calls."timestamp",
		frank.calls."toNumber",
		frank.calls."fromNumber",
		frank.calls.status,
		frank.calls."durationMilliseconds",
		frank.calls."recordingUrl",
		frank.calls.body, 
		frank.migrated_deals.hubspot_id as dealsIds,
		frank.migrated_contacts.hubspot_id as contactIds,
		frank.migrated_companies.hubspot_id as companyIds
	from 
		frank.calls
	left outer join 
		frank.migrated_deals 
		on 
			frank.migrated_deals.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.calls.deal_id, '') = '' then NULL
        			else frank.calls.deal_id
    			end
   				as DECIMAL)
	left outer join 
		frank.migrated_contacts 
		on 
			frank.migrated_contacts.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.calls.contact_id, '') = '' then NULL
        			else frank.calls.contact_id
    			end
   				as DECIMAL)
	left outer join 
		frank.migrated_companies 
		on 
			frank.migrated_companies.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.calls.account_id, '') = '' then NULL
        			else frank.calls.account_id 
    			end
   				as DECIMAL)
   	);
	
select count(*) from frank.cleaned_calls;
select * from frank.cleaned_calls;

select count(*) from frank.calls;

drop table frank.cleaned_calls;

select * from frank.calls 
where frank.calls.account_id = NULL;

select * from frank.cleaned_calls
where "recordingUrl" = 'https://wyatt-jones.org/';

select count("recordingUrl") from frank.cleaned_calls;

select *  
into table frank.cleaned_calls_2
from frank.cleaned_calls; 

select row_number() over(), *  -- notice: no fields are needed
into table frank.cleaned_calls_2
from frank.cleaned_calls;

select * from frank.cleaned_calls_2
where "recordingUrl" = 'http://www.phelps-vega.com/';

select * from frank.calls
where "recordingUrl" = 'http://www.phelps-vega.com/';
