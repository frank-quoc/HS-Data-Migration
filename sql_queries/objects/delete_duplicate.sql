-- Find the duplicate value
SELECT external_id, count(*)
FROM frank.contacts
GROUP BY external_id
HAVING COUNT(*) > 1;

-- Duplicates had an external_id = 102000

-- Create a table to modify
select 
	*
into table 
	frank.contacts_f
from 
	frank.contacts;

-- Find all rows with external_id  =  102000
select * from frank.contacts
where frank.contacts.external_id = 102000;
select count(*) from frank.contacts_f;

-- Decided to delete the row with the following email
delete from frank.contacts_f
where email = 'jowar84@summerscochran.com';

select count(*) from frank.contacts_f;
