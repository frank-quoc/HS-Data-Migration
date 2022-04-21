-- Clean tasks table
create table frank.cleaned_meetings as (
	select
		frank.tasks.active,
		frank.tasks."type",
		frank.tasks."timestamp",
		frank.tasks.body, 
		frank.tasks."startTime", 
		frank.tasks."endTime", 
		frank.tasks.title,
		frank.migrated_deals.hubspot_id as dealsIds,
		frank.migrated_contacts.hubspot_id as contactIds,
		frank.migrated_companies.hubspot_id as companyIds
	from 
		frank.tasks
	left outer join 
		frank.migrated_deals 
		on 
			frank.migrated_deals.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.tasks.deal_id, '') = '' then NULL
        			else frank.tasks.deal_id
    			end
   				as DECIMAL)
	left outer join 
		frank.migrated_contacts 
		on 
			frank.migrated_contacts.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.tasks.contact_id, '') = '' then NULL
        			else frank.tasks.contact_id
    			end
   				as DECIMAL)
	left outer join 
		frank.migrated_companies 
		on 
			frank.migrated_companies.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.tasks.account_id, '') = '' then NULL
        			else frank.tasks.account_id 
    			end
   				as DECIMAL)
   	);
   
update frank.cleaned_meetings
set 
	"type" = replace("type",'TASK', 'MEETING')			
where ("type" like '%TASK');
	
select count(*) from frank.cleaned_meetings;
select * from frank.cleaned_meetings;

select count(*) from frank.tasks;

drop table frank.cleaned_meetings;
