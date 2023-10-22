"""Utility functions used by the connectors."""

import os
from datetime import datetime as _datetime, timedelta
from azure.storage.fileshare import ShareFileClient
from azure.storage.fileshare import generate_file_sas
from azure.storage.fileshare import FileSasPermissions

# Encrypt/ Decrypt with OpenSSL:

def generate_fs_write_sas_token(
    account_name, account_key, share_name, file_path, minutes=10
):
    """Generate a 'write' SAS token for a File Share path in the specified
    Storage Account. The token will be valid for 10 minutes by default."""

    sas_token = generate_file_sas(
        account_name=account_name,
        account_key=account_key,
        share_name=share_name,
        file_path=file_path.split("/"),
        permission=FileSasPermissions(write=True),
        expiry=_datetime.utcnow() + timedelta(minutes=minutes),
    )

    return sas_token


def upload_to_fileshare(  # pylint: disable=too-many-arguments
    source_file_path,
    source_file_name,
    account_name,
    fs_name,
    fs_path,
    sas_token,
):
    """
    Upload the source file to the path specified on the Azure Fileshare.
    Optionally, zip and password protect the file before the file is uploaded
    to Fileshare.
    """

    account_url = f"https://{account_name}.file.core.windows.net"
    share_name = fs_name
    fs_file_path = fs_path.strip("/")
    file_path = os.path.join(fs_file_path, source_file_name)

    # Create the File Share API Client
    share_file_client = ShareFileClient(
        account_url=account_url,
        share_name=share_name,
        file_path=file_path,
        credential=sas_token,
    )

    with open(os.path.join(source_file_path, source_file_name), "rb") as source_file:
        share_file_client.upload_file(source_file)
