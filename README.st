production start celery
            CMD1="$SITES_PATH/$SITE/$ENVIRONMENT_PATH/bin/celery multi start responding_worker -Q responding -A rno -l info -c 1 --workdir=/home/rno/rno/ --pidfile=/home/rno/run/celery_responding.pid --logfile=/home/rno/log/celery_responding.log" 
            CMD2="$SITES_PATH/$SITE/$ENVIRONMENT_PATH/bin/celery multi start emailing_worker -Q emailing -A rno -l info -c 1 --workdir=/home/rno/rno/ --pidfile=/home/rno/run/celery_emailing.pid --logfile=/home/rno/log/celery_emailing.log" 

production stop celery
        CMD1="$SITES_PATH/$SITE/$ENVIRONMENT_PATH/bin/celery multi stopwait responding_worker -A rno -l info -c 1 --workdir=/home/rno/rno/ --pidfile=/home/rno/run/celery_responding.pid --logfile=/home/rno/log/celery_responding.log" 
        CMD2="$SITES_PATH/$SITE/$ENVIRONMENT_PATH/bin/celery multi stopwait emailing_worker -A rno -l info -c 1 --workdir=/home/rno/rno/ --pidfile=/home/rno/run/celery_emailing.pid --logfile=/home/rno/log/celery_emailing.log" 


development start celery
env/bin/celery multi start responding_worker -Q responding -A rno -l info -c 1 --workdir=/home/user/rno-dev/ --pidfile=/home/user/celery_responding.pid --logfile=/home/user/celery_responding.log
env/bin/celery multi start emailing_worker -Q emailing -A rno -l info -c 1 --workdir=/home/user/rno-dev/ --pidfile=/home/user/celery_emailing.pid --logfile=/home/user/celery_emailing.log

development stop celery
        env/bin/celery multi stopwait responding_worker -A rno -l info -c 1 --workdir=/home/user/rno-dev/ --pidfile=/home/user/celery_responding.pid --logfile=/home/user/celery_responding.log 
        env/bin/celery multi stopwait emailing_worker -A rno -l info -c 1 --workdir=/home/user/rno-dev/ --pidfile=/home/user/celery_emailing.pid --logfile=/home/user/celery_emailing.log 
