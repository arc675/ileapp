__artifacts_v2__ = {
    "line_message_attachments": {
        "name": "Line - Message Attachments",
        "description": "Files sent or received in Line chats, joined to the message each belongs "
                       "to and shown where the file is present.",
        "author": "@AlexisBrignoni, Claude",
        "creation_date": "2026-09-06",
        "last_update_date": "2026-09-06",
        "requirements": "none",
        "category": "Line",
        "notes": "One row per row of ZMESSAGEATTACHMENTINFO in the app's per account private "
                 "store, Library/Application Support/PrivateStore/P_<account "
                 "id>/Messages/MessageAttachmentInfo.sqlite. The link from an attachment to its "
                 "message is one the app recorded rather than a match on size or time: the row's "
                 "message identifier equalled a ZMESSAGE.ZID in the Line.sqlite beside it on "
                 "every row of both images that carry this store, and the stored file name is "
                 "that same identifier with an extension. The message text, chat and direction "
                 "are joined from that database, which the separate Line Artifacts artifact "
                 "reports in full. Direction is the same inference that module makes and states: "
                 "a row with no sender reference is read as outgoing. The file itself is looked "
                 "for in the Message Attachments folder of the same private store, which sits in "
                 "the app's own container while these databases sit in the app group container, "
                 "so the two are paired on the account the folder is named for. All four "
                 "attachment rows across the two images resolved to a file and the picture is "
                 "shown rather than only named. Every image tested holds one account. A tree "
                 "built by hand from one of them, carrying a second account whose Message "
                 "Attachments folder held files of the same names, was run to check that pairing: "
                 "each of the four rows resolved to the file in its own account's folder. The "
                 "stored timestamp needs care and the artifact reports both readings. Half the "
                 "rows on each image carry a plain Unix millisecond value and the other half "
                 "carry that same kind of value with 2305843009213693952 added to it, which is "
                 "two to the power of sixty one. Subtracting that offset puts each of those rows "
                 "within one second of the message it belongs to, measured at 0.97 and 0.74 "
                 "seconds, and leaving it in place would put them tens of millions of years from "
                 "now, so the offset is removed and the raw value is kept in its own column. "
                 "Nothing available explains why the app writes some rows tagged that way. "
                 "Content Type is reported as stored and held the value 1 on every row of both "
                 "images, which is too few values to say what the field distinguishes. The store "
                 "was not present on the third tested image.",
        "paths": ('*/Containers/*/*/Library/Application Support/PrivateStore/P_*/Messages/MessageAttachmentInfo.sqlite*',
                  '*/Containers/*/*/Library/Application Support/PrivateStore/P_*/Messages/Line.sqlite*',
                  '*/Containers/*/*/Library/Application Support/PrivateStore/P_*/Message Attachments/*'),
        "output_types": "standard",
        "artifact_icon": "paperclip",
        "sample_data": {
                           "hickman_ios13": "iOS 13.3.1 | Line | 2 rows",
                           "hickman_ios14": "iOS 14.3 | Line | 2 rows",
                           "hickman_ios15": "iOS 15.3.1 | Line | store not present",
                       },
    },
    "line_synced_contacts": {
        "name": "Line - Synced Contacts",
        "description": "Address book entries the Line app synchronised, with the name and phone "
                       "number held against each.",
        "author": "@AlexisBrignoni, Claude",
        "creation_date": "2026-09-06",
        "last_update_date": "2026-09-06",
        "requirements": "none",
        "category": "Line",
        "notes": "One row per row of ZMANAGEDCNCONTACT in the per account private store's "
                 "Contacts Syncing/Contacts.sqlite. These are entries the app took from the "
                 "device address book, so a row records a contact the phone held rather than "
                 "somebody the account exchanged messages with, and the two sets are not the "
                 "same. Created is a Core Data time, seconds since 2001, reported in UTC. The "
                 "Line Member ID column is what ties a contact to a Line account. It was blank on "
                 "every row of the two older tested images and carried a value on one of the six "
                 "rows of the newest, so on these devices almost every synced contact is an "
                 "address book entry the app had not matched to an account, and a blank there is "
                 "not evidence that the person has no Line account. Invited, Removed, Server "
                 "Synced, Inviteable and Type are the app's own flags and are reported as stored. "
                 "Invited, Removed and Inviteable held 0 on every row of all three images and "
                 "Type held 1; Server Synced held 0 on every row of the two older images and 1 on "
                 "every row of the newest, which is a difference between the images and not "
                 "something one row says about another. The tested images held 2, 4 and 6 rows. "
                 "Phonetic Name and Address Book Identifier held no value on any row of the three "
                 "tested images: the first is filled only where the device address book carries a "
                 "phonetic reading of the name, and the second only where the app kept a "
                 "reference back to the address book entry. Account ID held one value on every "
                 "row of each image, which is what a device with a single signed in account looks "
                 "like.",
        "paths": ('*/Containers/*/*/Library/Application Support/PrivateStore/P_*/Contacts Syncing/Contacts.sqlite*',),
        "output_types": "standard",
        "artifact_icon": "users",
        "sample_data": {
                           "hickman_ios13": "iOS 13.3.1 | Line | 2 rows",
                           "hickman_ios14": "iOS 14.3 | Line | 4 rows",
                           "hickman_ios15": "iOS 15.3.1 | Line | 6 rows",
                       },
    },
    "line_browser_history": {
        "name": "Line - In-App Browser History",
        "description": "Page records the browser built into the Line app keeps, with the address "
                       "and title of each.",
        "author": "@AlexisBrignoni, Claude",
        "creation_date": "2026-09-06",
        "last_update_date": "2026-09-06",
        "requirements": "none",
        "category": "Line",
        "notes": "One row per row of ZBROWSERHISTORYPAGEEVENT in the per account private store's "
                 "Browser History/BrowserHistory.sqlite, joined to the page record the event "
                 "names for the address, title and icon. This is the browser inside the app, "
                 "which a person reaches by opening a link from a chat, so it is a separate "
                 "record from Safari's history and neither implies the other. The two dates the "
                 "event carries are Core Data times, seconds since 2001, reported in UTC. The "
                 "store exists only on the newer of the three tested images and both of its "
                 "tables were empty there, so this reader is code present and was not exercised "
                 "and its columns are the ones the tables declare rather than ones observed "
                 "carrying values. An empty table is not evidence that no link was ever opened, "
                 "only that none was recorded here.",
        "paths": ('*/Containers/*/*/Library/Application Support/PrivateStore/P_*/Browser History/BrowserHistory.sqlite*',),
        "output_types": "standard",
        "artifact_icon": "globe",
        "sample_data": {
            "hickman_ios13": "iOS 13.3.1 | Line | store not present",
            "hickman_ios14": "iOS 14.3 | Line | store not present",
            "hickman_ios15": "iOS 15.3.1 | Line | 0 rows",
        },
    },
    "line_encrypted_chats": {
        "name": "Line - Encrypted Chats",
        "description": "The chats the Line app holds end to end encryption records for, and when "
                       "each key was created.",
        "author": "@AlexisBrignoni, Claude",
        "creation_date": "2026-09-06",
        "last_update_date": "2026-09-06",
        "requirements": "none",
        "category": "Line",
        "notes": "One row per row of ZE2EECHAT and of ZE2EEKEY in the per account private store's "
                 "Messages/E2EEData.sqlite, told apart by the Source Table column. A row records "
                 "that the app held encryption state for a chat, which tells an examiner why "
                 "message content for that chat may be absent or unreadable elsewhere. Key "
                 "Created is a Core Data time, seconds since 2001, reported in UTC. **No key "
                 "material is reported.** The ZKEYDATA column holds the key bytes and is read by "
                 "nothing here; the artifact reports only that a key exists, its identifier and "
                 "when it was made, and an examiner who needs the bytes can go to the file this "
                 "artifact names. Member ID comes from the row's ZMIDDATA blob, which holds one "
                 "type byte followed by the sixteen bytes of the identifier. Where that type byte "
                 "is 0x00 the identifier is rendered the way the app writes it as text elsewhere, "
                 "the letter u followed by those bytes in lower case hexadecimal. Every value "
                 "rendered that way on the three tested images equals a ZMID in the Line.sqlite "
                 "beside it, and on two of them one equals the account the private store folder "
                 "is named for, which is what establishes the rendering. No other type byte was "
                 "seen, so a blob carrying one is reported as hexadecimal as stored. Content "
                 "Types, Current Key ID, Sequence Number and Version are reported as stored. The "
                 "tested images held 2, 3 and 4 chat rows and 1, 2 and 2 key rows. Account ID "
                 "held one value on every row of each tested image, since one account was signed "
                 "in; it is kept because it is what separates two accounts on a device that has "
                 "both.",
        "paths": ('*/Containers/*/*/Library/Application Support/PrivateStore/P_*/Messages/E2EEData.sqlite*',),
        "output_types": "standard",
        "artifact_icon": "lock",
        "sample_data": {
                           "hickman_ios13": "iOS 13.3.1 | Line | 3 rows",
                           "hickman_ios14": "iOS 14.3 | Line | 5 rows",
                           "hickman_ios15": "iOS 15.3.1 | Line | 6 rows",
                       },
    },
}

