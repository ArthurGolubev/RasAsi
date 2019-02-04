def sheetFunc(sheetsTable):
    sheetsList = []
    for i in sheetsTable:
        sheetsList.append({
            'properties': {
                'title': i
            },
            'data': [
                {
                    'startRow': 0,
                    'startColumn': 0,
                    'rowData': [
                        {
                            "values": [
                                {
                                    'userEnteredValue': {
                                        'stringValue': 'Лот №'
                                    },
                                    'userEnteredFormat': {
                                        'backgroundColor': {
                                            'red': 0.3,
                                            'blue': 0.9,
                                            'green': 1
                                        },
                                        # 'borders': bordersForm(R=1, G=0, B=0.5),
                                        "horizontalAlignment": "CENTER",
                                        'textFormat': {
                                            'bold': True,
                                            # 'fontFamily': 'Lora',
                                            'fontSize': 12
                                        }
                                    }
                                },
                                {
                                    'userEnteredValue': {
                                        'stringValue': 'Наименование Лота'
                                    },
                                    'userEnteredFormat': {
                                        'backgroundColor': {
                                            'red': 0.3,
                                            'blue': 0.9,
                                            'green': 1
                                        },
                                        # 'borders': bordersForm(1, 0, 0.5),
                                        "horizontalAlignment": "CENTER",
                                        'textFormat': {
                                            'bold': True,
                                            # 'fontFamily': 'Lora',
                                            'fontSize': 12
                                        }
                                    }
                                },
                                {
                                    'userEnteredValue': {
                                        'stringValue': 'Цена продажи'
                                    },
                                    'userEnteredFormat': {
                                        'backgroundColor': {
                                            'red': 0.3,
                                            'blue': 0.9,
                                            'green': 1
                                        },
                                        # 'borders': bordersForm(1, 0, 0.5),
                                        "horizontalAlignment": "CENTER",
                                        'textFormat': {
                                            'bold': True,
                                            # 'fontFamily': 'Lora',
                                            'fontSize': 12
                                        }
                                    }
                                }
                            ]
                        }
                    ],
                    'columnMetadata': [
                        {
                            "pixelSize": 110
                        },
                        {
                            'pixelSize': 760
                        },
                        {
                            'pixelSize': 130
                        }
                    ]
                }
            ]
        })
    return sheetsList
