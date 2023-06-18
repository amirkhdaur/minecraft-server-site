from mcstatus import JavaServer

server = JavaServer.lookup('217.151.230.5')


def get_status():
    try:
        status = server.status()
    except:
        return {}
    
    
    data = {
        'players': {
            'online': status.players.online,
            'max': status.players.max,
            'sample': [player.name for player in status.players.sample] if status.players.sample else []
        },
        'description': status.description,
    }
    return data