import os
import re
from datetime import datetime, timedelta, timezone

from scripts.ilapfuncs import (artifact_processor, check_in_media, does_table_exist_in_db,
                               get_sqlite_db_records, logfunc)

_UNIX_EPOCH_UTC = datetime(1970, 1, 1, tzinfo=timezone.utc)
_CORE_DATA_EPOCH_UTC = datetime(2001, 1, 1, tzinfo=timezone.utc)
# Some attachment rows carry their Unix millisecond time with 2**61 added to it.
_TIME_TAG = 2305843009213693952
_PRIVATE_STORE = re.compile(r'(.*/PrivateStore/P_[^/]+)/', re.I)
_PRINTABLE = re.compile(rb'[ -~]{4,}')
# A stored member identifier is one type byte plus the sixteen bytes of the identifier.
_MID_LENGTH = 17


def _stores(files_found, name):
    '''Every file with the given base name among the matches, directories skipped.'''
    seen = []
    for found in files_found:
        path = str(found)
        if os.path.isdir(path) or path.endswith(('-wal', '-shm')):
            continue
        if os.path.basename(path) == name and path not in seen:
            seen.append(path)
    return seen


def _account_store(path):
    '''The per account private store a file sits in, or '' when it is not under one.'''
    match = _PRIVATE_STORE.match(str(path).replace('\\', '/'))
    return match.group(1) if match else ''


