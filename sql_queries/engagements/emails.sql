-- Clean emails table
create table frank.cleaned_emails as (
	select
		frank.emails.active,
		frank.emails."type",
		frank.emails."timestamp",
		frank.emails.cc,
		frank.emails.bcc,
		frank.emails.subject,
		frank.emails.html,
		frank.emails."text",
		frank.emails.from_email,
		frank.emails.to_email,
		frank.migrated_deals.hubspot_id as dealsIds,
		frank.migrated_contacts.hubspot_id as contactIds,
		frank.migrated_companies.hubspot_id as companyIds
	from 
		frank.emails
	left outer join 
		frank.migrated_deals 
		on 
			frank.migrated_deals.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.emails.deal_id, '') = '' then NULL
        			else frank.emails.deal_id
    			end
   				as DECIMAL)
	left outer join 
		frank.migrated_contacts 
		on 
			frank.migrated_contacts.db_id::BIGINT = frank.emails.contact_id
        	
	left outer join 
		frank.migrated_companies 
		on 
			frank.migrated_companies.db_id::DECIMAL = 
			cast(case
        			when coalesce(frank.emails.account_id, '') = '' then NULL
        			else frank.emails.account_id 
    			end
   				as DECIMAL)
   	);
	
select count(*) from frank.cleaned_emails;
select * from frank.cleaned_emails;

select count(*) from frank.emails;

drop table frank.cleaned_emails;

select * from frank.emails 
where frank.emails.account_id = NULL;
