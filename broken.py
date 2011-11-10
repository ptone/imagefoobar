import os, sys
import time
import shutil
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imagefoobar.settings")

from django.conf import settings

from dummy.models import Dummy
import Image
import ImageFile


ImageFile.MAXBLOCK = 1024*1024*5


try:
    pass
    # shutil.rmtree(settings.MEDIA_ROOT)
except:
    pass

sample = 'pony.jpg'

Dummy.objects.all().delete()

# Memory use stays constant around 30MB on my machine
# print 'plain PIL'
# for i in xrange(100):
    # x = Image.open(open(sample, 'rb'))
    # img = x.resize((600, 600))

# Memory spikes upwards of 300
print 'imagekit'
for i in xrange(100):
    d = Dummy()
    d.spec_image.save('foo.jpg', open(sample, 'rb'))

print 'done'
time.sleep(20)

