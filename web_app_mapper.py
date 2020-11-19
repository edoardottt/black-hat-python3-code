import os
import queue
import threading
import urllib.error
import urllib.parse
import urllib.request

threads = 10
target = "http://blackhatpython.com"
directory = "."
filters = [".jpg", ".gif", "png", ".css"]

os.chdir(directory)
web_paths = queue.Queue()

for r, d, f in os.walk("."):
    for files in f:
        remote_path = "%s/%s" % (r, files)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)


def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = "%s%s" % (target, path)
        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            print("[%d] => %s" % (response.code, path))
            response.close()
        except urllib.error.HTTPError as error:
            print("Failed %s" % error.code)
            pass


for i in range(threads):
    print("Spawning thread: %d" % i)
    t = threading.Thread(target=test_remote)
    t.start()
