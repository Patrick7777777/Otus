import time
from PIL import Image
from pathlib import Path


class MediaFile(Path):
    """
    Наследуемся от класса Path в pathlib,
    чтобы унаследовать методы работы с файлами.
    """
    def __new__(cls, *args, **kwargs):
        # создаем новый объект типа MediaFile, который также является экземпляром Path
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.author = kwargs.get('author', None)
        if self.exists():
            self.size = self.stat().st_size
            self.create_time = time.ctime(self.stat().st_ctime)
            self.modified_time = time.ctime(self.stat().st_mtime)
            self.last_access_time = time.ctime(self.stat().st_atime)
        else:
            print(f"Файла {self.name} не существует")

    def get_format(self):
        """Получает формат медиафайла"""
        raise NotImplementedError("Это метод должны реализовать дочерние классы.")

    def get_metadata(self):
        """Получает метаданные медиафайла"""
        raise NotImplementedError("Это метод должны реализовать дочерние классы.")

    def convert(self, new_format: str):
        """Конвертирует файл в заданный формат"""
        raise NotImplementedError("Это метод должны реализовать дочерние классы.")

    def save(self):
        """Сохраняет изменения в файле"""
        raise NotImplementedError("Это метод должны реализовать дочерние классы.")

    def delete_file(self):
        """Удаляет файл"""
        if self.exists():
            self.unlink(missing_ok=True)
            print(f"Файл {self.name} удален.")
        else:
            print(f"Удаление невозможно, файла {self.name} не существует")


media = MediaFile('example.png', author='Patrick7777777')
print(media.author, media.create_time, media.modified_time, media.last_access_time, media.size)
media_1 = MediaFile('example.mp3')
media_1.delete_file()


class ImageFile(MediaFile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.exists():
            self.image = Image.open(self)
        else:
            self.image = None

    def get_format(self):
        """Получает формат изображения"""
        if self.image:
            print(f"Формат изображения: {self.image.format}")
            return self.image.format

    def get_metadata(self):
        """Получает метаданные изображения"""
        if self.image:
            print(f"Получение метаданных... {self.name}")

    def convert(self,  new_format: str):
        """Конвертирует изображение в заданный формат и сохраняет"""
        if self.image:
            print(f"Конвертация в формат {new_format} и сохранение")

    def save(self):
        """Сохраняет текущее изображение"""
        if self.image:
            self.image.save(self)
            print(f"Изображение сохранено: {self}")

    def resize(self, width, height):
        """Изменяет размер изображения"""
        if self.image:
            self.image = self.image.resize((width, height))
            print(f"Изображение изменено на: {width}x{height}")


image = ImageFile('example.png')
image.get_format()
image.get_metadata()
image.resize(512, 512)
image.convert('jpg')
image.save()


class AudioFile(MediaFile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_format(self):
        """Получает формат аудиофайла"""
        if self.exists():
            print(f"Получение формата аудиофайла... {self.name}")
        else:
            print(f"Получение формата аудиофайла невозможно, файла {self.name} не существует")

    def get_metadata(self):
        """Получает метаданные аудиофайла"""
        if self.exists():
            print(f"Получение метаданных... {self.name}")
        else:
            print(f"Получение метаданных аудиофайла невозможно, файла {self.name} не существует")


audio = AudioFile('example.mp3')
audio.get_format()
audio.get_metadata()


class VideoFile(MediaFile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_format(self):
        """Получает формат видео файла"""
        if self.exists():
            print(f"Получение формата видео файла... {self.name}")
        else:
            print(f"Получение формата видео файла невозможно, файла {self.name} не существует")

    def get_metadata(self):
        """Получает метаданные видео файла"""
        if self.exists():
            print(f"Получение метаданных... {self.name}")
        else:
            print(f"Получение метаданных видео файла невозможно, файла {self.name} не существует")


video = VideoFile('example.mov')
video.get_format()
video.get_metadata()


class RemoteMediaFile(MediaFile):
    def __init__(self, bucket_name, storage_file, *args, **kwargs):
        self.bucket_name = bucket_name
        self.storage_file = storage_file
        self.local_file_path = Path(storage_file.split('/')[-1])
        print('Создание S3 клиента...')
        super().__init__(self.local_file_path, *args, **kwargs)

    def download(self):
        """Загружает файл на локальный диск"""
        try:
            print('Загрузка файла из облака...')
            print(f"Файл {self.local_file_path} загружен из облака.")
        except ConnectionError:
            print("Ошибка при подключении к s3-like storage")

    def upload(self):
        """Загружает локальный файл в облако"""
        try:
            print('Загрузка файла в облако...')
            print(f"Файл {self.local_file_path} загружен в облако.")
        except ConnectionError:
            print("Ошибка при подключении к s3-like storage")


class RemoteImageFile(RemoteMediaFile, ImageFile):
    def get_metadata(self):
        """Получает метаданные изображения из облака"""
        self.download()
        super().get_metadata()


remote_image = RemoteImageFile('my-bucket', 'bucket/example.jpg', author='Patrick7777777')
remote_image.get_format()
remote_image.get_metadata()

