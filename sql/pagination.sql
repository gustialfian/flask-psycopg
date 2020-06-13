-- limit = 2
-- offset = limit * (page - 1)
-- page = 1 
select * from pagination where type = 'keyword' limit 2 offset 0;
-- page = 2 
select * from pagination where type = 'keyword' limit 2 offset 2;
-- page = 3 
select * from pagination where type = 'keyword' limit 2 offset 4;