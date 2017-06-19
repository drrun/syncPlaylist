import urllib2
import platform

download_url = {
    "Windows": "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip",
    "Darwin": "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-macosx.zip"
}


def download(file_path):
    """get code from https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
    """
    phantomjs_file = file_path + download_url[platform.system()].split('/')[-1]
    u = urllib2.urlopen(download_url[platform.system()])
    f = open(phantomjs_file, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (phantomjs_file, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = "%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        print status
    f.close()
    return phantomjs_file


def unzip(zip_file, file_path):
    import zipfile
    zip_ref = zipfile.ZipFile(zip_file, 'r')
    zip_ref.extractall(file_path)
    zip_ref.close()


def _print(msg):
    print msg.encode('utf8')