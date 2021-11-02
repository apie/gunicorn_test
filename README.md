# gunicorn_test
Two endpoints. One normal and one slow.
Three servers:
1. Runserver
2. Gunicorn
3. Gunicorn with uvicorn

Also a proxy

Test: 
-----

    curl http://localhost:800{1,2,3}/
    curl http://localhost:800{1,2,3}/slow/

	siege --delay .5 --concurrent 10 -i http://localhost:8001
    or
	siege --delay .5 --concurrent 10 -i http://localhost:80

    telnet localhost 8126 #statsd admin interface

    curl http://localhost/nginx_status


https://github.com/statsd/statsd/blob/master/docs/admin_interface.md

