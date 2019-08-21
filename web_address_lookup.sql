CREATE DATABASE web_address_lookup;

CREATE TABLE address_input (
address_id INT
web_address text, 
needs_lookup INT
);

CREATE TABLE address_output (
address_id INT, 
http_response_code INT, 
redirected_to_url text,
html text, 
lookup_timestamp DATETIME
);

