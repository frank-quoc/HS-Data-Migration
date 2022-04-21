--Check number of rows in deals
select count(*) from frank.deals;
select count(*) from frank.migrated_deals;
select count(*) from frank.companies;
select count(*) from frank.migrated_companies;

-- Join Deals and companies
create table frank.deals_companies as (
	select 
		frank.migrated_deals.hubspot_id as deal_id,
		frank.migrated_companies.hubspot_id as company_id
	from 
		frank.deals
	inner join frank.migrated_deals on frank.migrated_deals.db_id = frank.deals.external_id::int
	inner join frank.migrated_companies on frank.migrated_companies.db_id::decimal = frank.deals.account_id::decimal);

-- Check table
select count(*) from frank.deals_companies;
select * from frank.deals_companies;

-- Error Handling
drop table frank.deals_companies;
