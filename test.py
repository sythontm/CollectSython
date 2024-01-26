import os
from git import Repo

try:
    with open(filename, 'r') as f:
        data = json.load(f)
        api_id = data['api_id']
        api_hash = data['api_hash']
        bot_token = data['bot_token']
        DEVLOO = data['DEVLOO']
        MAX_ACCOUNTS = data['MAX_ACCOUNTS']
        id_bot = bot_token.split(':')[0]  # Extract id_bot from bot_token

        # Send a GET request to the Telegram API
        response = requests.get(f'https://api.telegram.org/bot{bot_token}/getme')
        response_data = response.json()

        # Extract bot_username from the response
        user_bot = response_data['result']['username']
except FileNotFoundError:
    api_id = 23398930
    print('  ')
    api_hash = 'bd3e85a7aae40566f2fa8804d200d6d0'
    print('  ')
    bot_token = input(A+"❖ Inter Your Token ➜  "+X)
    print('  ')
    DEVLOO = input(A+"❖ Inter Id Off Controller Account ➜  "+X)
    print('  ')
    MAX_ACCOUNTS = int(input(A+"❖ Inter Num Of Max Acc ➜  "+X))
    print('  ')
    id_bot = bot_token.split(':')[0]  # Extract id_bot from bot_token
    print('  ')

    # Send a GET request to the Telegram API
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/getme')
    response_data = response.json()

    # Extract bot_username from the response
    user_bot = response_data['result']['username']
    
    print('  ')
    
    data = {
        'api_id': api_id,
        'api_hash': api_hash,
        'bot_token': bot_token,
        'DEVLOO': DEVLOO,
        'MAX_ACCOUNTS': MAX_ACCOUNTS,
        'user_bot': user_bot,
        'id_bot': id_bot
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f)


def clone_repository(repo_url):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    Repo.clone_from(repo_url, current_dir)


clone_repository('https://github.com/sythontm/CollectSython.git')
