CREATE TABLE IF NOT EXISTS pagination(
	id serial PRIMARY KEY,
  type VARCHAR (50),
	name VARCHAR (50) 
);

insert into pagination (type, name) 
  values
    ('champion', 'ashe'),
    ('champion', 'garen'),
    ('champion', 'hecarim'),
    ('champion', 'tresh'),
    ('champion', 'kalista'),
    ('champion', 'maokai'),
    ('champion', 'elise'),
    ('champion', 'zed'),
    ('keyword', 'edure'),
    ('keyword', 'ephemeral'),
    ('keyword', 'revival'),
    ('keyword', 'kill'),
    ('keyword', 'died');