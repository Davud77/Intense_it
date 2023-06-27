# from flask import Flask, render_template, request
from minio import Minio
from minio.error import S3Error

# app = Flask(__name__)

# Настройки MinIO
minio_endpoint = 'minio.botplus.ru'
minio_access_key = 'GAIsCXzNuOc7vblk'
minio_secret_key = 'wg86g95C9Hnm176uB2FsxGOl0DwQ9acU'
minio_bucket = 'pano'


try:
    minio_client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False
    )
    # Проверка доступности сервера MinIO
    minio_client.bucket_exists('mybucket')
    print('Подключение к серверу MinIO успешно установлено.')
except S3Error as err:
    print(f'Ошибка подключения к серверу MinIO: {err}')


# # Инициализация клиента MinIO
# minio_client = Minio(
#     minio_endpoint,
#     access_key=minio_access_key,
#     secret_key=minio_secret_key,
#     secure=False
# )


# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')


# @app.route('/upload', methods=['POST'])
# def upload():
#     # Получение файла из формы
#     file = request.files['file']

#     try:
#         # Загрузка файла в MinIO
#         minio_client.put_object(
#             bucket_name=minio_bucket,
#             object_name=file.filename,
#             data=file,
#             length=file.content_length,
#             content_type=file.content_type
#         )
#     except S3Error as err:
#         return f'Ошибка загрузки файла в MinIO: {err}', 500

#     return 'Файл успешно загружен в MinIO!'


# if __name__ == '__main__':
#     app.run()