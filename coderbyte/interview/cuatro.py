create table events (
  sensor_id integer not null,
  event_type integer not null,
  value integer not null,
  time timestamp unique not null
);

insert into events
(sensor_id, event_type, value, time)
VALUES
(2,2,5,2014-02-13 12:42:00),
(2,4,-42,2014-02-13 13:19:57),
(2,2,2,2014-02-13 14:48:30),
(3,2,7,2014-02-13 12:54:39),
(2,3,54,2014-02-13 13:32:36);

SELECT sensor_id, event_type, value FROM events
ORDER BY time DESC, sensor_id ASC, event_type ASC
LIMIT 4