import imaplib
import email
from email.header import decode_header
from typing import List, Dict, Optional


def read_emails(imap_server: str, email_address: str, password: str) -> List[Dict]:
    emails_data = []

    try:
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(email_address, password)

        imap.select("INBOX")

        status, messages = imap.search(None, "ALL")

        messages = messages[0].split()

        for msg_id in messages:
            try:
                status, msg_data = imap.fetch(msg_id, "(RFC822)")
                if status != 'OK':
                    continue

                msg = email.message_from_bytes(msg_data[0][1])

                subject = decode_header_value(msg.get("Subject", "Без темы"))

                from_ = msg.get("From", "Неизвестно")
                date = msg.get("Date", "Неизвестно")
                body = extract_email_body(msg)

                email_dict = {
                    'id': msg_id.decode() if isinstance(msg_id, bytes) else str(msg_id),
                    'from': from_,
                    'subject': subject,
                    'date': date,
                    'body': body,
                    'raw_body': body  # Можно добавить raw если нужно
                }

                emails_data.append(email_dict)
            except Exception as e:
                continue

        imap.close()
        imap.logout()

    except imaplib.IMAP4.error as e:
        print(e)
    except Exception as e:
        print(e)
    return emails_data


def decode_header_value(header_value: Optional[str], default: str = "") -> str:
    if not header_value:
        return default
    try:
        decoded_parts = []
        for part, encoding in decode_header(header_value):
            if isinstance(part, bytes):
                try:
                    decoded_parts.append(part.decode(encoding if encoding else 'utf-8', errors='ignore'))
                except:
                    decoded_parts.append(part.decode('utf-8', errors='ignore'))
            else:
                decoded_parts.append(str(part))
        return ' '.join(decoded_parts).strip()
    except Exception as e:
        print(e)


def extract_email_body(msg) -> str:
    body = ""
    try:
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition", ""))

                if content_type == "text/plain" and "attachment" not in content_disposition:
                    payload = part.get_payload(decode=True)
                    if payload:
                        body = payload.decode('utf-8', errors='ignore')
                        break

                elif content_type == "text/html" and not body and "attachment" not in content_disposition:
                    payload = part.get_payload(decode=True)
                    if payload:
                        html = payload.decode('utf-8', errors='ignore')

        else:
            payload = msg.get_payload(decode=True)
            if payload:
                body = payload.decode('utf-8', errors='ignore')

    except Exception as e:
        print(e)

    return ' '.join(body.split())
