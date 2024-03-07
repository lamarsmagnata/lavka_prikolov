docker run -d --name lavka_prikolov-postgres \
-e POSTGRES_PASSWORD=djangoroot \
-e POSTGRES_DB=django_db \
-e POSTGRES_USER=django \
-p 5432:5432 \
-v ${PWD}/dumps:/docker-entrypoint-initdb.d postgres:14