import datetime
from freediving.dive.dive import Dive
from freediving.dive.errors import DiveNotFoundError


class Session(object):

    def __init__(self, dives):
        self._dives = dives

    @property
    def length(self):
        return len(self._dives)


    def get_dive(self, index):
        return self._dives[index]

    def get_dive_by_time(self, timestamp):
        # check if time is within a dive, use that
        for dive in self._dives:
            if dive.start_time <= timestamp <= dive.end_time:
                return dive
        # otherwise, check next dive
        for dive in self._dives:
            if timestamp <= dive.start_time:
                return dive
        raise DiveNotFoundError("Cannot find dive")

    @staticmethod
    def from_messages(messages):
        dives = messages['dive_summary_mesgs']
        records = messages['record_mesgs']
        events = messages['event_mesgs']
        dive_objects = []
        for d in dives:
            if d['reference_mesg'] == 'lap':
                dive_objects.append(
                    Session.generate_dive(messages['lap_mesgs'][d['reference_index']], d, records, events)
                )

        return Session(dive_objects)

    @staticmethod
    def generate_dive(lap_data, dive_data, records, events):
        session_start = lap_data['start_time']
        session_end = session_start + datetime.timedelta(seconds=dive_data['bottom_time'])
        dive = Dive()
        for r in records:
            # too early
            if r['timestamp'] < session_start:
                continue
            # too late
            elif r['timestamp'] > session_end:
                break

            # pop events
            record_events = Session._pop_event(events, r['timestamp'])
            dive.add(r['timestamp'], r['depth'], rate=r.get('ascent_rate'), temp=r.get('temperature'),
                     events=record_events)
        dive.finish()
        return dive



    @staticmethod
    def _pop_event(events, timestamp):
        popped = []
        while len(events) > 0:
            e = events[0]
            if e['timestamp'] > timestamp:
                break
            popped.append(events.pop(0))
        return popped