def _account_id(path):
    '''The Line account identifier the private store directory name carries.'''
    store = _account_store(path)
    name = os.path.basename(store)
    return name[2:] if name.startswith('P_') else name


def _rows(path, table, columns):
    '''Rows of a table, or nothing when the store does not have it.'''
    if not does_table_exist_in_db(path, table):
        return []
    try:
        return list(get_sqlite_db_records(path, f'SELECT {columns} FROM {table}'))
    except Exception as error:                   # pylint: disable=broad-except
        logfunc(f'Line: could not read {table}: {error}')
        return []


def _text(value):
    '''A stored value as text, with a stored null read as absent.'''
    return '' if value is None else str(value)


def _core_data_to_utc(value):
    '''Core Data seconds since 2001 to an aware UTC datetime, or ''.'''
    if value in (None, '', 0):
        return ''
    try:
        return _CORE_DATA_EPOCH_UTC + timedelta(seconds=float(value))
    except (TypeError, ValueError, OverflowError):
        return ''


def _attachment_time(value):
    '''An attachment time as an aware UTC datetime, with the 2**61 tag removed.'''
    if value in (None, ''):
        return ''
    try:
        number = int(value)
    except (TypeError, ValueError):
        return ''
    if number > _TIME_TAG:
        number -= _TIME_TAG
    try:
        return _UNIX_EPOCH_UTC + timedelta(milliseconds=number)
    except (OverflowError, ValueError):
        return ''


def _unix_ms_to_utc(value):
    '''Unix milliseconds to an aware UTC datetime, or ''.'''
    if value in (None, '', 0):
        return ''
    try:
        return _UNIX_EPOCH_UTC + timedelta(milliseconds=int(value))
    except (TypeError, ValueError, OverflowError):
        return ''


