# gunicorn_test
Two endpoints. One normal and one slow.


Test: 
-----

    curl http://localhost:800{1,2,3}/
    curl http://localhost:800{1,2,3}/slow/

	siege --delay .5 --concurrent 10 -i http://localhost:8001

