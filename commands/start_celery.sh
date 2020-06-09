 #!/bin/bash

rm /srv/project/run/celery.pid
celery -A develops_today_test worker -l info --workdir=/srv/project/src --pidfile=/srv/project/run/celery.pid