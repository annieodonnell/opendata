import datetime


def date_generator(start, days):
  dt = start
  while dt < start + datetime.timedelta(days = days):
    yield dt
    dt = dt + datetime.timedelta(days=1)


ref = datetime.datetime(2012,01,01)
for dt in date_generator(ref, 365):
	print dt