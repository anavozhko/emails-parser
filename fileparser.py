import email


class FileParser(object):

    def __init__(self, filename, delimiter):
        self.filename = filename
        self.delimiter = delimiter

    def iterator(self):
        """
        Method that should iterate file. It is generator.
        """
        with open(self.filename, 'r') as file:
            buf = []
            for line in file:
                if ''.join(buf[-len(self.delimiter):]) == self.delimiter:
                    yield ''.join(buf)
                    buf = []
                else:
                    buf.append(line)
            yield ''.join(buf)

    @staticmethod
    def parse(item):
        """
        Method to parse item data to formated data. Item is a result from iterator.
        Method must return a dictionary.
        :param item: str
        :return: dict
        """
        message = email.message_from_string(item)
        data = {
            "date": message['date'],
            "to": message['to'],
            "from": message['from'],
            "subject": message['subject'],
            # "text": message.get_payload()
        }
        return data

    def start(self):
        """
        Main method
        """
        senders = {}
        for item in self.iterator():
            try:
                m = self.parse(item)
                if not m['from']:
                    continue

                if senders.get(m['from']):
                    senders[m['from']] += 1
                else:
                    senders[m['from']] = 1

                print('{} ({}): {}'.format(m['from'], m['date'], m['subject']))
            except Exception as e:
                print(type(e), e)
                continue

        print()
        for k, v in senders.items():
            print('{}: {}'.format(k, v))
