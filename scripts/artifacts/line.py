__artifacts_v2__ = {
    "line": {
        "name": "Line Artifacts",
        "description": "Line messages including message direction (inferred from the absence of a sender reference) and associated usernames",
        "author": "Elliot Glendye",
        "creation_date": "2023-11-22",
        "last_update_date": "2026-09-06",
        "requirements": "none",
        "category": "Line",
        "notes": "Direction is inferred: rows without a sender reference are treated as outgoing; "
                 "established through testing. The store holds no user row for the signed in "
                 "account itself on any tested image, so a message that account sent has no user "
                 "row to point at, which is what that reading expects. Username names the other "
                 "party rather than the sender of every row: it was filled on all 66 incoming rows "
                 "and on none of the 54 outgoing rows across the four tested images. "
                 "Every Line.sqlite in the extraction is read rather "
                 "than only the first one found. The app keeps one store per signed in account, "
                 "under a folder named for that account, and Account ID carries that name so rows "
                 "from two accounts on one device stay apart. A store that does not sit under such "
                 "a folder leaves Account ID blank. Rows from all stores are ordered together, "
                 "newest first. Every tested image held one account, so the two account case was "
                 "checked on a tree built by hand from one of them: the rows doubled to sixteen "
                 "under each of two accounts, and a message altered in the added copy appeared "
                 "only against that copy's account. Read the way it was before this change, the "
                 "same tree returned one of the two stores and sixteen of the thirty two rows.",
        "paths": ('**/Line.sqlite*',),
        "output_types": "standard",
        "artifact_icon": "message-circle",
        "sample_data": {
            "iphone11_ios17": "iOS 17.3 | group.com.linecorp.line | 62 rows",
            "hickman_ios13": "iOS 13.3.1 | group.com.linecorp.line | 15 rows",
            "hickman_ios14": "iOS 14.3 | group.com.linecorp.line | 16 rows",
            "hickman_ios15": "iOS 15.3.1 | group.com.linecorp.line | 27 rows",
        },
        "data_views": {
            "conversation": {
                "conversationDiscriminatorColumn": "Username",
                "textColumn": "Message",
                "directionColumn": "Sent / Received",
                "directionSentValue": "Outgoing",
                "timeColumn": "Timestamp",
                "senderColumn": "Username",
                "sentMessageStaticLabel": "Local User"
            }
        },
    }
}

import os
import re
import sqlite3

from scripts.ilapfuncs import artifact_processor, get_sqlite_db_records, logfunc

# The app keeps one store per signed in account, under a folder named for that account.
_PRIVATE_STORE = re.compile(r'.*/PrivateStore/P_([^/]+)/', re.I)


def _account_id(path):
    '''The account the private store folder is named for, or '' when there is no such folder.'''
    match = _PRIVATE_STORE.match(str(path).replace('\\', '/'))
    return match.group(1) if match else ''


@artifact_processor
def line(context):
    data_headers = (('Timestamp', 'datetime'), 'Sent / Received', 'Username', 'Message',
                    'Account ID')
    data_list = []
    sources = []
    for file_found in context.get_files_found():
        file_found = str(file_found)
        if os.path.isdir(file_found) or not file_found.endswith('Line.sqlite'):
            continue
        if file_found not in sources:
            sources.append(file_found)
    if not sources:
        return data_headers, data_list, ''

    query = '''
    SELECT
        datetime(ZMESSAGE.ZTIMESTAMP / 1000, 'unixepoch'),
        CASE WHEN ZMESSAGE.ZSENDER IS NULL THEN 'Outgoing' ELSE 'Incoming' END,
        ZUSER.ZNAME,
        ZMESSAGE.ZTEXT
    FROM ZMESSAGE
    LEFT JOIN ZUSER ON ZMESSAGE.ZSENDER = ZUSER.Z_PK
    ORDER BY ZMESSAGE.ZTIMESTAMP DESC
    '''
    read = []
    for source_path in sources:
        try:
            rows = get_sqlite_db_records(source_path, query)
        except sqlite3.Error as ex:
            logfunc(f'Error reading Line messages: {ex}')
            continue
        read.append(source_path)
        account = _account_id(source_path)
        for row in rows:
            data_list.append(tuple(row) + (account,))

    data_list.sort(key=lambda row: str(row[0]), reverse=True)

    return data_headers, data_list, '\n'.join(read)
