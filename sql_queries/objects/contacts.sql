select COUNT(*) from frank.contacts;

SELECT 
	first_name AS firstname, 
    last_name AS lastname, 
    street AS address, 
    city, 
    postcode AS zip, 
    phone, 
    phone_2 AS mobilephone, 
    email, 
    email_2 as work_email,
    company,
    prefix,
    external_id,
    picklist 
into frank.cleaned_contacts 
FROM 
    frank.contacts;
    
drop table frank.cleaned_contacts;
