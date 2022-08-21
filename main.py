from files import Files
from args import args


def main():
    file = Files()
    file.finding_directory()
    file.replacing_files(args.image, args.video, args.other)
    file.file_attributes(args.image, args.video, args.other, args.size)
    file.additional_checks()
