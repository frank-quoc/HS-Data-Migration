--Check number of rows in deals
select count(*) from frank.deals;
select count(*) from frank.migrated_deals;  

-- Join Deals and contacts
create table frank.deals_contacts as (
	select 
		frank.migrated_deals.hubspot_id as deal_id,
		frank.migrated_contacts.hubspot_id as contact_id
	from 
		frank.deals
	inner join frank.migrated_deals on frank.migrated_deals.db_id = frank.deals.external_id::int
	inner join frank.migrated_contacts on frank.migrated_contacts.db_id = frank.deals.contact_id::int);

-- Check table
select count(*) from frank.deals_contacts;
select * from frank.deals_contacts;

-- Error Handling
drop table frank.deals_contacts;
