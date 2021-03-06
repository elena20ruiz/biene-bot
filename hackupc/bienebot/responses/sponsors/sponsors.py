import json

from hackupc.bienebot.responses.error import error
from hackupc.bienebot.util import log


# noinspection PyBroadException
def get_message(response_type):
    """
    Return a message from a sponsor intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/sponsors/sponsors_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')
        entities = response_type['entities']

        # Log stuff
        if entities:
            entity = entities[0]['entity']
            log_info = f'|RESPONSE| About [{entity}] getting [{list_intent[1]}]'
        else:
            log_info = f'|RESPONSE| Getting [{list_intent[1]}] about all sponsors'
        log.debug(log_info)

        switcher = {
            'Which': which_sponsor,
            'Help': help_sponsor,
            'AllChallenges': all_challenges_sponsor,
            'Where': where,
            'Challenge': challenge,
            'Contact': contact
        }
        # Get the function from switcher dictionary
        func = switcher.get(list_intent[1], lambda: error.get_message())
        # Execute the function
        return func(data, entities)


# noinspection PyUnusedLocal
def which_sponsor(data, entities):
    """
    Retrieve response for `which` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses.
    """
    response = '{}\n'.format(data['default']['total'])
    for value in data['sponsors'].values():
        response += '- {}\n'.format(value['name'])
    array = [response]
    return array


# noinspection PyUnusedLocal
def help_sponsor(data, entities):
    """
    Retrieve response for `help` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses.
    """
    return ['\n'.join(data['Help'])]


# noinspection PyUnusedLocal
def all_challenges_sponsor(data, entities):
    """
    Retrieve response for `all_challenges` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses.
    """
    return ['\n'.join(data['AllChallenges'])]


def where(data, entities):
    """
    Retrieve response for `where` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses.
    """
    array = []
    if entities:
        sponsor = entities[0]['entity'].lower()
        log.debug(f'|RESPONSE|: About [{sponsor}] getting WHERE')
        array.append(data['sponsors'][sponsor]['where'])
    else:
        array.append(data['default']['where'])
    return array


def challenge(data, entities):
    """
    Retrieve response for `challenge` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses.
    """
    array = []
    if entities:
        sponsor = entities[0]['entity'].lower()
        log.debug(f'|RESPONSE|: About [{sponsor}] getting CHALLENGE')
        array.append(data['sponsors'][sponsor]['challenge'])
    else:
        array.append(data['default']['challenge'])
    return array


def contact(data, entities):
    """
    Retrieve response for `contact` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses.
    """
    array = []
    if entities:
        sponsor = entities[0]['entity'].lower()
        log.debug(f'|RESPONSE|: About [{sponsor}] getting CONTACT')
        array.append(data['sponsors'][sponsor]['contact'])
    else:
        array.append(data['default']['contact'])
    return array
