-- Check how many rows are in the original companies table
select COUNT(*) from frank.companies

-- Change table names to huspot properties
SELECT
	"name", 
	cdomain AS domain, 
	street AS address, 
	city, 
	postcode AS zip, 
	phone,
	email as owneremail,
	"text",
	"boolean", 
	external_id
into table 
	frank.cleaned_companies
FROM 
	frank.companies
	
-- Check if the right amount of rows carried over
select count(*) from frank.cleaned_companies;
select * from frank.cleaned_companies;

-- Check if the companies have migrated
select * from frank.migrated_companies;
select count(*) from frank.migrated_companies;

-- Error Handling
drop table frank.cleaned_companies;
drop table frank.migrated_companies;
