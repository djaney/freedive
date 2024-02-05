from garmin_fit_sdk import Decoder, Stream
from freediving.fitfiles.errors import InvalidFitFileError, CorruptedFitFileError
from freediving.fitfiles.session import Session


def fit_to_session(path: str):
    stream = Stream.from_file(path)
    decoder = Decoder(stream)

    if not decoder.is_fit():
        raise InvalidFitFileError

    # This does not mean entire dataset is corrupt
    if not decoder.check_integrity():
        raise CorruptedFitFileError

    messages, errors = decoder.read()

    return Session.from_messages(messages)

