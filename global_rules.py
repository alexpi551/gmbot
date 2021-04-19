bot_info = [cfb574a311ea1e684d2c812336, Tester bot]



def run(data, bot_info, send_message):
    if data['text'] == 'nice':
      send_message('Nice', bot_info[0])
      return True
