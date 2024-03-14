import datetime


class Dive(object):
    def __init__(self):
        self._timeline = []
        self._finish = False
        self._peak = None

    @staticmethod
    def generate(target_depth: int, descent_rate: float, ascent_rate: float):
        dive = Dive()
        dt = datetime.datetime.now()

        for i in range(0, target_depth+1):
            dive.add(dt, i, rate=-descent_rate)
            dt += datetime.timedelta(seconds=1/descent_rate)

        for i in range(target_depth-1, -1, -1):
            dive.add(dt, i, rate=ascent_rate)
            dt += datetime.timedelta(seconds=1/ascent_rate)

        dive.finish()

        return dive

    @property
    def timeline(self):
        return self._timeline

    @property
    def start_time(self):
        return self._timeline[0]['timestamp']

    @property
    def end_time(self):
        return self._timeline[-1]['timestamp']

    def add(self, timestamp, depth, rate=None, temp=None, events=None):
        if self._finish:
            raise Exception("Cannot add, already finished")
        d = {
            "timestamp": timestamp,
            "depth": depth,
        }
        if rate:
            d.update({'rate': rate})

        if temp:
            d.update({'temp': temp})

        if events:
            d.update({'events': events})
        self._timeline.append(d)

    def finish(self):
        # find peak
        peak = None
        for t in self._timeline:
            if peak is None or peak['depth'] < t['depth']:
                peak = t
        self._peak = peak

        # flag as finished
        self._finish = True

    def events_to_annotations(self):
        if not self._finish:
            raise Exception("Cannot annotate unfinished")
        # annotate
        for t in self._timeline:
            events = t.get('events')
            if events:
                for e in events:
                    if e['event_type'] == 'marker' and e['event'] == 'dive_alert' and e['dive_alert'] == 'depth_alert':
                        if 'annotations' not in t:
                            t['annotations'] = []
                        t['annotations'].append("Alert")

    def peak_to_annotation(self, text: str):
        if not self._finish:
            raise Exception("Cannot annotate unfinished")
        for t in self._timeline:
            if t['timestamp'] == self._peak['timestamp']:
                if 'annotations' not in t:
                    t['annotations'] = []
                t['annotations'].append(text)
                return

    def annotate_by_meters(self, meters: float, text: str, ascend=False):
        if not self._finish:
            raise Exception("Cannot annotate unfinished")

        for t in self._timeline:
            ascending = t['timestamp'] > self._peak['timestamp']
            if ascending == ascend and (not ascending and t['depth'] >= meters or ascending and t['depth'] <= meters):

                if 'annotations' not in t:
                    t['annotations'] = []
                t['annotations'].append(text)
                return

    def clean(self):
        self._timeline = self._trim_ends(self._timeline)
        self._timeline = self._fill_ends(self._timeline)

    def get_plot_data(self, with_ts=False):
        xpoints = []
        ypoints = []
        annotations = []
        timestamps = []
        start_ts = self._timeline[0]['timestamp']
        for t in self._timeline:
            x = float((t['timestamp'] - start_ts).total_seconds())
            y = float(-t['depth'])
            xpoints.append(x)
            ypoints.append(y)
            timestamps.append(t['timestamp'])
            for a in t.get('annotations', []):
                annotations.append((a, (x, y)))

        if with_ts:
            return timestamps, xpoints, ypoints, annotations
        else:
            return xpoints, ypoints, annotations

    def _trim_ends(self, timeline):
        if not self._finish:
            raise Exception("Cannot trim unfinished")
        start = None
        end = None
        peak_ts = self._peak['timestamp']
        for i, t in enumerate(timeline):
            depth = t['depth']
            ts = t['timestamp']
            rate = t.get('rate', 0)

            if ts < peak_ts:
                if start is None and depth >= 1:
                    start = i
                elif start is not None and depth < 1:
                    start = None
            else:
                if end is None and depth <= 1:
                    end = i

        if start is None:
            start = 0
        if end is None:
            end = len(timeline) - 1

        return timeline[start:end+1]

    def _fill_ends(self, timeline):
        first = timeline[0]
        last = timeline[-1]

        new_first = {
            'timestamp': first['timestamp'] - datetime.timedelta(seconds=1),
            'depth': 0,
            'rate': 1 * first['depth']
        }

        new_last = {
            'timestamp': last['timestamp'] + datetime.timedelta(seconds=1),
            'depth': 0,
            'rate': 1 * last['depth']
        }
        timeline = [new_first] + timeline + [new_last]
        return timeline