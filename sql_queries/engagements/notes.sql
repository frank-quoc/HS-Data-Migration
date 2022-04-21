-- Clean notes table
create table frank.cleaned_notes as (
	select
		frank.notes.active,
		frank.notes."type",
		frank.notes."timestamp",body
		frank.notes.body, 
		frank.migrated_deals.hubspot_id as dealsIds,
		frank.migrated_contacts.hubspot_id as contactIds,
		frank.migrated_companies.hubspot_id as companyIds
	from 
		frank.notes
	left outer join 
		frank.migrated_deals 
		on 
			frank.migrated_deals.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.notes.deal_id, '') = '' then NULL
        			else frank.notes.deal_id
    			end
   				as DECIMAL)
	left outer join 
		frank.migrated_contacts 
		on 
			frank.migrated_contacts.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.notes.contact_id, '') = '' then NULL
        			else frank.notes.contact_id
    			end
   				as DECIMAL)
	left outer join 
		frank.migrated_companies 
		on 
			frank.migrated_companies.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.notes.account_id, '') = '' then NULL
        			else frank.notes.account_id 
    			end
   				as DECIMAL)
   	);
	
select count(*) from frank.cleaned_notes;
select * from frank.cleaned_notes;

select count(*) from frank.notes;

drop table frank.cleaned_notes;
