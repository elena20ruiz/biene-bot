import json

from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a mentor intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/mentor/mentor_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        # Log stuff
        log.info('|RESPONSE| Looking for [{}] from JSON element'.format(list_intent[1]))

        array = ['\n'.join(data[list_intent[1]])]
        return array