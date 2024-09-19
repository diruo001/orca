import argparse
import io
import os

from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'data_sync.json'


def authenticate():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds


def upload(file_path, folder_id):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()
    print(f"upload {file_path} done!")


def list_file():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    results = (
        service.files()
        .list(pageSize=30, fields="nextPageToken, files(id, name)")
        .execute()
    )
    items = results.get("files", [])

    if not items:
        print("No files found.")
        return
    print("Files:")
    for item in items:
        print(f"{item['name']} ({item['id']})")


def download(real_file_id, save_path=None):
    """Downloads a file
    Args:
        real_file_id: ID of the file to download
    Returns : 
    """
    creds = authenticate()

    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)

        file_id = real_file_id

        request = service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}.")

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None

    if save_path is not None and file is not None:
        file.seek(0)
        with open(save_path, "wb") as f:
            f.write(file.read())
            f.close()
    print(f"download {save_path} done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    parser_download = subparsers.add_parser("download", help="download help")
    parser_download.add_argument("--orca", action="store_true", help="")
    parser_download.add_argument("--file_id", type=str, help="")
    parser_download.add_argument("--save_path", type=str, default="orca.tar.xz", help="")
    parser_upload = subparsers.add_parser("upload", help="upload help")
    parser_upload.add_argument("--file_path", type=str, help="")
    parser_upload.add_argument("--folder_id", type=str, help="")
    parser_upload = subparsers.add_parser("list", help="list help")
    args = parser.parse_args()

    if args.command == "download":
        if args.orca:
            download(real_file_id="10HZybV4M4BUVc3RNOiefrkrEewGxwrfz",
                     save_path=args.save_path)
        else:
            download(real_file_id=args.file_id, save_path=args.save_path)
    elif args.command == "upload":
        upload(file_path=args.file_path, folder_id=args.folder_id)
    elif args.command == "list":
        list_file()

