import os
from args import args


class Files:
    def __init__(self):
        self.path = args.path
        if not self.path:
            raise BaseException('Укажите путь -p')

        self.img = os.path.join(self.path, 'img')
        if not os.path.exists(self.img):
            os.makedirs(self.img)
        self.video = os.path.join(self.path, 'video')
        if not os.path.exists(self.video):
            os.makedirs(self.video)
        self.other = os.path.join(self.path, 'other')
        if not os.path.exists(self.other):
            os.makedirs(self.other)
        self.paths = [self.img, self.video, self.other]

        self.ext_img = ('.jpg', '.png', '.gif')
        self.ext_video = ('.webm', '.mp4')

    def finding_directory(self) -> os.DirEntry:
        return os.scandir(self.path)

    def replacing_files(self, img, video, other):
        for m in self.finding_directory():
            name = os.path.basename(m)
            if img or video or other:
                if img:
                    if name.endswith(self.ext_img):
                        os.replace(m, os.path.join(self.img, name))
                if video:
                    if name.endswith(self.ext_video):
                        os.replace(m, os.path.join(self.video, name))
                if other:
                    if os.path.isfile(os.path.join(self.path, name)) and not name.endswith(
                            self.ext_img) and not name.endswith(self.ext_video):
                        os.replace(m, os.path.join(self.other, name))

        if not img:
            print('\n---For sorting images by size enter arg "-i"')
        if not video:
            print('\n---For sorting video by size enter arg "-v"')
        if not other:
            print('\n---For sorting other files by size enter arg "-o"\n')

    def file_attributes(self, image, video, other, size):
        for n in self.finding_directory():
            if n.name == 'img':
                for f in os.scandir(self.img):
                    name = os.path.basename(f)
                    o = os.stat(os.path.join(self.img, name)).st_size
                    if image:
                        big_img = os.path.join(self.img, 'Большое изображение')
                        small_img = os.path.join(self.img, 'Маленькое изображение')
                        if os.path.isfile(f) and o >= int(size):
                            if not os.path.exists(os.path.join(big_img)):
                                os.makedirs(os.path.join(big_img))
                            os.replace(f, os.path.join(big_img, name))
                        elif os.path.isfile(f) and o <= int(size):
                            if not os.path.exists(os.path.join(small_img)):
                                os.makedirs(os.path.join(small_img))
                            os.replace(f, os.path.join(small_img, name))

            elif n.name == 'video':
                for f in os.scandir(self.video):
                    name = os.path.basename(f)
                    o = os.stat(os.path.join(self.video, name)).st_size
                    if video:
                        big_vid = os.path.join(self.video, 'Большое видео')
                        small_vid = os.path.join(self.video, 'Маленькое видео')
                        if os.path.isfile(f) and o >= int(size):
                            if not os.path.exists(os.path.join(big_vid)):
                                os.makedirs(os.path.join(big_vid))
                            os.replace(f, os.path.join(big_vid, name))
                        elif os.path.isfile(f) and o <= int(size):
                            if not os.path.exists(os.path.join(small_vid)):
                                os.makedirs(os.path.join(small_vid))
                            os.replace(f, os.path.join(small_vid, name))

            elif n.name == 'other':
                for f in os.scandir(self.other):
                    name = os.path.basename(f)
                    o = os.stat(os.path.join(self.other, name)).st_size
                    if other:
                        big_file = os.path.join(self.other, 'Большой файл')
                        small_file = os.path.join(self.other, 'Маленький файл')
                        if os.path.isfile(f) and o >= int(size):
                            if not os.path.exists(os.path.join(big_file)):
                                os.makedirs(os.path.join(big_file))
                            os.replace(f, os.path.join(big_file, name))
                        elif os.path.isfile(f) and o <= int(size):
                            if not os.path.exists(os.path.join(small_file)):
                                os.makedirs(os.path.join(small_file))
                            os.replace(f, os.path.join(small_file, name))

    def additional_checks(self):
        for directory in self.paths:
            f = os.scandir(directory)
            for d in f:
                if any(i for i in ('изображение', 'видео', 'файл') if i in d.name):
                    m = os.scandir(os.path.join(d))
                    for s in m:
                        n = os.path.basename(s)
                        if os.path.isfile(s):
                            os.replace(s, os.path.join(self.path, n))
                            self.replacing_files(img=True, video=True, other=True)
                            self.file_attributes(args.image, args.video, args.other, args.size)
                        else:
                            break

# asdasd