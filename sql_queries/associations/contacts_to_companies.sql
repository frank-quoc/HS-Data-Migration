--Check number of rows in deals
select count(*) from frank.contacts_f;
select count(*) from frank.migrated_contacts;
select count(*) from frank.companies;
select count(*) from frank.migrated_companies;

-- Join contacts and companies
create table frank.contacts_companies as (
	select 
		frank.migrated_contacts.hubspot_id as contacts_id,
		frank.migrated_companies.hubspot_id as company_id
	from 
		frank.contacts_f
	inner join frank.migrated_contacts on frank.migrated_contacts.db_id = frank.contacts_f.external_id
	inner join frank.migrated_companies on frank.migrated_companies.db_id = frank.contacts_f.company_id);

-- Check table
select * from frank.contacts_companies;
select count(*) from frank.contacts_companies;

-- Error Handling
drop table frank.contacts_companies;

-- Check number of rows in associated deals and contacts column 
select count(*) from frank.contacts_companies;
select * from frank.contacts_companies;

-- Find duplicates
SELECT
    external_id, external_id
    COUNT( external_id )
FROM
    frank.contacts 
GROUP BY
    external_id 
HAVING
    COUNT( external_id )> 1
ORDER BY
    external_id;
   
SELECT
    contacts_id, 
    external_id,
    COUNT( contacts_id )
FROM
    frank.contacts_companies 
GROUP BY
    contacts_id,
    external_id
HAVING
    COUNT( contacts_id )> 1
ORDER BY
    contacts_id;
