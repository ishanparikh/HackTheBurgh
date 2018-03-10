import botometer

mashape_key = "x6adkBnZYXmshRWvj2nX0tehNLZCp1t6i54jsn3ZAARXmmZG52"
twitter_app_auth = {
    'consumer_key': 'TyIlP6mnNgQgGSmuuqGZ77SeP',
    'consumer_secret': 'KLJUO4ZssEt06GkPz1r74FA8p2FmyK0LK23pwQHSOJm5k9PpPy',
    'access_token': '2830897771-VRxmf5eYXxCcsRwjdMhmAxO89pIrBttYM5H5gx9',
    'access_token_secret': 'DfZhwzW3FWCaE7Vf0qU2MYJdJ5eB0p1eimh0gnxKSQZd4',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                                                    mashape_key=mashape_key,
                                                    **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@clayadavis')

# Check a single account by id
result = bom.check_account(1548959833)

# Check a sequence of accounts
accounts = ['@clayadavis', '@onurvarol', '@jabawack']
for screen_name, result in bom.check_accounts_in(accounts):
    print result
