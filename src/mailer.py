import os
import base64
# resend.com package
import resend


def send_email_report(subject, body, to_email, attachments, logger):
    '''
    ### Sends an automated email report with attachments using the Resend Python SDK('resend' package). ###
    resend.com have built their own Python package and you must use it in your code to send your emails instead of packages
    like 'requests'.
    See the file EMAILER_DOCUMENTAION.md in the main folder of this project for full explanation
    '''

    # 1. Fetch the Resend API key safely from environment variables
    resend_key = os.environ.get("RESEND_API_KEY")


    if not resend_key:
        logger.error("Delivery Failure: RESEND_API_KEY environment variable is not defined.")
        logger.warning("Please add RESEND_API_KEY to your local PyCharm environment to test.")
        return False

    # Initialize the official Resend client tool
    resend.api_key = resend_key

    # 2. Process and compile file attachments into the format expected by the SDK
    resend_attachments = []
    if isinstance(attachments, str):
        attachments = [attachments]

    for file_path in attachments:
        if not os.path.isfile(file_path):
            logger.warning(f"File missing on disk: {file_path}")
            continue
        try:
            # Read file and convert to text-based Base64 bytes
            with open(file_path, "rb") as f:
                encoded_content = base64.b64encode(f.read()).decode("utf-8")

            # Format the attachment dictionary exactly to Resend's specification
            resend_attachments.append({
                "filename": os.path.basename(file_path),
                "content": encoded_content
            })
            logger.info(f"Attached file for cloud processing: {os.path.basename(file_path)}")
        except Exception as e:
            logger.error(f"Attachment conversion failed for {file_path}: {e}")

    # 3. Format plain text newlines (\n) to HTML break tags (<br>) for clean rendering
    html_body = f"<div style='font-family: Arial, sans-serif; white-space: pre-wrap;'>{body}</div>"

    # 4. Construct the official payload dictionary
    email_params = {
        "from": "Automation Engine <onboarding@resend.dev>",
        "to": [to_email],
        "subject": subject,
        "html": html_body,
        "attachments": resend_attachments
    }

    # 5. Transmit the data payload through the SDK client wrapper
    try:
        logger.info("Connecting to Resend Cloud Mail Server via SDK...")

        # Trigger the cloud transmission
        email_response = resend.Emails.send(email_params)

        logger.info(f"Report successfully accepted by Resend! Message ID: {email_response}")
        return True
    except Exception as e:
        logger.error(f"Resend SDK Delivery Exception: {str(e)}")
        return False
