import time, json, os
from pypresence import Presence, PyPresenceException

client_id = 0
interval_update = 2
list = []

with open( os.path.abspath( 'rpc.json' ), 'r' ) as js:
    jsn = json.load( js )
    for k, v in jsn.items():
        if k == 'client ID':
            client_id = v
        elif k == 'interval update':
            interval_update = int(v)
        elif k == 'buttons':
            list = v
    js.close()

RPC = Presence(client_id)
RPC.connect()

while True:
    try:
        button_1 = { "label": list[0][0], "url": list[0][1] }
        button_2 = { "label": list[1][0], "url": list[1][1] }
        botones = [ button_1, button_2 ]
        img = ''
        state = ''
        if len(list[0]) >= 3:
            img = list[0][2]
            if len(list[0]) >= 4:
                state = list[0][3]

        list.append( list.pop(0) )
        RPC.update( buttons=botones, large_image=img, state=state )
        time.sleep( interval_update )
    except PyPresenceException as e:
        print(f'Exception on updating presence: {e}')
        time.sleep( interval_update )
