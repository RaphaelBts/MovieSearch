def responseDict(namedGroups):
    repDict = {
        'Hello': f'{namedGroups.get("greeting")} you !',
        'Exit': 'Hope I helped. Do not hesitate to come seeing me again !',
        'Help': 'How can I help you ?',
        'Current weather': f'Current weather is {namedGroups.get("city")}...'
    }
    return repDict