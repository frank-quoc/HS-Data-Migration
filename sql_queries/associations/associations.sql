select count(*) from frank.deals;

 -- CREATE A TABLE FROM 3 INNER JOINS
create table association_obj as (
	select 
	frank.deals.external_id as deal_id,
	frank.contacts.email,
	frank.companies.cdomain
	from 
		frank.deals 
	inner join frank.contacts on deals.contact_id = frank.contacts.external_id
	inner join frank.companies on deals.account_id::DECIMAL = frank.companies.external_id::DECIMAL);
drop table association_obj;
	
-- INNER JOIN FOR CONTACT AND COMPANY
create table frank.contact_company as (
select 
	frank.contacts.email,
	frank.companies.cdomain
from 
	frank.contacts 
inner join
	frank.companies on contacts.company_id = frank.companies.external_id);   

-- INNER JOIN FOR DEALS AND CONTACTS
create table frank.deals_contacts as (
select 
	frank.contacts.email,
	frank.deals.external_id as deal_id
from 
	frank.deals
inner join 
	frank.contacts on frank.contacts.external_id = deals.contact_id);
-- check table
select * from frank.deals_contacts;
select count(*) from frank.deals_contacts;
-- Error handling
drop table frank.deals_contacts;

-- INNER JOIN FOR DEALS AND COMPANIES
create table frank.deals_companies as (
select 
	frank.deals.external_id as deal_id,
	frank.companies.cdomain
from 
	frank.deals
inner join 
	frank.companies on deals.account_id::DECIMAL = frank.companies.external_id::DECIMAL);
-- check tables
select * from frank.deals_companies;
select count(*) from frank.deals_companies;
-- Error handling
drop table frank.deals_companies;

create table frank.association_table as (
select 
	frank.contacts.email,
	frank.companies.cdomain,
	frank.deals.external_id as deal_id
from 
	frank.contacts 
inner join
	frank.companies on contacts.company_id = frank.companies.external_id
inner join 
	frank.deals on contacts.external_id = frank.deals.contact_id);

select count(*) from frank.contact_company;
drop table contact_company;

-- CONTACT TO COMPANY ASSOCIATION USING MIGRATED TABLE
select
	frank.migrated_contacts.id as contact_id,
	frank.migrated_companies.id as company_id
from
	frank.contact_company
inner join
	frank.migrated_contacts on frank.migrated_contacts.txt_id = frank.contact_company.email
inner join 
	frank.migrated_companies on frank.migrated_companies.txt_id = frank.contact_company.cdomain;

-- DEALS TO CONTACT ASSOCIATION USING MIGRATED TABLE
select
	frank.migrated_contacts.id as contact_id,
	frank.migrated_companies.id as company_id
from
	frank.contact_company
inner join
	frank.migrated_contacts on frank.migrated_contacts.txt_id = frank.contact_company.email
inner join 
	frank.migrated_companies on frank.migrated_companies.txt_id = frank.contact_company.cdomain;
