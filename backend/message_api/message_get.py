import imaplib
import email
from email.header import decode_header
from typing import Dict, Optional


def read_emails(imap_server: str, email_address: str, password: str) -> Optional[Dict]:
    imap = None
    try:
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(email_address, password)
        imap.list()
        imap.select("INBOX")

        status, messages = imap.search(None, "ALL")
        messages = messages[0].split()
        if not messages:
            return None

        last_message = messages[-1]
        status, msg_data = imap.fetch(last_message, "(RFC822)")
        raw_email = msg_data[0][1]

        email_msg = email.message_from_bytes(raw_email)

        # Декодирование темы
        subject_header = email_msg["Subject"]
        if subject_header:
            subject, encoding = decode_header(subject_header)[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else 'utf-8', errors='ignore')
        else:
            subject = ""

        # Извлечение тела
        body = ""
        if email_msg.is_multipart():
            for part in email_msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    payload = part.get_payload(decode=True)
                    if payload:
                        body = payload.decode('utf-8', errors='ignore')
                        break
        else:
            payload = email_msg.get_payload(decode=True)
            if payload:
                body = payload.decode('utf-8', errors='ignore')

        return {
            "from": email_msg.get("From", ""),
            "subject": subject,
            "date": email_msg.get("Date", ""),
            "body": body.strip()
        }

    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    finally:
        if imap:
            try:
                imap.close()
                imap.logout()
            except:
                pass

