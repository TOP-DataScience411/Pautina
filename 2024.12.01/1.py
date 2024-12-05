from datetime import datetime, timedelta, date


def is_vacations(act_date: datetime.date) -> bool: 

	"""Проверяет является ли выбранная дата праздничным днем """

	if 'vacations' in globals():
		for start_vac, period in vacations:
			end_vac = start_vac + period
			if start_vac <= act_date <= end_vac:
				return False
	return True

def schedule(start_date: datetime.date, week: int, /, *weeks: int, sessions: int, format: str = '%d/%m/%Y') -> list[str]:

	"""Создает расписание занятий выбирая нужные дни недели, не включая праздничные дни"""

	lesson_date = []
	actual_date = start_date
	weekdays = [week] + list(weeks)
	

	while len(lesson_date) < sessions:
		if actual_date.isoweekday() in weekdays and is_vacations(actual_date):
			lesson_date.append(actual_date.strftime(format))
		actual_date += timedelta(days = 1)
	return lesson_date
	
# vacations = [ (date(2023, 5, 1), timedelta(weeks=1)), (date(2023, 7, 17), timedelta(weeks=1)), ]
# py321 = schedule(date(2023, 4, 1), 6, 7, sessions = 70)
# len(py321)
#70
# py321[28:32]
#['15/07/2023', '16/07/2023', '29/07/2023', '30/07/2023']
