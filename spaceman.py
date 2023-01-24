#!/usr/bin/env python
# coding: utf-8


# Importar as bibliotecas:

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

import mysql.connector

# -----------------------------------------------------------------------------------------------
# Definir a pagina que sera usada :
# -----------------------------------------------------------------------------------------------
while True:
    html = urlopen("https://gs11.pragmaticplaylive.net/api/ui/statisticHistory?tableId=spacemanyxeabn03&numberOfGames=500&JSESSIONID=ta7gZAYsEEDqQPueORdXQu9NJ5OS8V3pF3MzofXdv6tisICkRAOQ!1652711196&ck=1674506937455&game_mode=lobby_desktop")

    # -----------------------------------------------------------------------------------------------
    # Converter HTML em um Objeto  BautifulSoup:
    # -----------------------------------------------------------------------------------------------

    soup = BeautifulSoup(html, "html.parser")
    ee = soup

    # iniciar a raspagem :
    # print(ee)

    y = json.loads(ee.text)

    # -----------------------------------------------------------------------------------------------
    # conexao banco:
    # -----------------------------------------------------------------------------------------------

    db_connection = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="spaceman")
    cursor = db_connection.cursor()
    # print(cursor)

    # -------------------------------------------------------------------------------------
    # contar total de registro :
    # -------------------------------------------------------------------------------------

    total_registro = len(y['history'])

    # print(total_registro)

    if(total_registro >= 1):
        for i in range(total_registro):
            resultTime = y['history'][i]['resultTime'].split('.')

            print(resultTime)

            query_select = "SELECT * FROM historicos WHERE resultTime =" + \
                "'" + resultTime[0] + "'"

            print(query_select)

            cursor.execute(query_select)
            cursor.fetchall()
            historico = cursor.rowcount
            db_connection.commit()

            print(historico)

            if (historico < 1):
                # print(resultTime[0])

                # inser in bd :
                gameId = y['history'][i]['gameId']
                gameType = y['history'][i]['gameType']
                betCount = y['history'][i]['betCount']
                playerCount = y['history'][i]['playerCount']
                playerWinCount = y['history'][i]['playerWinCount']
                gameResult = y['history'][i]['gameResult']
                resultTime = resultTime[0]
                resultTime_string = y['history'][i]['resultTime']
                gameHashKey = y['history'][i]['gameHashKey']
                gameEncryptedResult = y['history'][i]['gameEncryptedResult']

                sql = "INSERT INTO historicos (gameId, gameType, betCount, playerCount, playerWinCount, gameResult, resultTime, resultTime_string, gameHashKey, gameEncryptedResult) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (gameId, gameType, betCount, playerCount, playerWinCount, gameResult,
                       resultTime, "resultTime_string", gameHashKey, "gameEncryptedResult")
                cursor.execute(sql, val)
                db_connection.commit()

                # print(y['history'][i]['gameResult'])
