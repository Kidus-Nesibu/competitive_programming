class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.calendar:
            if startTime < e and endTime > s:
                return False

        self.calendar.append((startTime, endTime))
        return True