def _member_id(blob):
    '''The member identifier a stored blob carries, or ''.

    ZMIDDATA holds one type byte followed by the sixteen bytes of the identifier. Where
    that type byte is 0x00 the app writes the same identifier as text elsewhere, as the
    letter u followed by those sixteen bytes in lower case hexadecimal: every value
    decoded that way on the tested images equals a ZMID in the Line.sqlite beside it, and
    on two of them one equals the account the private store folder is named for. No other
    type byte was seen, so a blob carrying one is reported as hexadecimal as stored rather
    than given a letter that nothing here establishes.
    '''
    if blob is None:
        return ''
    if isinstance(blob, str):
        return blob
    try:
        raw = bytes(blob)
    except (TypeError, ValueError):
        return ''
    if len(raw) == _MID_LENGTH:
        return ('u' + raw[1:].hex()) if raw[0] == 0 else raw.hex()
    runs = _PRINTABLE.findall(raw)
    return runs[0].decode('ascii', 'replace') if runs else ''


def _messages(store):
    '''{message id: (timestamp, text, chat member id, sender name, direction)} for a store.'''
    path = os.path.join(store, 'Messages', 'Line.sqlite')
    if not os.path.exists(path):
        return {}
    index = {}
    for (message_id, stamp, text, chat_mid, sender_name, sender) in _rows(
            path, 'ZMESSAGE',
            'ZMESSAGE.ZID, ZMESSAGE.ZTIMESTAMP, ZMESSAGE.ZTEXT, '
            '(SELECT ZMID FROM ZCHAT WHERE ZCHAT.Z_PK = ZMESSAGE.ZCHAT), '
            '(SELECT ZNAME FROM ZUSER WHERE ZUSER.Z_PK = ZMESSAGE.ZSENDER), ZMESSAGE.ZSENDER'):
        if message_id is None:
            continue
        direction = 'Outgoing' if sender is None else 'Incoming'
        index[str(message_id)] = (_unix_ms_to_utc(stamp), _text(text), _text(chat_mid),
                                  _text(sender_name), direction)
    return index


@artifact_processor
def line_message_attachments(context):
    data_list = []
    files_found = context.get_files_found()
    sources = _stores(files_found, 'MessageAttachmentInfo.sqlite')

    on_disk = {}
    for found in files_found:
        path = str(found)
        if os.path.isdir(path):
            continue
        if '/Message Attachments/' in path.replace('\\', '/'):
            # Keyed on the account id, not the container: the databases sit in the app group
            # container and the attachment files in the app data container, and the two share
            # only the P_<account id> directory name.
            on_disk.setdefault((_account_id(path), os.path.basename(path)), path)

    for source_path in sources:
        store = _account_store(source_path)
        messages = _messages(store)
        for (message_id, chat_mid, filename, content_type, size, stamp) in _rows(
                source_path, 'ZMESSAGEATTACHMENTINFO',
                'ZMESSAGEID, ZCHATMID, ZFILENAME, ZCONTENTTYPE, ZFILESIZE, ZTIMESTAMP'):
            when, text, chat, sender, direction = messages.get(
                _text(message_id), ('', '', '', '', ''))
            media = ''
            cached = (on_disk.get((_account_id(source_path), _text(filename)))
                      if filename else None)
            if cached:
                media = check_in_media(cached, _text(filename))
            data_list.append((
                _attachment_time(stamp), when, direction, sender, _text(text), media,
                _text(filename), _text(content_type), _text(size), chat or _member_id(chat_mid),
                _text(message_id), _text(stamp), _account_id(source_path),
            ))

    data_list.sort(key=lambda row: str(row[0]), reverse=True)

    data_headers = (
        ('Attachment Timestamp', 'datetime'), ('Message Timestamp', 'datetime'),
        'Message Direction', 'Sender', 'Message', ('Attachment', 'media'), 'File Name',
        'Content Type (as stored)', 'File Size', 'Chat Member ID', 'Message ID',
        'Attachment Timestamp (as stored)', 'Account ID',
    )
    return data_headers, data_list, '\n'.join(sources)


