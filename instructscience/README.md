CREATE DATABASE insc;
CREATE USER insc_root WITH PASSWORD 'd3d01e70a29c0f39842cd0c257fb5db9';
ALTER ROLE insc_root SET client_encoding TO 'utf8';
ALTER ROLE insc_root SET default_transaction_isolation TO 'read committed';
ALTER ROLE insc_root SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE insc TO insc_root;