@artifact_processor
def line_synced_contacts(context):
    data_list = []
    sources = _stores(context.get_files_found(), 'Contacts.sqlite')

    for source_path in sources:
        for (name, phonetic, sortable, phone, member_id, created, invited, inviteable,
             removed, synced, kind, ab_luid, cn_luid) in _rows(
                source_path, 'ZMANAGEDCNCONTACT',
                'ZNAME, ZPHONETICNAME, ZSORTABLENAME, ZPHONENUMBER, ZMID, ZCREATEDAT, '
                'ZISINVITED, ZISINVITEABLE, ZISREMOVED, ZSERVERSYNCED, ZTYPE, ZABLUID, ZCNLUID'):
            data_list.append((
                _core_data_to_utc(created), _text(name), _text(phone), _text(member_id),
                _text(phonetic), _text(sortable), _text(invited), _text(inviteable),
                _text(removed), _text(synced), _text(kind), _text(ab_luid), _text(cn_luid),
                _account_id(source_path),
            ))

    data_list.sort(key=lambda row: str(row[0]), reverse=True)

    data_headers = (
        ('Created', 'datetime'), 'Name', ('Phone Number', 'phonenumber'), 'Line Member ID',
        'Phonetic Name', 'Sortable Name', 'Invited (as stored)', 'Inviteable (as stored)',
        'Removed (as stored)', 'Server Synced (as stored)', 'Type (as stored)',
        'Address Book Identifier', 'Contact Identifier', 'Account ID',
    )
    return data_headers, data_list, '\n'.join(sources)


@artifact_processor
def line_encrypted_chats(context):
    data_list = []
    sources = _stores(context.get_files_found(), 'E2EEData.sqlite')

    for source_path in sources:
        account = _account_id(source_path)
        for (member, content_types, current_key, sequence, version) in _rows(
                source_path, 'ZE2EECHAT',
                'ZMIDDATA, ZCONTENTTYPES, ZCURRENTKEYID, ZSEQUENCENUMBER, ZVERSION'):
            data_list.append((
                '', _member_id(member), _text(content_types), _text(current_key),
                _text(sequence), _text(version), '', 'ZE2EECHAT', account,
            ))
        for (member, created, key_id, enc_key_id, version) in _rows(
                source_path, 'ZE2EEKEY',
                'ZMIDDATA, ZCREATEDTIME, ZKEYID, ZENCKEYID, ZVERSION'):
            data_list.append((
                _core_data_to_utc(created), _member_id(member), '', _text(key_id), '',
                _text(version), _text(enc_key_id), 'ZE2EEKEY', account,
            ))

    data_list.sort(key=lambda row: str(row[0]), reverse=True)

    data_headers = (
        ('Key Created', 'datetime'), 'Member ID', 'Content Types (as stored)',
        'Key ID (as stored)', 'Sequence Number (as stored)', 'Version (as stored)',
        'Encryption Key ID (as stored)', 'Source Table', 'Account ID',
    )
    return data_headers, data_list, '\n'.join(sources)


@artifact_processor
def line_browser_history(context):
    data_list = []
    sources = _stores(context.get_files_found(), 'BrowserHistory.sqlite')

    for source_path in sources:
        for (visited, start_of_visit, url, title, page_type, icon) in _rows(
                source_path, 'ZBROWSERHISTORYPAGEEVENT',
                'ZBROWSERHISTORYPAGEEVENT.ZVISITEDDATE, '
                'ZBROWSERHISTORYPAGEEVENT.ZSTARTOFVISITEDDATE, '
                '(SELECT ZPAGEURL FROM ZBROWSERHISTORYPAGEMETADATA m '
                ' WHERE m.Z_PK = ZBROWSERHISTORYPAGEEVENT.ZPAGEMETADATA), '
                '(SELECT ZPAGETITLE FROM ZBROWSERHISTORYPAGEMETADATA m '
                ' WHERE m.Z_PK = ZBROWSERHISTORYPAGEEVENT.ZPAGEMETADATA), '
                '(SELECT ZPAGETYPE FROM ZBROWSERHISTORYPAGEMETADATA m '
                ' WHERE m.Z_PK = ZBROWSERHISTORYPAGEEVENT.ZPAGEMETADATA), '
                '(SELECT ZICONFILEURL FROM ZBROWSERHISTORYPAGEMETADATA m '
                ' WHERE m.Z_PK = ZBROWSERHISTORYPAGEEVENT.ZPAGEMETADATA)'):
            data_list.append((
                _core_data_to_utc(visited), _core_data_to_utc(start_of_visit), _text(title),
                _text(url), _text(page_type), _text(icon), _account_id(source_path),
            ))

    data_list.sort(key=lambda row: str(row[0]), reverse=True)

    data_headers = (
        ('Visited', 'datetime'), ('Start Of Visit', 'datetime'), 'Page Title', 'Page URL',
        'Page Type (as stored)', 'Icon File URL', 'Account ID',
    )
    return data_headers, data_list, '\n'.join(sources)
